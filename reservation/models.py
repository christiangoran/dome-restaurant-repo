from django.db import models
from django.contrib.auth.models import User

CAPACITY = ((2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"))
BOOKING_TIME = ((1, "12:00pm - 1:45pm"), (2, "2:00pm - 3:45pm"),
                (3, "4:00pm - 5:45pm"), (4, "6:00pm - 7:45pm"),
                (5, "8:00pm - 9:45pm"))


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=150, blank=True, null=True)
    date = models.DateField()
    time = models.IntegerField(choices=BOOKING_TIME, default=1)
    notes = models.TextField(null=True, blank=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY, default=2)

    def __str__(self):
        return str(self.table_number)
