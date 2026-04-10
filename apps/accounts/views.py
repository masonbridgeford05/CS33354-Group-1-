from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.models import User
from apps.accounts.validator import Validator
# Create your views here.

class UserController(View):
    def createUserAccount(self, userName, userEmail, userPassword):
        if Validator.isValidEmail(userEmail) and Validator.isValidPassword(userPassword):
            return User.createUserAccount(userName, userEmail, userPassword)
        return None
    
    def loginUser(self, request, userEmail, userPassword):
        if User.checkUserCredentials(userEmail, userPassword):
            request.session["user_id"] = User.objects.get(userEmail=userEmail).userId
            return True
        return False
        
    def fetchUserData(self, userId):
        try:
            return User.objects.get(userId = userId)
        except User.DoesNotExist:
            return None
    
    def processUserRequest(self, userId, userRequest):
        user = self.fetchUserData(userId)
        if not user:
            return "User does not exist"
        
        if userRequest == "START_LEVEL_EASY":
            return "Level Easy started"
        elif userRequest == "START_LEVEL_HARD":
            return "Level Hard started"
        elif userRequest == "SUBMIT_GUESS":
            return "Checking..."
        elif userRequest == "END_GAME":
            return "Game Over"
        
        return "Unknown Request"
        
    def logoutUser(self, request):
        if hasattr(request, 'session'):
            request.session.flush()
            return True
        return False