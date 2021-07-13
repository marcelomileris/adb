from rest_framework import viewsets
from person.api import serializers
from person import models

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()

class Person_typeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Person_typeSerializer
    queryset = models.Person_type.objects.all()  

class Person_media_typeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Person_media_typeSerializer
    queryset = models.Person_media_type.objects.all()  
