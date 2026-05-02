from django.test import TestCase, Client
from apps.accounts.models import User
from django.urls import reverse
from django.contrib.auth.hashers import make_password

class AccountCreationTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Use custom field names and .create()
        User.objects.create(
            userName='Existinguser',
            userEmail='existing@utdallas.edu',
            userPassword=make_password('Newpassword123')
        )

    def test_tc1_all_valid(self):
        response = self.client.post(reverse('register'), {
            'userName': 'Newuser123',
            'userEmail': 'johndoe@utdallas.edu',
            'userPassword': 'Newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(userName='Newuser123').exists())

    def test_tc2_confirm_password_invalid(self):
        response = self.client.post(reverse('register'), {
            'userName': 'Newuser123',
            'userEmail': 'johndoe@utdallas.edu',
            'userPassword': 'Newpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(userName='Newuser123').exists())

    def test_tc3_username_invalid(self):
        response = self.client.post(reverse('register'), {
            'userName': 'Existinguser',
            'userEmail': 'johndoe@utdallas.edu',
            'userPassword': 'Newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(userName='Existinguser').count(), 1)

    def test_tc5_password_invalid(self):
        response = self.client.post(reverse('register'), {
            'userName': 'Newuser123',
            'userEmail': 'johndoe@utdallas.edu',
            'userPassword': 'weak'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(userName='Newuser123').exists())