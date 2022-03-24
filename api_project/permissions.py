from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit the profile"""

    def has_object_permission(self,request,view,obj):
        """check permission for user to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow user to update their own status"""

    def has_object_permission(self,request,view,obj):
        """check user is only updating own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
