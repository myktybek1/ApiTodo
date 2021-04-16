from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todoApi.serializers import *
from todoApi.models import Posts

@api_view(['GET'])
def postview(request):
    todo_urls ={
        'List': '/post-list/',
        'Detail View': '/post-detail/<int:pk>',
        'Create': '/post-create/',
        'Update': '/post-update/<int:pk>',
        'Delete': '/post-delete/<int:pk>',
    }
    return Response(todo_urls)

class PostsListView(generics.ListAPIView):
    serializer_class = PostsSerialiser
    queryset = Posts.objects.all().order_by('-id')

class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerialiser
    queryset = Posts.objects.all()

class PostsCreateView(generics.CreateAPIView):
    serializer_class = PostsSerialiser

class PostsUpdateView(generics.UpdateAPIView):
    serializer_class = PostsSerialiser
    queryset = Posts.objects.all()

class PostsDeleteView(generics.DestroyAPIView):
    serializer_class = PostsSerialiser
    queryset = Posts.objects.all()







