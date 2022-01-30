from django.shortcuts import render
from django.http import JsonResponse
# from models import *
#decorators
# from rest_framework import api_view


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializer import TutorialSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST','DELETE'])
def tutorial_list(request):
    # getter for list of tutorials , post a new tutorial, delete tutorials list

    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        # serializer = TutorialSerializer(tutorials, many=True)
        # return JsonResponse(serializer.data, safe=False)
        print("receieved GET request")
     
            #synonmy for request.get 
            #https://www.django-rest-framework.org/api-guide/requests/#query_params
        title = request.query_params.get('title',None) # None here means default value
        if title is not None:
            tutorials = Tutorial.objects.filter(title__icontains=title)
        tutorials_serilizer=TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serilizer.data, safe=False) 

    elif request.method == "POST":
        tutorial_data=JSONParser().parse(request)
        tutorial_serializer=TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        count = Tutorial.Object.all().delete()
        return JsonResponse({'message':'{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    


@api_view(['GET', 'PUT','DELETE'])
def tutorial_detail(request,pk):
    # find tutotrial by pk 
    try:
        tutorial=Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'error':'Tutorial not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer =TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)
    elif request.method=='PUT': # made a typo here & in the decorator
        tutorial_data=JSONParser().parse(request)
        tutorial_serializer =TutorialSerializer(tutorial, data=tutorial_data)

        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        tutorial.delete()
        return JsonResponse({'message':'Deleted successfully'},status=status.HTTP_204_NO_CONTENT)

    # else:
    #     return JsonResponse({"error":"Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])
# def tutorial_list_published(request):


#     tutorials= Tutorial.objects.filter(published=True)
#     if request.method == 'GET':
#         tutorials_serializer= TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#     else:
#         return JsonResponse({"error":"Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    return JsonResponse({"error":"Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

