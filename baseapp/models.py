from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Dog(models.Model):
    dogName=models.CharField(max_length=20)
    dogAge=models.IntegerField()
    gaurdianContact=models.CharField(max_length=15,validators=[MinLengthValidator(15)])
    healthDescription=models.TextField()
    dogPicture=models.ImageField(upload_to='dogImages/',null=True)

    def __str__(self):
        return self.dogName


class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()

