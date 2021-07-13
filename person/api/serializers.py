from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from person.models import Person, Person_type, Person_media_type, Person_media
from rest_framework.validators import UniqueValidator
from person.validators import CPFValidator, validate_image


class Person_typeSerializer(ModelSerializer):
    class Meta:
        model = Person_type
        fields = '__all__'


class Person_media_typeSerializer(ModelSerializer):
    class Meta:
        model = Person_media_type
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonCreateSerializer(ModelSerializer):
    cpf = serializers.CharField(
        validators=[UniqueValidator(queryset=Person.objects.all()), CPFValidator()]
    )  
    class Meta:
        model = Person
        fields = ("name", "type", "cpf", "phone", "company")


class Person_mediaCreateSerializer(ModelSerializer):
    object_media = serializers.CharField(
        validators=[validate_image]
    )
    class Meta:
        model = Person_media
        fields = ('person', 'media_type', 'object_media')

class Person_mediaSerializer(ModelSerializer):
    class Meta:
        model = Person_media
        fields = ('person', 'media_type', 'object_media')