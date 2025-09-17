# accounts/urls.py
from django.urls import path
from .views import SignupView, LoginView, UserProfileView, LogoutView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(), name="logout"),
    path('user/<uuid:userID>/profile', UserProfileView.as_view(), name='user-profile'),
]