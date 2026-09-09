from django.urls import path
from .views import UserRegistrationAPIView

urlpatterns = [
    path(
        "auth/register/",
         UserRegistrationAPIView.as_view(),
         name="register"
        )
]