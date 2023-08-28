from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Reservation, BOOKING_TIME
from .forms import ReservationForm
import datetime

class ReservationFormTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create(username='testuser', password='123456790')

        # Create some Table instances
        self.table1 = Table.objects.create(table_number=1, capacity=4)
        self.table2 = Table.objects.create(table_number=2, capacity=2)
    
    def test_valid_data(self):
        form = ReservationForm({
            'name': 'Testy McTesterson',
            'customer_email': 'testy.mctesterson@cool.com',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 1,  # same as "12:00pm - 1:45pm" on website
            'notes': 'This is a test',
            'number_of_guests': 2,
        })
        self.assertTrue(form.is_valid())

