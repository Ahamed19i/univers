

from rest_framework import serializers
from .models import Example, EmploiDuTemps

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'


# Serializers pour l'emploi du temps 

class EmploiDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiDuTemps
        fields = '__all__'