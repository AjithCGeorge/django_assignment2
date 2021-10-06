from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profiles(models.Model):
    mobile_num=models.CharField(max_length=20)
    residence=models.CharField(max_length=100)
    email_alt=models.EmailField()
    education=models.CharField(max_length=50)
    hobbies=models.CharField(max_length=100)
    profile_user=models.ForeignKey(User,on_delete=models.CASCADE,default=None,unique=True)