from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.accounts.models import User
from apps.accounts.validator import Validator


class UserController(View):
    def login_view(request):
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html');
        else:
            # error here

    def create_account_view(request): 
        if request.method == 'POST':
            

# class UserController(View):
#     def createUserAccount(self, userName, userEmail, userPassword):
#         if Validator.isValidEmail(userEmail) and Validator.isValidPassword(userPassword):
#             return User.createUserAccount(userName, userEmail, userPassword)
#         return None
    
#     def loginUser(self, userEmail, userPassword):
#         if User.checkuserCredentials(userEmail, userPassword):
#             return True
#         return False
        
#     def fetchUserData(self, userID):
#         try:
#             return User.objects.get(user_ID = userID)
#         except User.DoesNotExist:
#             return None

#     def processUserRequest(self, userId, userRequest):
#         user = self.fetchUserData(userId)
#         if not user:
#             return "User does not exist"

#         if userRequest == "START_LEVEL_EASY":
#             return "Level Easy started"
#         elif userRequest == "START_LEVEL_HARD":
#             return "Level Hard started"
#         elif userRequest == "SUBMIT_GUESS":
#             return "Checking..."
#         elif userRequest == "END_GAME":
#             return "Game Over"

#         return "Unknown Request"

#     def logoutUser(self, request):
#         if hasattr(request, 'session'):
#             request.session.flush()
#             return True
#         return False
    
#     @staticmethod
#     def login_view(request):
#         return render(request, 'login.html')
    
#     @staticmethod
#     def register_view(request):
#         return render(request, 'createaccount.html')
    
#     @staticmethod
#     def logout_view(request):
#         controller = UserController()
#         controller.logoutUser(request)
#         return redirect('home')
    
#     @staticmethod
#     def home_view(request):
#         return render(request, 'home.html')



