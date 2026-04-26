from django.contrib import admin
from django.urls import path
from apps.accounts import views as account_views
from apps.game import views as game_views
from apps.leaderboard import views as leaderboard_views # Added this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts Routes
    path('login/', account_views.login_view, name='login'), 
    path('register/', account_views.register_view, name='register'),
    path('logout/', account_views.logout_view, name='logout'),
    
    # Game Routes
    path('game/start/', game_views.signal_game_start, name='signal_game_start'),

    # Leaderboard Route
    path('leaderboard/', leaderboard_views.show_leaderboard, name='leaderboard'),
    path('dashboard/', account_views.dashboard_view, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)