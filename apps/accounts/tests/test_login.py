from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTestCase(TestCase):

    def setUp(self):
      
        self.client = Client()

        # Creating a valid user for login testing
        User.objects.create_user(
            username="Newuser123",
            
            password="Newpassword123",
            
            email="johndoe@gmail.com"
        )

    def test_tc1_valid_username_valid_password(self):
        # Test case 1
        
        # Valid username and password
        
        # succesful log in 

        response = self.client.post(reverse('login'), 
        {
            'username': 'Newuser123',
            'password': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 302)
        
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_tc2_valid_username_invalid_password(self):
        
        # Test case 2
        
        # invalid pass and valid user
        
        #log in failed 

        response = self.client.post(reverse('login'),
        {
            'username': 'Newuser123',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc3_invalid_username_valid_password(self):
        
        # Test case 3
        
        # Invalid user and valid pass
        
        # log in failed 

        response = self.client.post(reverse('login'),
        {
            'username': 'Invaliduser',
            'password': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc4_invalid_username_invalid_password(self):
        
        # Test case 4
        
        # Invalid user and pass
        
        # log in failed

        response = self.client.post(reverse('login'),
        {
            'username': 'Invaliduser',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc5_exception_username(self):
       
        # Test case test 5
        
        # valid pass and empty user
        
        # Log in failed

        response = self.client.post(reverse('login'),
        {
            'username': '',
            'password': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc6_exception_password(self):
       
        # Test case 6
        
        # Valid user and empty pass
        
        # log in failed

        response = self.client.post(reverse('login'),
        {
            'username': 'Newuser123',
            'password': ''
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)
