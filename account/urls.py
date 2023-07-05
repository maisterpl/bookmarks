from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login_from_book/', views.user_login, name='login_from_book'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
