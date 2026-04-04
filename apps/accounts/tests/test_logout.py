from django.test import TestCase
from apps.accounts.views import UserController


class FakeSession:
    
    # fake session object with a flush method for testing
    
    def __init__(self):
        self.flushed = False

    def flush(self):
        self.flushed = True


class FakeRequest:
    
    # Fake request object that contains a session attribute
    
    def __init__(self):
        self.session = FakeSession()


class LogoutTestCase(TestCase):

    def print_result(self, tc_name, inputs, success):
        
        # Print test case name, inputs, and final result
        
        print("\n" + "=" * 60)
        
        print(tc_name)
        
        print(f"Input -> {inputs}")
        
        print("Result ->", "Test Case Successful" if success else "Test Case Failed")
        
        print("=" * 60)

    def setUp(self):
        
        # Create controller instance
        
        self.controller = UserController()

        # test case 1

    def test_tc1_valid_session(self):
        
        # Valid session
        
        request = FakeRequest()
        
        result = self.controller.logoutUser(request)

        success = result and request.session.flushed

        self.print_result(
            "TC1 Logout (Valid Session)",
            "request has session attribute",
            success
        )

        self.assertTrue(result)
        
        self.assertTrue(request.session.flushed)

        # test case 2

    def test_tc2_invalid_session_object(self):
        
        # no session
        
        class NoSessionRequest:
            pass

        request = NoSessionRequest()
        
        result = self.controller.logoutUser(request)

        success = result

        self.print_result(
            "TC2 Logout (No Session Attribute)",
            "request has no session attribute",
            success
        )

        self.assertTrue(result)

        # test case 3

    def test_tc3_exception_session_none(self):
        
        # no session
        
        class NoneSessionRequest:
            session = None

        request = NoneSessionRequest()

        try:
            result = self.controller.logoutUser(request)
            success = False
        except:
            success = True

        self.print_result(
            "TC3 Logout (Session Is None)",
            "request.session=None",
            success
        )

        self.assertTrue(success)
