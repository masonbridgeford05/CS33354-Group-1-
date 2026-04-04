from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LogoutTestCase(TestCase):

    def setUp(self):
        # Create a test client
        
        self.client = Client()

        # Create a user for logout testing
        
        User.objects.create_user(
            username='logoutuser',
            password='Logout123'
        )

    def test_tc1_valid_session(self):
        
        # Test case 1 
        
        # User is logged in before logout
        
        # successful log out

        self.client.login(username='logoutuser', password='Logout123')

        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc2_invalid_session(self):
        
        # Test case 2 
        
        # session isnt active
        
        # request is handled

        response = self.client.get(reverse('logout'))

        self.assertIn(response.status_code, [200, 302])
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc3_expired_session(self):
        
        # Test case 3 
        
        # Simulate expired session by clearing it first
        
        # request handled

        self.client.login(username='logoutuser', password='Logout123')
        
        self.client.session.flush()

        response = self.client.get(reverse('logout'))

        self.assertIn(response.status_code, [200, 302])
        
        self.assertFalse('_auth_user_id' in self.client.session)
