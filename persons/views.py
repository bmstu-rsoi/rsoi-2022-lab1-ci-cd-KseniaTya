from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Persons
from .serializers import PersonSerializer


#Методы GET и POST для всех объектов
@csrf_exempt
@api_view(['GET','POST'])
def persons_operations(request):
    if request.method == 'GET':
        persons = Persons.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PersonSerializer(data=data)
            if serializer.is_valid():
                per = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers={"Location" :"api/v1/persons/"+str(per.id)})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #return JsonResponse(serializer.data, status=201)
            #return JsonResponse(serializer.errors, status=400)


#Методы GET, PATCH, DELETE для объектов по id
@csrf_exempt
@api_view(['GET','PATCH','DELETE'])
def person_id_operations(request, pk):
    try:
        persons = Persons.objects.get(pk=pk)
    except Persons.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(persons)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(persons, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #return JsonResponse(serializer.data)
        #return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        persons.delete()
        return HttpResponse(status=204)