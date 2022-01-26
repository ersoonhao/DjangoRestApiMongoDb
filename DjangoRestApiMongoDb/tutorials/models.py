from django.db import models

# Create your models here.


# Django model. Similar to sequalize ORM
# python manage.py makemigrations tutorials

# from model to DD: https://docs.djangoproject.com/en/4.0/topics/migrations/


#https://stackoverflow.com/questions/70185942/why-i-am-getting-not-implemented-error-database-objects-do-not-implement-truth#comment124677085_70191268
# requires django-mongoengine 

class Tutorial(models.Model):
    #hmm mongo uses a partition key & sorting key. Where is that defined?
    # ohh it is generated in migrations files. interesting. 

    # typo @ max_length 
    title= models.CharField(max_length=200, blank=False, default='')
    description =models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)

