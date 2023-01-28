from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from .models import Persons
from .serializers import PersonsSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template import loader

@api_view(['GET','POST'])
def persons_operations(request,format=None):
    if request.method=='GET':
        persons=Persons.objects.all()
        serializer=PersonsSerializer(persons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        data = JSONParser().parse(request)
        serializer = PersonsSerializer(data=data)
        if serializer.is_valid():
            per = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers={"Location": "api/v1/persons/" + str(per.id)})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PATCH','DELETE'])
def person_id_operations(request,id,format=None):
    try:
        person=Persons.objects.get(id=id)
    except Persons.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=PersonsSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='PATCH':
        serializer=PersonsSerializer(person,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)