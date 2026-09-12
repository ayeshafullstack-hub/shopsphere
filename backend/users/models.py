from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    
    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        SELLER = "SELLER","Seller"
        ADMIN = "ADMIN","Admin"
        
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )
    
    def _str__(self):
        return f"{self.user.username}-{self.role}"