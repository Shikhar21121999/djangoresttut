from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission class to allow edit and delete acess
    to the owner of the object(snippet)
    '''

    def has_object_permission(self, request, view, obj):
        '''
        function to overide object permissions in BasePermission class
        and give acess for save methods to any request
        but give acess to update and delte only to creator of the snippet
        '''
        if request.method == 'OPTIONS':
            return False
        if request.method in permissions.SAFE_METHODS:
            # gives acess if method are get options and head
            return True

        return obj.owner == request.user
