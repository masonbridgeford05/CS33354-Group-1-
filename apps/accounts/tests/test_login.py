from django.test import TestCase, Client
from apps.accounts.models import User 
from django.urls import reverse
from django.contrib.auth.hashers import make_password

class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Create a user in the custom User table
        User.objects.create(
            userName="Newuser123",
            userEmail="johndoe@utdallas.edu",
            userPassword=make_password("Newpassword123")
        )

    def test_tc1_valid_username_valid_password(self):
        response = self.client.post(reverse('login'), {
            'userName': 'Newuser123',
            'userPassword': 'Newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        # Verify custom session key is set
        self.assertIn('user_id', self.client.session)

    def test_tc2_valid_username_invalid_password(self):
        response = self.client.post(reverse('login'), {
            'userName': 'Newuser123',
            'userPassword': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user_id', self.client.session)

    def test_tc3_invalid_username_valid_password(self):
        response = self.client.post(reverse('login'), {
            'userName': 'Invaliduser',
            'userPassword': 'Newpassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user_id', self.client.session)