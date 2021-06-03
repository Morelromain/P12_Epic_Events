from rest_framework import status
from rest_framework.test import APITestCase


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
