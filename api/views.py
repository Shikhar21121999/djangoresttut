from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    View function to display all code snippet
    if a get request is passed
    or to add a new snippet to database
    if post request is passed
    """

    if request.method == 'GET':
        # list all code snippet
        snippets = Snippet.objects.all()   # query snippet to get all objects
        # serializer the object set using snippetSerializer
        serializer = SnippetSerializer(snippets, many=True)
        # return the serialized data as a Json Response
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request.data)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # put request is used to update an entry
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
