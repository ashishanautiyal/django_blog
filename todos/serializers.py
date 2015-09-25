from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todos


class PostSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200) #Like a VARCHAR field
    description = serializers.CharField(max_length=200) #Like a TEXT field
    created = serializers.DateTimeField() #Like a DATETIME field

    class Meta:
        model = Todos
        fields = ('name', 'description', 'created' , 'pk')