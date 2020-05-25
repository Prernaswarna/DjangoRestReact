from fixer.models import User , Project
from rest_framework import permissions

class IsTeamOrReadOnly(permissions.BasePermission):
    def has_object_permission(self , request , view , obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        for p in obj.project_members:
            if(request.user.id == p):
                return True
        if request.user.typeofuser==True:
            return True
        return False


class IsAdminOrNoAccess(permissions.BasePermission):
    def has_permission(self , request , view ):
        if request.method == 'GET':
            if request.user.is_authenticated :
                if request.user.typeofuser == True:
                    return True
                else:
                    return False


