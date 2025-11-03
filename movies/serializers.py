from rest_framework import serializers
from .models import Movie

#Creamos serializer que le indique que queremos todos los campos de Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= '__all__'