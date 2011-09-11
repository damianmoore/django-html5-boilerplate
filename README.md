django-html5-boilerplate
========================

_This project is still in it's early stages, so if you come across something
that is broken, please let me know. Patches, improvements and other feedback is
most welcome._


This project allows you to easily start a Django project based on the amazing
HTML5 Boilerplate template and build system (http://html5boilerplate.com/).

When looking for similar projects on the web, I found a few that incorporated
the template of HTML5 Boilerplate but none that would allow you to make use of
the build system for optimisation. More can be read about the build system at
http://html5boilerplate.com/docs/#Build-script but basically it will combine and
minify your JavaScript and CSS files, optimize JPEG and PNG images, minify your
HTML and revises file names of resources so you can make use of very long expire
times on your server. You should make sure you understand most of what HTML5
Boilerplate is about before trying to make too many modifications.

The django-html5-boilerplate project initially only contains two Python scripts
which are described below. These scripts will be available on your virtualenv's
path if you install via `python setup.py install` or `pip install <package>`.


- - -

Dependencies
------------

*   Python 2.x
*   Java JRE or JDK
*   Ant (1.8.2)
*   Pip
*   (Django and HTML5 Boilerplate will be downloaded when `startproject` is run)


- - -

startproject
------------

This is equivalent to Django's `django-admin.py startproject` command so use it
with your intended project name as an argument to begin your project. You are
advised to start off in a clean virtualenv with no Django project created yet.
Read more about virtualenv and virtualenvwrapper at
http://pypi.python.org/pypi/virtualenv/ and
http://pypi.python.org/pypi/virtualenvwrapper/

*   Downloads Django if necessary
*   Makes a new Django project with the name of your choice using
    `django-admin.py startproject`
*   Downloads HTML5 Boilerplate and extracts it
*   Moves HTML5 Boilerplate HTML, CSS and images into your new project under
    *templates* and *static* directories
*   Sets up the HTML5 Boilerplate installation to build from your Django project


buildproject
------------

This is run when you are about to deploy to a server. This may take a minute or
more to run as it is using html5boilerplate's Ant build optimisations. When
`buildproject` has run, the optimised version of *static* is in a separtate
directory called *static_publish* and the same goes for *templates*. Running
your server in production mode with `DEBUG=False` will cause the optimised
templates to be used by and you should configure your webserver to serve
*static_published* at the */static/* URL. The build process uses *staticfiles*
which is new in Django 1.3. This should mean that static content from
INSTALLED_APPS should also get collected together and optimised. If you're
wondering why *static* is not called *media*, Django now recommends *media* is
just used for user-uploaded content. Read more here:
http://docs.djangoproject.com/en/dev/howto/static-files/

*   Runs HTML5 Boilerplate's Ant build script to compress your Django HTML
    templates, JavaScript, CSS and Images
*   Moves the compressed output files into *static_publish* and
    *templates_publish*.
*   Your original HTML template, JavaScript, CSS and Image files are kept in
    their original location for future editing and still used when `DEBUG=True`.

