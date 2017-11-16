from __future__ import unicode_literals
from datetime import datetime, timedelta, date
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()	
    birthdate = models.DateField()
    #   desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
          return "<User object: \nid {} {} {} \nemail : {} \n age: {} \n bday : {} >".format(self.id, self.first_name, self.last_name, self.email, self.age, self.birthdate)

'''
For Shell commands
1)python manage.py make migrations 2)python manage.py migrate 3)python manage.py shell
once in shell run the following import
from apps.userApp.models import *

Create a few records in the users
User.objects.create( first_name = "Ana", last_name = "Propas", email = "aPropas@gmail.com", age=23, birthdate = "2014-07-01")
User.objects.create( first_name = "Mary", last_name = "Gonzalez", email = "mary@gmail.com", age=5, birthdate = "2012-08-02")
User.objects.create( first_name = "Sandra", last_name = "Lopez", email = "mary@gmail.com", age=5, birthdate = "2012-08-02")
----------------------
Know how to retrieve all users.
User.objects.all()
Know how to get the last user.
User.objects.last()
Know how to get the first user.
User.objects.first()
-------------------
Know how to get the users sorted by their first name (order by first_name DESC)
User.objects.all().order_by("-last_name")
-------------
user3 = User.objects.get(id=3)
user3.last_name= "Rogers"
user3.save()
------------
user4 = User.objects.get(id=4)
user4.delete()
'''
