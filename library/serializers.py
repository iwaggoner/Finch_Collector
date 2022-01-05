# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models import Dog

# create our serializer class

class DogSerializer(serializers.ModelSerializer):
    # define a meta class
    class Meta:
        # specify the model from which to define the fields
        model = Dog
        # define the fields to be returned
        fields = '__all__'