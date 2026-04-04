from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AccountCreationTestCase(TestCase):

    def setUp(self):
        
        # Create a test client
        
        self.client = Client()

        # Create an existing user for duplicate user testing
        
        User.objects.create_user(
            username="Existinguser",
            email="existing@gmail.com",
            password="Newpassword123"
        )

    def print_result(self, tc_name, inputs, success):
        
        # Print the test case name, input values, and result
        
        print("\n" + "=" * 60)
        print(tc_name)
        print(f"Input -> {inputs}")
        print("Result ->", "Test Case Successful" if success else "Test Case Failed")
        print("=" * 60)

    def test_tc1_all_valid(self):
        
        # Test case 1 
        
        # all valid inputs
        
        # succesful account creation

        username = "Newuser123"
        email = "johndoe@gmail.com"
        password1 = "Newpassword123"
        password2 = "Newpassword123"

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 302)

        self.print_result(
            "TC1 Create Account (All Valid)",
            f"username={username}, email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 302)
        
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_tc2_confirm_password_invalid(self):
        
        # Test case 2
        
        # all valid except for confirm password
        
        # failed account creation

        username = "Newuser123"
        email = "johndoe@gmail.com"
        password1 = "Newpassword123"
        password2 = "Newpassword123567"

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC2 Create Account (Password Mismatch)",
            f"username={username}, email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username=username).exists())

    def test_tc3_username_invalid(self):
        
        # Test case 3
        
        # Invalid user 
        
        # failed account creation

        username = "Existinguser"
        email = "johndoe@gmail.com"
        password1 = "Newpassword123"
        password2 = "Newpassword123"

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC3 Create Account (Duplicate Username)",
            f"username={username}, email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(User.objects.filter(username=username).count(), 1)

    def test_tc4_email_invalid(self):
        
        # Test case 4
        
        # all valid except email 
        
        # failed account creation

        username = "Newuser123"
        email = "invalid"
        password1 = "Newpassword123"
        password2 = "Newpassword123"

        response = self.client.post(reverse('register'), 
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC4 Create Account (Invalid Email)",
            f"username={username}, email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username=username).exists())

    def test_tc5_password_invalid(self):
        
        # Test case 5
        
        # all valid except passwords
        
        # failed account creation 

        username = "Newuser123"
        email = "johndoe@gmail.com"
        password1 = "weak"
        password2 = "weak"

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC5 Create Account (Weak Password)",
            f"username={username}, email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username=username).exists())

    def test_tc6_exception_username(self):
       
        # Test case 6
        
        # all valid but no username
        
        # failed account creation

        username = ""
        email = "johndoe@gmail.com"
        password1 = "Newpassword123"
        password2 = "Newpassword123"

        response = self.client.post(reverse('register'), 
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC6 Create Account (Empty Username)",
            f"username='{username}', email={email}, password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)

    def test_tc7_exception_email(self):
        
        # Test case 7
        
        # all valid but no email
        
        # failed account creation

        username = "Newuser123"
        email = ""
        password1 = "Newpassword123"
        password2 = "Newpassword123"

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC7 Create Account (Empty Email)",
            f"username={username}, email='{email}', password1={password1}, password2={password2}",
            success
        )

        self.assertEqual(response.status_code, 200)

    def test_tc8_exception_password(self):
        
        # Test case 8 
        
        # all valid but no passwords
        
        # failed account creation

        username = "Newuser123"
        email = "johndoe@gmail.com"
        password1 = ""
        password2 = ""

        response = self.client.post(reverse('register'),
        {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        success = (response.status_code == 200)

        self.print_result(
            "TC8 Create Account (Empty Password Fields)",
            f"username={username}, email={email}, password1='{password1}', password2='{password2}'",
            success
        )

        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(User.objects.filter(username=username).exists())
