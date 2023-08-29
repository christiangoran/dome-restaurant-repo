from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Reservation
from .forms import ReservationForm
import datetime


class ReservationFormTestCase(TestCase):


    def setUp(self):
        # Create a user
        self.user = User.objects.create(username='TestyMcTesterson', password='IamCool123')

        # Create some Table instances
        # And we need to create 5 to match validation error code in forms.py
        self.table1 = Table.objects.create(table_number=1, capacity=4)
        self.table2 = Table.objects.create(table_number=2, capacity=2)
        self.table3 = Table.objects.create(table_number=3, capacity=2)
        self.table4 = Table.objects.create(table_number=4, capacity=2)
        self.table5 = Table.objects.create(table_number=5, capacity=2)

    
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


    def test_all_tables_reserved(self):

        # Creating 5 reservations first so that all tables are reserved
        Reservation.objects.create(
            user=self.user,
            table=self.table1,
            name='Spanky McSpankerson',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
        )

        Reservation.objects.create(
            user=self.user,
            table=self.table2,
            name='Eggbert McEggerson',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
        )

        Reservation.objects.create(
            user=self.user,
            table=self.table3,
            name='Rooney McRooneyson',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
        )

        Reservation.objects.create(
            user=self.user,
            table=self.table4,
            name='Coolio Bonkers',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
        )

        Reservation.objects.create(
            user=self.user,
            table=self.table5,
            name='Mr Last Table',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
        )

        # And now we try to create a new reservation
        form = ReservationForm({
            'name': 'Testy McTesterson',
            'customer_email': 'testy.mctesterson@cool.com',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 1,  # same as "12:00pm - 1:45pm" on website
            'notes': 'This is a test',
            'number_of_guests': 2,
        })   

        self.assertFalse(form.is_valid())  # The form should be invalid

        expected_error = 'Sorry we do not have a table available for that date and time'
        actual_error = str(form.errors['__all__'][0]) 
        self.assertEqual(expected_error, actual_error)


    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ['name', 'customer_email', 'date', 'time', 'notes', 'number_of_guests'])