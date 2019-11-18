Applications
============

This directory is used for custom applications. You can safely remove this directory, if you do not plan to develop custom applications. 
Most of a Django project’s apps will be installed into the Python path and not be kept in your project root.

``` bash
$ python3 manage.py startapp <application_name>
```

A Django project typically consists of many applications. 
Django applications should follow the Unix philosopy of, “Do one thing and do it well.”, with a focus on being small and modular, mirroring Django’s “loose coupling” design philosophy.