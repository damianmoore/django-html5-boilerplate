#!/usr/bin/env python

from distutils.core import setup

setup(name = 'django-html5-boilerplate',
    version = '0.1',
    description = 'Scripts for creating and builing Django projects based on HTML5 Boilerplate',
    author = 'Damian Moore',
    author_email = '',
    url = 'https://github.com/damianmoore/django-html5-boilerplate',
    packages = ['django-html5-boilerplate',],
    scripts = ['django-html5-boilerplate/startproject', 'django-html5-boilerplate/buildproject',],
    install_requires = ['django',]
)

