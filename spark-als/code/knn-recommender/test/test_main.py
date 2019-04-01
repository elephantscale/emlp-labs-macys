from unittest import TestCase


class TestMain(TestCase):
    def test_true_is_not_false(self):
        self.assertNotEqual(True, False)
