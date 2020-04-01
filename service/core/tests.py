from django.test import TestCase

from core.utils import str2bool


class TestUtils(TestCase):
    def test_str_to_bool_returns_true(self):
        for s in ['true', 'True', 'yes', 'on', '1']:
            self.assertTrue(str2bool(s))

    def test_str_to_bool_returns_false(self):
        for s in ['false', 'False', 'no', 'off', '0', '', 'AAAA', 'aaaa', 0, 1, True, False]:
            self.assertFalse(str2bool(s))


