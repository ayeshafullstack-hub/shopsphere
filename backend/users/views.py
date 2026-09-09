from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

# Create your views here.
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