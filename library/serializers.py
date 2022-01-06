# import serializers from the django rest framework
from rest_framework import serializers

# import our model
from .models.dog import Dog
from .models.owner import Owner

# create our serializer class

class DogSerializer(serializers.ModelSerializer):
    # define a meta class
    class Meta:
        # specify the model from which to define the fields
        model = Dog
        # define the fields to be returned
        fields = '__all__'

class DogReadSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Dog
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    # define a meta class
    dogs_owned = DogSerializer(many=True, read_only=True)
    class Meta:
        # specify the model from which to define the fields
        model = Owner
        # define the fields to be returned
        fields = '__all__' 