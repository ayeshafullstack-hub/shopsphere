from rest_framework import generics, status
from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegistrationSerializer

# Create your views here.
class UserLoginAPIView(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            from django.contrib.auth.models import User
            
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password."},
                status = status.HTTP_401_UNAUTHORIZED
            )
        
        user = authenticate(
            username=user.username,
            password=password
        )
        
        if user is None:
            return Response(
                {"error":"Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "access":str(refresh.access_token),
                "refresh":str(refresh),
            },
            status=status.HTTP_200_OK
        )
#UserProfileAPIView
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        return Response(
            {
                "id":user.id,
                "username":user.username,
                "email":user.email,
                "role":user.profile.role,
            },
            status=status.HTTP_200_OK
        )
    
    def patch(self,request):
        user=request.user
        
        username = request.data.get("username")
        email = request.data.get("email")
        
        if username:
            user.username = username
        
        if email: 
            user.email=email
        
        user.save()
        
        return Response(
            {
                "id":user.id,
                "username":user.username,
                "email":user.email,
                "role":user.profile.role,
            },
            status=status.HTTP_200_OK
        )    

#User RegistrationAPIView
class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def create(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )