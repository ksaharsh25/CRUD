from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('Name','EmailId','Password','id')


       