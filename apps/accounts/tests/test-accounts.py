from django.test import TestCase
from apps.accounts.models import createUserAccount

class TestCreateUser(TestCase):
    def Setup():
        createUserAccount("thecowman", "cxc210050@utdallas.edu", "CowPassword123")
        