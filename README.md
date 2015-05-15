My preferred minimal Django setup which includes:

 * django-allauth with email address as the username
 * django-rest-framework
 
Installation:

  ```shell
  virtualenv env
  . env/bin/activate
  pip install django
  django-admin.py startproject <project_name> --template=https://github.com/rapilabs/django-template/archive/master.zip
  ```
