from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import check_password

# Create your models here.
#DBMgr
class User(AbstractBaseUser):

    userId = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 16)
    userEmail = models.EmailField(unique = True)

    USERNAME_FIELD = 'userEmail'
    REQUIRED_FIELDS = ['username']

    @staticmethod
    def createUserAccount(username, userEmail, userPassword):
        user = User(username = username, userEmail = userEmail)
        user.set_password(userPassword)
        user.save()
        return user

    # Keeping for tests that are already written, but not used in views
    @staticmethod
    def checkUserCredentials(userEmail, userPassword):
        try:
            user = User.objects.get(userEmail = userEmail)
            return user.check_password(userPassword)
        except User.DoesNotExist:
            return False
        
    @staticmethod
    def authenticateUser(userEmail, userPassword):
        try:
            user = User.objects.get(userEmail=userEmail)
            if user.check_password(userPassword):
                return user
        except User.DoesNotExist:
            pass
        return None
     
    @property
    def is_active(self): return True

    @property
    def is_staff(self): return False

    @property
    def is_superuser(self): return False 

    def has_perm(self, perm, obj=None): return True
    def has_module_perms(self, app_label): return True
