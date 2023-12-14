from django.urls import path
from accounts.views import user_login, user_logout, create_user

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", create_user, name="signup"),
]
