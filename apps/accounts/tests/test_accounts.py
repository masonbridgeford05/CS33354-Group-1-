from django.test import TestCase
from apps.accounts.views import UserController
from apps.accounts.models import User

class TestCreateUser(TestCase):
    
    def setUp(self):
        self.controller = UserController()
        self.controller.createUserAccount("thecowman", "cxc210050@utdallas.edu", "CowPassword123")
    
    def testCreatedUser(self):
        count = User.objects.count()
        print(f"Users in test DB: {count}")
        