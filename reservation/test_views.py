from django.test import TestCase
from django.contrib.auth.models import User
from .models import Table, Reservation
import datetime
from django.urls import reverse


"""
In this test file I will divide the tests into different classes
instead of having all tests in one class for learning purposes
"""


class BaseTest(TestCase):
    """
    The purpose of this class is to reduce code duplication by 
    providing a common setup that can be inherited by multiple test classes.

    The class creates two users, one staff user and one non-staff user.
    It also creates two tables and one reservation.

    """

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
    """
    Tests the home view for correct status code, template, and content.

    """

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Home')


class TestMenuView(TestCase):
    """
    Tests the menu view for correct status code, template, and content.
    """
    def test_menu_view(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertContains(response, 'Menu')


class TestIndexReservationView(BaseTest):
    """
    Test the Index Reservation View.

    Tests goes over:
    - Basic view accessibility.
    - Redirection for unauthenticated users.
    - Staff user's ability to see all reservations.
    - Non-staff user's ability to see only their reservations.
    - Search functionality by email and date.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The view redirects unauthenticated users to the login page.
    - The view returns all reservations when the user is staff.

    """

    def test_index_reservation_view(self):
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 302)

    def test_if_user_not_logged_in_redirect_to_login(self):
        response = self.client.get('/view/')
        # Django's LoginRequiredMixin seem to appends a
        # ?next= parameter to the URL to
        # keep track of where to send the user back after they have logged in.
        # This is why you see the ?next=%2Fview%2F part here below

        # I also removed the response context from the test since
        # I kept getting a 301 instead of an expected 200
        self.assertRedirects(
            response, '/accounts/login?next=%2Fview%2F',
            fetch_redirect_response=False
        )

    def test_if_user_is_staff_return_all_reservations(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 200)

    def test_if_user_is_not_staff_return_only_their_reservations(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get('/view/')
        self.assertEqual(response.status_code, 200)

    def test_search_by_email(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get(
            '/view/', {'booking_email': 'mcspank2003@hotmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 1)
        self.assertEqual(
            response.context['reservations'][0].customer_email,
            'mcspank2003@hotmail.com'
        )

    def test_search_by_date(self):
        self.client.login(username='Ms Doubtfire', password='HelloDear')
        response = self.client.get(
            '/view/',
            {
                'booking_date':
                    datetime.date.today() + datetime.timedelta(days=1)
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['reservations']), 1)
        self.assertEqual(
            response.context['reservations'][0].date,
            datetime.date.today() + datetime.timedelta(days=1))


class TestCreateReservationView(BaseTest):
    """
    Test suite for the Create Reservation View.

    Tests goes over:
    - View accessibility and template usage.
    - Reservation creation functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A new reservation can be successfully created.
    """


    def test_create_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_reservation.html')

    def test_create_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
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


class TestUpdateReservationView(BaseTest):
    """
    Test for the update reservation view.

    Tests goes over:
    - View accessibility and template usage.
    - Reservation update functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A reservation can be successfully updated.

    """

    def test_update_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get('/update/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_reservation.html')

    def test_update_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.post('/update/1/', {
            'table': self.table1,
            'name': 'Spanky McSpankerson',
            'date': datetime.date.today() + datetime.timedelta(days=1),
            'time': 2,  # Update time from 1 to 2
            'number_of_guests': 4,  # Update number_of_guests from 2 to 4
            'customer_email': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.get(id=1).time, 2)
        self.assertEqual(Reservation.objects.get(id=1).number_of_guests, 4)


class TestDeleteReservationView(BaseTest):
    """
    Test for the delete reservation view.
    
    Tests goes over:
    - View accessibility and template usage.
    - Reservation deletion functionality.

    The tests makes sure that that:
    - The view is accessible when the user is logged in.
    - The correct template is used for the view.
    - A reservation can be successfully deleted.
    
    """

    def setUp(self):
        super().setUp()
        self.reservation = Reservation.objects.create(
            user=self.user,
            table=self.table1,
            name='Delete Me',
            date=datetime.date.today() + datetime.timedelta(days=3),
            time=2,
            number_of_guests=3,
        )
        self.delete_url = reverse(
            'reservation:delete', args=[self.reservation.id])

    def test_delete_reservation_view(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_reservation.html')

    def test_authorized_user_delete_reservation(self):
        self.client.login(username='Mr McSchmoff',
                          password='BuzzLightyearIsSexxi')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse(
            'reservation:view'), fetch_redirect_response=False)
        # Verify the reservation was actually deleted
        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(id=self.reservation.id)
