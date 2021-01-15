from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):
    '''
    Class based view to display list of snippets
    and also create new snippets
    '''
    # we want that when a new snippet is added
    # the creator to it gets added
    # as the currently logged in user
    # so we overide .perform_create() method

    # to denote permission that a request should have to run or see this view
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Class based view to display,update and delete a snippet
    delete and update operation should be possible for creator of the snippet
    '''

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    '''
    Class based view to display list of users(read only)
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
