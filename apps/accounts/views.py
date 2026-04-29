from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.models import User
from apps.accounts.validator import Validator
from apps.game.GameController import GameController
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.hashers import check_password
from datetime import date
from django.db.models import Sum
from apps.game.models import GameResult
from apps.accounts.models import User


class UserController(View):

    def processUserRequest(self, request, userRequest):
        userId = request.session.get("user_id")
        user = self.fetchUserData(userId)
        if not user:
            return "User does not exist"
        
        if userRequest == "START_LEVEL_EASY":
            controller = GameController(0, userId)
            return "Level Easy started"
        elif userRequest == "START_LEVEL_HARD":
            controller = GameController(1, userId)
            return "Level Hard started"
        elif userRequest == "SUBMIT_GUESS":
            return "Checking..."
        elif userRequest == "END_GAME":
            return "Game Over"
        return "Unknown Request"
    
    def login_view(request):
        storage = get_messages(request)
        for _ in storage:
            pass
        if request.method == 'POST':
            name_input = request.POST.get('userName')
            pass_input = request.POST.get('userPassword')

            try:
                # Look for the user in your custom User model
                user = User.objects.get(username=name_input)
            
                # Check if the password matches
                if check_password(pass_input, user.password):
                    request.session['user_id'] = user.userId
                    request.session['user_name'] = user.username
                    request.session.modified = True
                    messages.success(request, f"Welcome back, {user.username}!")
                    return redirect('dashboard')
                else:
                    messages.error(request, "Incorrect password. Please try again.")
        
            except User.DoesNotExist:
                messages.error(request, "Username not found. Have you registered yet?")

        return render(request, 'login.html')
    
    def register_view(request):
        storage = get_messages(request)
        for _ in storage:
            pass

        if request.method == 'POST':
            email_input = request.POST.get('userEmail')
            name_input = request.POST.get('userName')
            pass_input = request.POST.get('userPassword')
            if User.objects.filter(userEmail=email_input).exists():
                messages.error(request, "An account with this email already exists.")
            elif User.objects.filter(username=name_input).exists():
                messages.error(request, "That username is already taken.")
            elif len(pass_input) < 12:
                messages.error(request, "Password must be at least 12 characters.")
            else:
                User.objects.create(
                    userEmail=email_input,
                    username=name_input,
                    userPassword=pass_input
                )
                messages.success(request, "Account created! Please log in.")
                return redirect('login')

            return render(request, 'createaccount.html', {
                'typed_email': email_input,
                'typed_name': name_input
            })

        return render(request, 'createaccount.html')
    
    def logout_view(request):
        storage = get_messages(request)
        for _ in storage:
            pass
        if hasattr(request, 'session'):
            request.session.flush()
        return redirect('login')
    
    def dashboard_view(request):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')

        user = User.objects.get(userId=user_id)
    
        # Calculate total points
        total_points = GameResult.objects.filter(user_id=user).aggregate(Sum('score'))['score__sum'] or 0
    
        # Check if they played today
        has_played = GameResult.objects.filter(user_id=user, date_played__date=date.today()).exists()

        return render(request, 'dashboard.html', {
            'user': user,
            'total_points': total_points,
            'has_played': has_played
        })
    
    @staticmethod
    def home_view(request):
        return render(request, 'home.html')

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

