from rest_framework import status
from rest_framework.reverse import reverse_lazy

from apps.core.tests import UserAPITestCase, LoggedUserAPITestCase


class AuthAPITest(UserAPITestCase):
    token_obtain_pair_view = 'token-obtain-pair'
    token_verify_view = 'token-verify'
    token_refresh_view = 'token-refresh'

    def obtain_token(self, username, password):
        url = reverse_lazy(self.token_obtain_pair_view)
        data = {
            "username": username,
            "password": password
        }
        return self.client.post(url, data, format='json')

    def verify_token(self, token):
        url = reverse_lazy(self.token_verify_view)
        data = {
            "token": token
        }
        return self.client.post(url, data, format='json')

    def refresh_token(self, refresh):
        url = reverse_lazy(self.token_refresh_view)
        data = {
            "refresh": refresh
        }
        return self.client.post(url, data, format='json')

    def test_obtain_token_with_valid_credentials(self):
        response = self.obtain_token(self.current_user.username, self.current_user_password)
        assert response.status_code == status.HTTP_200_OK
        assert 'refresh' in response.data
        assert 'access' in response.data
        return response

    def test_obtain_token_with_fake_credentials(self):
        response = self.obtain_token('fake', 'fake')  # print(response.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'detail' in response.data

    def test_refresh_token_with_valid_token(self):
        response_token = self.obtain_token(self.current_user.username, self.current_user_password)
        assert response_token.status_code == status.HTTP_200_OK
        response = self.refresh_token(response_token.data['refresh'])
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data

    def test_refresh_token_with_fake_token(self):
        response = self.refresh_token('fake refresh token')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'detail' in response.data
        assert 'code' in response.data
        assert response.data['code'] == 'token_not_valid'

    def test_verify_token_with_valid_token(self):
        response_token = self.obtain_token(self.current_user.username, self.current_user_password)
        assert response_token.status_code == status.HTTP_200_OK
        response = self.verify_token(response_token.data['access'])
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0

    def test_verify_token_with_fake_token(self):
        response = self.verify_token('fake access token')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert 'detail' in response.data
        assert 'code' in response.data
        assert response.data['code'] == 'token_not_valid'


class UserAPITests(LoggedUserAPITestCase):

    def get_users(self, **kwargs):
        url = reverse_lazy('user-list')
        return self.client.get(url, kwargs, format='json')

    def get_user(self, pk, **kwargs):
        url = reverse_lazy('user-detail', kwargs={'pk': pk})
        return self.client.get(url, kwargs, format='json')

    def post_user(self, username, password, email, first_name, last_name):
        url = reverse_lazy('user-list')
        data = {
            "username": username,
            "password": password,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_post_user_with_valid_data(self):
        """
        Ensure we can create a new User
        """
        response = self.post_user('test_username', 'test_password', 'test@test.com', 'test_first_name',
                                  'test_first_name')
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_user_with_duplicated_data(self):
        """
        Ensure we can not create a new User with duplicated username
        """
        response = self.post_user('admin', 'test_password', 'test@test.com', 'test_first_name', 'test_first_name')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_users(self):
        """
        Ensure we have only one user
        """
        response = self.get_users()
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_with_valid_pk(self):
        """
        Ensure we one user in users list
        """
        response = self.get_user(self.current_user.pk)
        assert response.status_code == status.HTTP_200_OK

    def test_get_user_with_fake_pk(self):
        """
        Ensure we one user in users list
        """
        response = self.get_user(111)  # fake pk
        assert response.status_code == status.HTTP_404_NOT_FOUND
