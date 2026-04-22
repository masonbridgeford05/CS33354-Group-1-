from django.contrib import admin
from django.urls import path
from apps.accounts import views as account_views
from apps.game import views as game_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts Routes
    path('login/', account_views.login_view, name='login'), 
    path('register/', account_views.register_view, name='register'),
    path('logout/', account_views.logout_view, name='logout'),
    
    # Game Routes-
    # Named 'signal_game_start' to match the redirect in views.py
    path('game/start/', game_views.signal_game_start, name='signal_game_start'),
]