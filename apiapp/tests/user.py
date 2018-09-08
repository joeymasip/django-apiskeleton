from rest_framework.test import APIClient
from rest_framework import status
from apiapp.tests.fixture import FixtureTestCase


class UserTestCase(FixtureTestCase):

    def test_api_admin_get_users_unauthorized_i_am_anon(self):
        client = APIClient()
        response = client.get('/api/admin/user/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_api_admin_get_users_authorized_i_am_admin(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_admin))
        response = client.get('/api/admin/user/')
        assert response.status_code == status.HTTP_200_OK

    def test_api_admin_get_user_authorized_i_am_admin(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_admin))
        response = client.get('/api/admin/user/1/')
        assert response.status_code == status.HTTP_200_OK
        response = client.get('/api/admin/user/2/')
        assert response.status_code == status.HTTP_200_OK
        response = client.get('/api/admin/user/3/')
        assert response.status_code == status.HTTP_200_OK

    def test_api_admin_get_user_unauthorized_i_am_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_normal_1))
        response = client.get('/api/admin/user/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_normal_1))
        response = client.get('/api/admin/user/1/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_normal_1))
        response = client.get('/api/admin/user/2/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_api_get_user_authorized_i_am_admin(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_admin))
        response = client.get('/api/user/1/')
        assert response.status_code == status.HTTP_200_OK
        response = client.get('/api/user/2/')
        assert response.status_code == status.HTTP_200_OK
        response = client.get('/api/user/3/')
        assert response.status_code == status.HTTP_200_OK

    def test_api_get_user_authorized_i_am_user(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token(self.user_normal_1))
        response = client.get('/api/user/1/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        response = client.get('/api/user/2/')
        assert response.status_code == status.HTTP_200_OK
        response = client.get('/api/user/3/')
        assert response.status_code == status.HTTP_403_FORBIDDEN
