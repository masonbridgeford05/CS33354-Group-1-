from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
#DBMgr
class User(models.Model):

    userId = models.AutoField(primary_key = True)
    userName = models.CharField(max_length = 16)
    userEmail = models.EmailField(unique = True)
    userPassword = models.CharField(max_length = 128)

    def createUserAccount(userName, userEmail, userPassword):
        hashed_password = make_password(userPassword)
        user = User(userName = userName, userEmail = userEmail, userPassword = hashed_password)
        user.save()
        return user

    def checkUserCredentials(userEmail, userPassword):
        try:
            user = User.objects.get(userEmail = userEmail)
            return check_password(userPassword, user.userPassword)
        except User.DoesNotExist:
            return False

