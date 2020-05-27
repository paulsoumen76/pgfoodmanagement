from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class PgMenu(models.Model):
    day=models.CharField(max_length=20)
    breakfast=models.CharField(max_length=20)
    lunch=models.CharField(max_length=20)
    dinner=models.CharField(max_length=20)
class PersonalDetails(models.Model):
    name=models.CharField(max_length=20)
    room_no=models.IntegerField()
    mobile_no=models.IntegerField()
class BreakfastAgreement(models.Model):
    date=models.DateField(auto_now_add=True)
    breakfast=models.CharField(max_length=3)
class LunchAgreement(models.Model):
    date=models.DateField(auto_now_add=True)
    lunch=models.CharField(max_length=3)
class DinnerAgreement(models.Model):
    date=models.DateField(auto_now_add=True)
    dinner=models.CharField(max_length=3)
class Student(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    dp=models.ImageField(upload_to='pgfoodmanagement/user_image')
