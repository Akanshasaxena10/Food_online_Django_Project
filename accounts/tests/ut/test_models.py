from django.test import TestCase
from accounts import models
from accounts.models import User
from accounts.models import UserProfile

class TestUserProfile(TestCase):
    def setUp(self) -> None:###create a user 
     self.user = User.objects.create_user(first_name='tomtom',last_name='youngtom',username='tom',email='tom@gmail.com')
     
     ###check the user profile for the created user 
    def test_user_creation(self):
         user_profile = UserProfile.objects.filter(user=self.user)
         self.assertIsNotNone(user_profile) 
         