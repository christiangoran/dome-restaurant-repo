from django.db import models
from django.contrib.auth.models import User

# Provides a list of choices when creating tables in the admin panel.
CAPACITY = ((2, "2"), (4, "4"), (6, "6"), (8, "8"))
# Provides a list of times when creating reservations.
BOOKING_TIME = ((1, "12:00pm - 1:45pm"), (2, "2:00pm - 3:45pm"),
                (3, "4:00pm - 5:45pm"), (4, "6:00pm - 7:45pm"),
                (5, "8:00pm - 9:45pm"))


class Reservation(models.Model):
    """
    This represents a reservation made by a user.
    It's linked to the User who made the reservation and the Table that's reserved.

    Fields:
    user (ForeignKey): The user who made the reservation.
    name (CharField): The name of the person who made the reservation.
    customer_email (EmailField): The email address of the customer.
    date (DateField): The date of the reservation.
    time (IntegerField): The time of the reservation.
    notes (TextField): Additional notes or special requests.
    table (ForeignKey): The table that's reserved.

    Methods:
    __str__: Returns the name of the person who made the reservation.
    
    """
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
    """
    This represents a table in the restaurant.

    Fields:
    table_number (IntegerField): The number of the table.
    capacity (IntegerField): The capacity of the table.

    Methods:
    __str__: Returns the number of the table.

    """
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY, default=2)

    def __str__(self):
        return str(self.table_number)
