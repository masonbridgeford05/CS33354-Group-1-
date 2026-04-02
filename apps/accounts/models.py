from django.db import models


# Create your models here.

#DBMgr
class User(models.Model):
    userId = models.AutoField(primary_key = True)
    userName = models.CharField(max_length = 16)
    userEmail = models.EmailField(unique = True)
    userPassword = models.CharField(max_length = 32)

