from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Alimento, Plato


class AlimentosResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'

class PlatosResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

    