from django.test import TestCase
from apps.accounts.models import User
from apps.accounts.views import UserController


class LoginTestCase(TestCase):

    def print_result(self, tc_name, inputs, success):
        
        # Print test case name, inputs, and final result
        
        print("\n" + "=" * 60)
        print(tc_name)
        print(f"Input -> {inputs}")
        print("Result ->", "Test Case Successful" if success else "Test Case Failed")
        print("=" * 60)

    def setUp(self):
        
        # Create controller instance and one valid user
        
        self.controller = UserController()
        
        User.createUserAccount("Newuser123", "johndoe@utdallas.edu", "Newpassword123")

        # test case 1

    def test_tc1_valid_valid(self):
        
        # Valid email and pass
        
        result = self.controller.loginUser("johndoe@utdallas.edu", "Newpassword123")

        self.print_result(
            "TC1 Login (Valid Email / Valid Password)",
            "email=johndoe@utdallas.edu, password=Newpassword123",
            result
        )

        self.assertTrue(result)

        # test case 2 

    def test_tc2_valid_invalid(self):
        
        # Valid email but invalid pass
        
        result = self.controller.loginUser("johndoe@utdallas.edu", "wrongpassword")

        self.print_result(
            "TC2 Login (Valid Email / Invalid Password)",
            "email=johndoe@utdallas.edu, password=wrongpassword",
            not result
        )

        self.assertFalse(result)

        # test case 3

    def test_tc3_invalid_valid(self):
        
        # Invalid email and valid pass
        
        result = self.controller.loginUser("invalid@utdallas.edu", "Newpassword123")

        self.print_result(
            "TC3 Login (Invalid Email / Valid Password)",
            "email=invalid@utdallas.edu, password=Newpassword123",
            not result
        )

        self.assertFalse(result)

        # test case 4

    def test_tc4_invalid_invalid(self):
        
        # Invalid email and pass
        
        result = self.controller.loginUser("invalid@utdallas.edu", "wrongpassword")

        self.print_result(
            "TC4 Login (Invalid Email / Invalid Password)",
            "email=invalid@utdallas.edu, password=wrongpassword",
            not result
        )

        self.assertFalse(result)

        # test case 5

    def test_tc5_exception_email(self):
        
        # empty email
        
        result = self.controller.loginUser("", "Newpassword123")

        self.print_result(
            "TC5 Login (Empty Email)",
            "email='', password=Newpassword123",
            not result
        )

        self.assertFalse(result)

        # test case 6

    def test_tc6_exception_password(self):
        
        # empty pass
        
        result = self.controller.loginUser("johndoe@utdallas.edu", "")

        self.print_result(
            "TC6 Login (Empty Password)",
            "email=johndoe@utdallas.edu, password=''",
            not result
        )

        self.assertFalse(result)
