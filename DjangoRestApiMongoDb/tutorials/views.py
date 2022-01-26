from django.shortcuts import render
from django.http import JsonResponse
# from models import *
#decorators
# from rest_framework import api_view
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST','DELETE'])
def tutorial_list(request):
    # getter for list of tutorials , post a new tutorial, delete tutorials list
    return None 


@api_view(['GET', 'PUT','DELETE'])
def tutorial_detail(request,pk):
    # find tutotrial by pk 
    try:
        tutorial=Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'error':'Tutorial not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def tutorial_list_published(request):
    # getter for list of published tutorials
    return None