from django.db import models

from .owner import Owner

# Create your models here.
class Dog(models.Model):
    """Defines fields and methods of the Book resource model"""
    # define our fields here
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='dog_owner'
    )

    # https://docs.djangoproject.com/en/3.0/ref/models/instances/#str
    # here we'll set up our __str__ method and our as_dict method
    def __str__(self):
        """Returns a string depiction of the model"""
        return self.title
    
    # This will be used before we have a serializer in the 'show' method request
    def as_dict(self):
        """returns dictionary version of the Book instance"""
        return {
            'id': self.id,
            'name': self.name,
            'owner': self.owner
        }