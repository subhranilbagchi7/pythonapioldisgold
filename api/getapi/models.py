from django.db import models

# Create your models here.
class Signup ( models.Model ):
    passangers_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=10)
    email_id = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return ()

