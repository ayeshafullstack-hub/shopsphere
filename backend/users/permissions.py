from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    message="Only customers can perform this action."
    
    def has_permission(self,request,view):
        return (
            request.user.is_authenticated
            and hasattr(request.user,"profile")
            and request.user.profile.role=="CUSTOMER"
        )
        
class IsSeller(BasePermission):
    message = "Only sellers can perform this action."
    
    def has_permission(self,request,view):
        return(
            request.user.is_authenticated
            and hasattr(request.user,"profile")
            and request.user.profile.role == "SELLER"
        )