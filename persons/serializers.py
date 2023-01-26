from rest_framework import serializers
from .models import Persons
class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persons
        fields=['id','name','age','address','work']