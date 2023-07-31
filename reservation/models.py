from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return str(self.table_number)
