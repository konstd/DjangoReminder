from datetime import timedelta
from unittest import skip

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from rest_framework.authtoken.models import Token

from rest_framework.test import APIClient


ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@example.com'
ADMIN_PASSWORD = '1234567Q'

BASE_API_V1_PATH = '/api/v1'


class TestDjangoCalls(TestCase):
    def test_docs_are_available(self):
        response = self.client.get('/api/docs/', follow=True)
        self.assertEqual(response.status_code, 200)


class TestDRFAuth(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            ADMIN_USERNAME,
            ADMIN_EMAIL,
            ADMIN_PASSWORD,
        )
        self.drf_client = APIClient()

        self.token = Token.objects.get_or_create(user=self.admin)[0]
        self.authorized_drf_client = APIClient()
        self.authorized_drf_client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )

    def tearDown(self):
        self.admin.delete()

    @staticmethod
    def build_api_url(endpoint):
        return f'{BASE_API_V1_PATH}{endpoint}'

    def create_user_via_api(self, credentials):
        response = self.drf_client.post(self.build_api_url('/accounts/registration/'), {
            'username': credentials['username'],
            'password': credentials['password'],
            'email': credentials['email'],
        })
        return response.data

    def test_v1_token_endpoint_is_available(self):
        response = self.drf_client.get(self.build_api_url('/auth/token/'))
        self.assertEqual(response.status_code, 405)  # working endpoint will return method not allowed

    def test_v1_registration_endpoint_is_available(self):
        response = self.drf_client.get(self.build_api_url('/accounts/registration/'))
        self.assertEqual(response.status_code, 405)  # working endpoint will return method not allowed

    def test_v1_token_is_available(self):
        response = self.drf_client.post(self.build_api_url('/auth/token/'), {
            'username': ADMIN_USERNAME,
            'password': ADMIN_PASSWORD,
            'email': ADMIN_EMAIL,
        })
        self.assertDictEqual(response.data, {
            'token': self.token.key,
        })

    def test_list_all_account(self):
        credentials = {
            'username': 'user1',
            'password': '1q2w3e!Q@W#E',
            'email': 'email1@example.com',
        }

        self.create_user_via_api(credentials)

        response = self.authorized_drf_client.get(self.build_api_url('/accounts/'))

        self.assertEqual(len(response.data), 1)  # only one user was created

        data = dict(response.data[0])

        self.assertEqual(data['username'], credentials['username'])
        self.assertEqual(data['email'], credentials['email'])

    def test_get_my_account(self):
        response = self.authorized_drf_client.get(self.build_api_url('/accounts/me/'))

        self.assertDictEqual(response.data, {
             'username': self.admin.username,
             'email': self.admin.email,
             'first_name': '',
             'last_name': ''
        })

    @skip('Need to fix CELERY_ALWAYS_EAGER functionality')
    def test_create_reminder(self, send_email_mock):
        credentials = {
            'username': 'user2',
            'password': '1q2w3e!Q@W#E',
            'email': 'email2@example.com',
        }

        self.create_user_via_api(credentials)

        user = User.objects.get(username=credentials['username'])

        response = self.authorized_drf_client.post(self.build_api_url('/reminders/'), {
            'owner': self.admin.id,
            'title': 'title',
            'body': 'body',
            'location': 'location',
            'target_date': timezone.now() + timedelta(days=1),
            'participants': [user.id],
        })
