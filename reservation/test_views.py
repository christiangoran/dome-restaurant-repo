from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Reservation
import datetime


"""
In this test file I will divide the tests into different classes
instead of having all tests in one class for learning purposes
"""

class BaseTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Mr McSchmoff',
            password='BuzzLightyearIsSexxi'
        )

        self.staff_user = User.objects.create_user(
            username='Ms Doubtfire',
            password='HelloDear',
            is_staff=True
        )

        self.table1 = Table.objects.create(table_number=1, capacity=4)
        self.table2 = Table.objects.create(table_number=2, capacity=4)

        Reservation.objects.create(
            user=self.user,
            table=self.table1,
            name='Spanky McSpankerson',
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=1,
            number_of_guests=2,
            customer_email='mcspank2003@hotmail.com'
        )


class TestHomeView(TestCase):

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Home')


class TestMenuView(TestCase):

    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertContains(response, 'Menu')


class TestIndexReservationView(BaseTest):

    def test_index_reservation_view(self):
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 302)

    def test_if_user_not_logged_in_redirect_to_login(self):
        response = self.client.get('/view/')
        # Django's LoginRequiredMixin seem to appends a ?next= parameter to the URL to 
        # keep track of where to send the user back after they have logged in. 
        # This is why you see the ?next=%2Fview%2F part here below
        
        # I also removed the response context from the test since
        # I kept getting a 301 instead of an expected 200
        self.assertRedirects(response, '/login?next=%2Fview%2F',fetch_redirect_response=False)

    def test_if_user_is_staff_return_all_reservations(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_staff_return_only_their_reservations(self):
        self.client.login(username='Mr McSchmoff', password='BuzzLightyearIsSexxi')
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 200)

    def test_search_by_email(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get('/view/', {'booking_email': 'mcspank2003@hotmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 1)
        self.assertEqual(response.context['reservations'][0].customer_email, 'mcspank2003@hotmail.com')
          
    def test_search_by_date(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get('/view/', {'booking_date': datetime.date.today() + datetime.timedelta(days=1)})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 1)
        self.assertEqual(response.context['reservations'][0].date, datetime.date.today() + datetime.timedelta(days=1))


class TestCreateReservationView(BaseTest):

    def test_create_reservation_view(self):
        self.client.login(username='Mr McSchmoff', password='BuzzLightyearIsSexxi')
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_reservation.html')

    def test_create_reservation(self):
        self.client.login(username='Mr McSchmoff', password='BuzzLightyearIsSexxi')
        response = self.client.post('/create/', {
            'table': self.table2,
            'name': 'Tree Hugger',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 1,
            'number_of_guests': 2,
            'customer_email': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 2)

