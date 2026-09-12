from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path(
        "auth/register/",
         UserRegistrationAPIView.as_view(),
         name="register"
        ),
    path(
        "auth/login/",
        UserLoginAPIView.as_view(),
        name="login"
    ),
]