from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=16)
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=256)

    @staticmethod
    def createUserAccount(userName, userEmail, userpass):
        try:
            user = User.objects.create(
                userName=userName, 
                userEmail=userEmail, 
                userPassword=make_password(userpass)
            )
            return user
        except Exception:
            return None

    @staticmethod
    def authenticateUser(identifier, password):
        try:
            user = User.objects.get(userEmail=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(userName=identifier)
            except User.DoesNotExist:
                return None
        
        if check_password(password, user.userPassword):
            return user
        return None