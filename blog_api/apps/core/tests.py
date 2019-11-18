from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model


class UserAPITestCase(APITestCase):
    def setUp(self) -> None:
        super(UserAPITestCase, self).setUp()
        User = get_user_model()
        self.current_user_password = 'admin'
        self.current_user = User.objects.create_user(username='admin', email='admin@gmail.com', password=self.current_user_password)

    def tearDown(self) -> None:
        super(UserAPITestCase, self).tearDown()
        self.current_user.delete()


class LoggedUserAPITestCase(UserAPITestCase):

    def setUp(self) -> None:
        super(LoggedUserAPITestCase, self).setUp()
        self.client.login(username=self.current_user.username, password=self.current_user_password)

    def tearDown(self) -> None:
        super(LoggedUserAPITestCase, self).tearDown()
        self.client.logout()