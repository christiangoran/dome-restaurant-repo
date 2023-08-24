from django.test import TestCase
from .forms import ReservationForm, SearchReservationForm


class TestReservationForm(TestCase):
    
    def test_name_is_required(self):
        form = ReservationForm({
            'name': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_date_is_required(self):
        form = ReservationForm({
            'date': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_time_is_required(self):
        form = ReservationForm({
            'time': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')
