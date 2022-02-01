note to self:

Self learning for vue3, Django & AWS deployment for non-relational database MongoDB with aws documentDB 

---commands to note---

Django Specific commands:
django-admin startproject projectName


Server Commands(using python 3): 
python3 manage.py startapp appname # in this case it creates a default tutorials django folder structure 

python3 manage.py makemigrations tutorials  # creates tables in mongo from specified model 
python3 manage.py runserver 8080

python3 manage.py showmigrations --list # shows all unapplied migration

Impt Dependencies:
pip install djangorestframework
pip install django-cors-headers #CorsMiddleware should be specified and places as high as possible in settings.py before any middleware can generate responses e.g CommonMiddleware


References:
https://www.bezkoder.com/django-angular-13-crud/#Setup_Database_engine
https://www.bezkoder.com/vue-3-crud/#Create_Data_Service

