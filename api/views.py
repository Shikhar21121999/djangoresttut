from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import Http404
# from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
import requests

from rest_framework import mixins
from rest_framework import generics


# class SnippetList(APIView):
#     '''
#     List all snippets or create a new snippet
#     using class based view
#     '''

#     def get(self, request, format=None):
#         # function that gets called when request is of get type
#         # list all code snippet
#         snippets = Snippet.objects.all()   # query snippet to get all objects
#         # serializer the object set using snippetSerializer
#         serializer = SnippetSerializer(snippets, many=True)
#         # return the serialized data as a Json Response
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):
    # query set on which to call the veiw function
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    query = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)


# class SnippetDetail(APIView):
#     '''
#     class based view to give detail
#     of a snippet supports GET,PUT,DELETE
#     for a particular snippet represented by pk
#     '''

#     def get_object(self, pk):
#         '''
#         Utility function to get object or snippet
#         reffered by pk
#         '''
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         '''
#         utility function to handel get request
#         for a snippet
#         '''
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         '''
#         Utility function to handel put request
#         for a snippet
#         '''
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#     def delete(self, request, pk, format=None):
#         '''
#         Utility function to handel DELETE request
#         and delete a snippet
#         '''
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)
