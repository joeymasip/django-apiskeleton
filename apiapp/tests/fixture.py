from django.test import TestCase
from rest_framework_jwt.settings import api_settings
from apiapp.models import User


class FixtureTestCase(TestCase):
    fixtures = [
        'test/users.json',
    ]

    user_admin = None
    user_normal_1 = None
    user_normal_2 = None

    def get_token(self, user_inst: User):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user_inst)
        token = jwt_encode_handler(payload)
        return token

    def setUp(self):
        self.user_admin = User.objects.get(pk=1)
        self.user_normal_1 = User.objects.get(pk=2)
        self.user_normal_2 = User.objects.get(pk=3)
