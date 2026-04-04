from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class LogoutTestCase(TestCase):

    def setUp(self):
        
        # Create a test client
        
        self.client = Client()

        # Create a user for logout testing
       
        User.objects.create_user(
            username="logoutuser",
            password="Logout123"
        )

    def print_result(self, tc_name, inputs, success):
        
        # Print the test case name, input values, and result
        
        print("\n" + "=" * 60)
        print(tc_name)
        print(f"Input -> {inputs}")
        print("Result ->", "Test Case Successful" if success else "Test Case Failed")
        print("=" * 60)

    def test_tc1_valid_session(self):
        
        # Test case 1
        
        # Valid session
        
        # succesful logout

        self.client.login(username="logoutuser", password="Logout123")

        response = self.client.get(reverse('logout'))

        success = (response.status_code == 302)

        self.print_result(
            "TC1 Logout (Valid Session)",
            "user logged in before logout request",
            success
        )

        self.assertEqual(response.status_code, 302)
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc2_invalid_session(self):
        
        # Test case 2
        
        # no user logged in
        
        # failed test case

        response = self.client.get(reverse('logout'))

        success = response.status_code in [200, 302]

        self.print_result(
            "TC2 Logout (No Active Session)",
            "no user logged in",
            success
        )

        self.assertIn(response.status_code, [200, 302])
        
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_tc3_expired_session(self):
        # Test case 3
        
        # expired session
        
        # failed log out

        self.client.login(username="logoutuser", password="Logout123")

        # Clear session to simulate expiration
        
        self.client.session.flush()

        response = self.client.get(reverse('logout'))

        success = response.status_code in [200, 302]

        self.print_result(
            "TC3 Logout (Expired/Cleared Session)",
            "session cleared before logout request",
            success
        )

        self.assertIn(response.status_code, [200, 302])
        
        self.assertFalse('_auth_user_id' in self.client.session)
