from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True
    )
    
    password_confirm = serializers.CharField(
        write_only = True,
        required = True
    )
    
    class Meta:
        model = User
        fields = ["id","username","email","password","password_confirm"]
        extra_kwargs = {
            "email" : {
                "required":True
            }
        }
        
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )
        return value
    
    def validate_password(self,value):
        validate_password(value)
        return value
    
    def validate(self,data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError({
                "password_confirm":
                    "Passwords do not match."
            })
        return data
    
    def create(self,validated_data):
        validated_data.pop("password_confirm")
        
        user = User.objects.create_user(
            username=validated_data["username"],
            email = validated_data["email"],
            password=validated_data["password"],
            
        )
        
        UserProfile.objects.create(
            user=user,
            role=UserProfile.Role.CUSTOMER
        )
        
        return user