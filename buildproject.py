#!/usr/bin/env python
import os
import subprocess
import shutil
from django.core import management
#from project import settings

BOILERPLATE_DIR = 'html5boilerplate'


def buildproject():
    print 'Removing old \'publish\' directories...'
    if os.path.exists(os.path.join(BOILERPLATE_DIR, 'project', 'templates_publish')):
        shutil.rmtree(os.path.join(BOILERPLATE_DIR, 'project', 'templates_publish'))
        os.mkdir(os.path.join(BOILERPLATE_DIR, 'project', 'templates_publish'))
    if os.path.exists(os.path.join(BOILERPLATE_DIR, 'project', 'static_publish')):
        shutil.rmtree(os.path.join(BOILERPLATE_DIR, 'project', 'static_publish'))
        os.mkdir(os.path.join(BOILERPLATE_DIR, 'project', 'static_publish'))
    if os.path.exists(os.path.join(BOILERPLATE_DIR, 'project', 'static_tmp')):
        shutil.rmtree(os.path.join(BOILERPLATE_DIR, 'project', 'static_tmp'))
        
    print 'Running collectstatic...'
    #management.setup_environ(settings)
    #management.execute_from_command_line(['collectstatic', '--noinput',])
    
    #from django.contrib.staticfiles.management.commands.collectstatic import Command
    #collectstatic_command = Command()
    #collectstatic_command.handle_noargs(interactive=False)
    
    subprocess.call(['python', 'project/manage.py', 'collectstatic', '--noinput'])
    
    os.rename(os.path.join(BOILERPLATE_DIR, 'project', 'static_publish'), os.path.join(BOILERPLATE_DIR, 'project', 'static_tmp'))
        
    cwd = os.getcwd()
    os.chdir(os.path.join(BOILERPLATE_DIR, 'build'))
    print 'Starting Ant build...'
    try:
        subprocess.call(['ant', '-version'])
    except OSError:
        print 'You do not appear to have \'ant\' installed'
        return
    #retcode = subprocess.call(['ant', 'minify'])
    retcode = subprocess.call(['ant', 'build'])
    if retcode > 0:
        print 'Ant build failed'
        return
    os.chdir(cwd)
    
    print 'Moving minified templates to Django project (templates_publish)...'
    os.rename(os.path.join(BOILERPLATE_DIR, 'publish', 'project', 'templates'), os.path.join(BOILERPLATE_DIR, 'project', 'templates_publish'))
    
    print 'Moving CSS, JS and images into Django project...'
    os.rename(os.path.join(BOILERPLATE_DIR, 'publish', 'project', 'static_tmp'), os.path.join(BOILERPLATE_DIR, 'project', 'static_publish'))
    
    shutil.rmtree(os.path.join(BOILERPLATE_DIR, 'publish'))
    shutil.rmtree(os.path.join(BOILERPLATE_DIR, 'project', 'static_tmp'))
    
    
if __name__ == "__main__":
    buildproject()
