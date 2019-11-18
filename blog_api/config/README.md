The Django root directory [project_name]
======

The Django root directory will be named according to the project name you specified in django-admin startproject [projectname]. 
This directory is the project’s connection with Django.

```text
[project_name]/settings/
```

Instead of a plain settings-file, the configuration is split into several files in this Python module. For an in-depth documentation of these settings see Settings.

```text
[project_name]/urls.py
```

The root URL configuration of the project. The only configured set of urls is the admin-application. For background information see The Django Book Chapter 3 and The Django Book Chapter 8.

```text
[project_name]/wsgi.py
```
Deploying Django makes use of WSGI, the Pythonic way of deploying web applications. See the official settings documentation on WSGI for more details. The default WSGI-application is modified to use our settings-module.