from django.test import TestCase
from apps.accounts.models import User
from apps.accounts.views import UserController


class CreateAccountTestCase(TestCase):

    def setUp(self):
        
        # Create controller instance
        
        self.controller = UserController()

    def print_result(self, tc_name, inputs, expected, actual):
        
        # Print expected vs actual
        
        print("\n" + "=" * 60)
        print(tc_name)
        print(f"Input -> {inputs}")
        print(f"Expected -> {expected}")
        print(f"Actual -> {actual}")
        print("Result ->", "PASS" if expected == actual else "FAIL")
        print("=" * 60)

    
    # Test case 1:
    
    # All valid inputs
    
    def test_tc1_valid_all(self):
        user = self.controller.createUserAccount(
            "Newuser123",
            "johndoe@utdallas.edu",
            "Newpassword123"
        )

        expected = True
        
        actual = (user is not None)

        self.print_result("TC1 Create Account (Valid/Valid/Valid)",
                          "username=Newuser123, email=johndoe@utdallas.edu, password=Newpassword123",
                          expected, actual)

        self.assertTrue(actual)

    # Test case 2 
    
    # Invalid email
    
    def test_tc2_invalid_email(self):
        user = self.controller.createUserAccount(
            "Newuser123",
            "johndoe@gmail.com",
            "Newpassword123"
        )

        expected = False
        
        actual = (user is not None)

        self.print_result("TC2 Create Account (Valid/Invalid/Valid)",
                          "username=Newuser123, email=johndoe@gmail.com, password=Newpassword123",
                          expected, actual)

        self.assertFalse(actual)

    # Test case 3 
    
    # invalid password

    def test_tc3_invalid_password(self):
        user = self.controller.createUserAccount(
            "Newuser123",
            "johndoe@utdallas.edu",
            "short"
        )

        expected = False
        
        actual = (user is not None)

        self.print_result("TC3 Create Account (Valid/Valid/Invalid)",
                          "username=Newuser123, email=johndoe@utdallas.edu, password=short",
                          expected, actual)

        self.assertFalse(actual)

    
    # Test case 4 
    
    # no username
    
    def test_tc4_empty_username(self):
        user = self.controller.createUserAccount(
            "",
            "johndoe@utdallas.edu",
            "Newpassword123"
        )

        expected = True
        
        actual = (user is not None)

        self.print_result("TC4 Create Account (Empty Username)",
                          "username='', email=johndoe@utdallas.edu, password=Newpassword123",
                          expected, actual)

        self.assertTrue(actual)

    
    # Test case 5 
    
    # no email
    
    def test_tc5_empty_email(self):
        user = self.controller.createUserAccount(
            "Newuser123",
            "",
            "Newpassword123"
        )

        expected = False
        
        actual = (user is not None)

        self.print_result("TC5 Create Account (Empty Email)",
                          "username=Newuser123, email='', password=Newpassword123",
                          expected, actual)

        self.assertFalse(actual)

    # Test case 6
    
    # no password
    
    def test_tc6_empty_password(self):
        user = self.controller.createUserAccount(
            "Newuser123",
            "johndoe@utdallas.edu",
            ""
        )

        expected = False
        
        actual = (user is not None)

        self.print_result("TC6 Create Account (Empty Password)",
                          "username=Newuser123, email=johndoe@utdallas.edu, password=''",
                          expected, actual)

        self.assertFalse(actual)
