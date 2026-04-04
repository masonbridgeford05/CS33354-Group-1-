from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LoginTestCase(TestCase):

    def setUp(self):
        # Create a test client that simulates browser requests
        self.client = Client()

        # Create one valid user for all login test cases
        User.objects.create_user(
            username="Newuser123",
            password="Newpassword123",
            email="johndoe@gmail.com"
        )

    def print_result(self, tc_name, inputs, success):
        
        # Print the test case name, input values, and result
        
        print("\n" + "=" * 60)
        
        print(tc_name)
        
        print(f"Input -> {inputs}")
        
        print("Result ->", "Test Case Successful" if success else "Test Case Failed")
        
        print("=" * 60)

    def test_tc1_valid_username_valid_password(self):
        
        # Test case 1 
        
        # valid user and pass
        
        # succesful log in 

        username = "Newuser123"
        
        password = "Newpassword123"

        response = self.client.post(reverse('login'),
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 302)

        self.print_result(
            "TC1 Login (Valid Username / Valid Password)",
            f"username={username}, password={password}",
            success
        )

        self.assertEqual(response.status_code, 302)
        
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_tc2_valid_username_invalid_password(self):
       
        # Test case 2
       
        # Valid user but invalid pass
        
        # failed log
        
        username = "Newuser123"
        password = "wrongpassword"

        response = self.client.post(reverse('login'),
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC2 Login (Valid Username / Invalid Password)",
            f"username={username}, password={password}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc3_invalid_username_valid_password(self):
       
        # Test case 3
       
        # Invalid user but valid pass
       
        # failed log in

        username = "Invaliduser"
        password = "Newpassword123"

        response = self.client.post(reverse('login'),
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC3 Login (Invalid Username / Valid Password)",
            f"username={username}, password={password}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc4_invalid_username_invalid_password(self):
       
        # Test case 4
       
        # Invalid user and pass
       
        # failed log in

        username = "Invaliduser"
        password = "wrongpassword"

        response = self.client.post(reverse('login'),
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC4 Login (Invalid Username / Invalid Password)",
            f"username={username}, password={password}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc5_exception_username(self):
        # Test case 5
       
        # no user name but valid pass
       
        # failed log in

        username = ""
        password = "Newpassword123"

        response = self.client.post(reverse('login'), 
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC5 Login (Empty Username / Valid Password)",
            f"username='{username}', password={password}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc6_exception_password(self):
        # Test case 6
        
        # Valid user but no pass
        
        # failed log in

        username = "Newuser123"
        password = ""

        response = self.client.post(reverse('login'),
        {
            'username': username,
            'password': password
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC6 Login (Valid Username / Empty Password)",
            f"username={username}, password='{password}'",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse('_auth_user_id' in self.client.session)
