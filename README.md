My preferred minimal Django setup which includes:

 * [django-allauth](http://www.intenct.nl/projects/django-allauth) with email address as the username
 * [django-rest-framework](http://www.django-rest-framework.org)
 * [django-classy-settings](http://django-classy-settings.readthedocs.org) to manage various environment settings
 
Installation:

  ```shell
  virtualenv env
  . env/bin/activate
  pip install django
  django-admin.py startproject <project_name> . --template=https://github.com/rapilabs/django-template/archive/master.zip
  pip install -r requirements.txt
  pip install -r dev-requirements.txt
  ```
