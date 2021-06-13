from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User
from django.contrib.auth.models import Group


class UserViewsTests(APITestCase):

    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_mdp'
        self.data = {
            'username': self.username,
            'password': self.password,
        }
        self.url_get_token = reverse('token_obtain_pair')

    def test_basic_index_acces(self):
        """
        basic acces to API root
        """

        result = self.client.get("/")
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_bad_login_fail_recovers_token(self):
        """
        login to API with a wrong user
        """

        User.objects.create_user(username='bad_user_name', password='test_mdp')
        response = self.client.post(
            self.url_get_token, self.data, format='json')
        assert response.status_code in [401]

    def test_login_with_bad_permission(self):
        """
        login to API with a wrong groups user
        """

        User.objects.create_user(
            username='test_user', password='test_mdp')
        response = self.client.post(
            self.url_get_token, self.data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.get("/clients/", data={'format': 'json'})
        assert response.status_code in [403]

    def test_login_and_acces_with_token_GOOD(self):
        """
        succès login to API and acces on endpoint
        """

        group = Group.objects.create(name='Sales')
        user = User.objects.create_user(
            username='test_user', password='test_mdp')
        user.groups.add(group)
        response = self.client.post(
            self.url_get_token, self.data, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['access']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer {0}'.format(token))
        response = self.client.get("/users/", data={'format': 'json'})
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.content)
