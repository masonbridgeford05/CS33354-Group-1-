from django.shortcuts import render, redirect
from django.views import View
from apps.accounts.models import User
from apps.accounts.validator import Validator
from apps.game.GameController import GameController

class UserController(View):
    def loginUser(self, request, username_or_email, userPassword):
        # Uses the model's auth logic
        user = User.authenticateUser(username_or_email, userPassword) 
        if user:
            request.session["user_id"] = user.userId 
            request.session.modified = True 
            return True
        return False

    def createUserAccount(self, userName, userEmail, userPassword):
        if Validator.isValidEmail(userEmail) and Validator.isValidPassword(userPassword):
            user = User.createUserAccount(userName, userEmail, userPassword)
            return user
        return None

    def fetchUserData(self, userId):
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            return None
    
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
        
    def logoutUser(self, request):
        if hasattr(request, 'session'):
            request.session.flush()
            return True
        return False

def login_view(request):
    if request.method == "POST":
        u_identifier = request.POST.get('username') or request.POST.get('userEmail')
        u_pass = request.POST.get('password') or request.POST.get('userPassword')
        
        controller = UserController()
        if controller.loginUser(request, u_identifier, u_pass):
            return redirect('signal_game_start') 
        
        print(f"DEBUG: Login failed for {u_identifier}")
            
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        p1 = request.POST.get('password') or request.POST.get('password1') or request.POST.get('userPassword')
        p2 = request.POST.get('password2')
        
        # 1. Check if passwords match
        if p2 and p1 != p2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # 2. Check if username or email already exists
        if User.objects.filter(userName=u_name).exists() or User.objects.filter(userEmail=u_email).exists():
            # Return 200 to stay on the page as the test expects
            return render(request, 'register.html', {'error': 'User already exists'})

        controller = UserController()
        if controller.createUserAccount(u_name, u_email, p1):
            return redirect('login')
            
    return render(request, 'register.html')

def logout_view(request):
    controller = UserController()
    controller.logoutUser(request)
    return redirect('login')