from .models import Person
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name', 'last_name', 'email', 'date_of_birth', 'date_added']