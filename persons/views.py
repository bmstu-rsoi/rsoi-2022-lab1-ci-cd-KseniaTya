from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Persons
from .serializers import PersonsSerializer


@api_view(['GET', 'POST'])
def persons_operations(request):
    if request.method == 'GET':
        persons = Persons.objects.all()
        serializer = PersonsSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    if request.method == 'POST':
        serializer = PersonsSerializer(data=request.data)
        if serializer.is_valid():
            d = serializer.save()
            response = Response(status=201)
            response['Location'] = '/api/v1/persons/{personId}'.format(personId=d.id)
            return response
        return JsonResponse(serializer.data, safe=False, status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
def person_id_operations(request, id):
    try:
        person = Persons.objects.get(id=id)
    except Persons.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = PersonsSerializer(person)
        return Response(serializer.data, status=200)
    if request.method == 'PATCH':
        serializer = PersonsSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=204)
