from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table
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


    def test_past_date(self):
        form = ReservationForm({
            'name': 'Testy McTesterson',
            'customer_email': 'testy.mctesterson@cool.com',
            'date': datetime.date.today() - datetime.timedelta(days=1),
            'time': 1,  # same as "12:00pm - 1:45pm" on website
            'notes': 'This is a test',
            'number_of_guests': 2,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'__all__': ['Sorry you have to book a future date']})


    def test_invalid_number_of_guests(self):
        form = ReservationForm({
            'name': 'Testy McTesterson',
            'customer_email': 'testy.mctesterson@cool.com',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 1,  # same as "12:00pm - 1:45pm" on website
            'notes': 'This is a test',
            'number_of_guests': 20,
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'__all__': ['Sorry we do not have a table with that capacity available']})