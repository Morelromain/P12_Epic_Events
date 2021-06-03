from user.models import User

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

class CRMTestCase(APITestCase):

    def test_index(self):

        result = self.client.get("/")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
    
    def test_acces_login(self):

        result = self.client.get("/api-auth/login/")
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_log(self):

        data = {"username": "user10", "password": "86Ibra86aaa"}
        result = self.client.post("/api-auth/login/", data)
        assert result.status_code in [200]

    def test_acces_logout(self):

        result = self.client.get("/api-auth/logout/")
        assert result.status_code in [200]


    def test_acces_client(self):
        """data = User.objects.get(username="user10")"""
        self.client.force_authenticate("/clients/", user="user")
        result = self.client.get("/clients/", user="user")
        assert result.status_code in [200]


"""from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.test import TestCase

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        
    def test_login(self):
        # login
        response = self.client.post('/api-auth/login/', **self.credentials)      
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_active)"""
