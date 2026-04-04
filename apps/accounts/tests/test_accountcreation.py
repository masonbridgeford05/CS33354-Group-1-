from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AccountCreationTestCase(TestCase):

    def setUp(self):
        # Create a test client
      
        self.client = Client()

        # Create an existing user for duplicate username testing
      
        User.objects.create_user(
            username='Existinguser',
            email='existing@gmail.com',
            password='Newpassword123'
        )

    def test_tc1_all_valid(self):
        
        # Test case 1
        
        # all valid inputs
        
        # expected outcome: account created

        response = self.client.post(reverse('register'),
        {
            'username': 'Newuser123',
            'email': 'johndoe@gmail.com',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='Newuser123').exists())

    def test_tc2_confirm_password_invalid(self):
        
        # Test case 2 
        
        # password and confirmation password dont't match
        
        # Expected outcome: account not created

        response = self.client.post(reverse('register'), 
        {
            'username': 'Newuser123',
            'email': 'johndoe@gmail.com',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123567'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username='Newuser123').exists())

    def test_tc3_username_invalid(self):
        
        # Test case 3 
        
        # existing user
        
        # Expected outcome: account creation fail

        response = self.client.post(reverse('register'),
        {
            'username': 'Existinguser',
            'email': 'johndoe@gmail.com',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(User.objects.filter(username='Existinguser').count(), 1)

    def test_tc4_email_invalid(self):
        
        # Test case 4 
        
        # email formatting is invalid
        
        # Expected outcome: accouint creation failed

        response = self.client.post(reverse('register'),
        {
            'username': 'Newuser123',
            'email': 'invalid',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username='Newuser123').exists())

    def test_tc5_password_invalid(self):
        
        # Test case 5
        
        # password is either invalid or weak
        
        # Expected outcome: account creation failed

        response = self.client.post(reverse('register'), 
        {
            'username': 'Newuser123',
            'email': 'johndoe@gmail.com',
            'password1': 'weak',
            'password2': 'weak'
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username='Newuser123').exists())

    def test_tc6_exception_username(self):
        
        # Test case 6 
        
        # null user
        
        # Expected outcome: account creation failed

        response = self.client.post(reverse('register'),
        {
            'username': '',
            'email': 'johndoe@gmail.com',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)

    def test_tc7_exception_email(self):
        
        # Test case 7 
        
        # null email
        
        # Expected outcome: account creation failed

        response = self.client.post(reverse('register'), {
            'username': 'Newuser123',
            'email': '',
            'password1': 'Newpassword123',
            'password2': 'Newpassword123'
        })

        self.assertEqual(response.status_code, 200)

    def test_tc8_exception_password(self):
        
        # Test case 8 
        
        # null passwords
        
        # Expected outcome: account creation failed

        response = self.client.post(reverse('register'),
        {
            'username': 'Newuser123',
            'email': 'johndoe@gmail.com',
            'password1': '',
            'password2': ''
        })

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username='Newuser123').exists())
