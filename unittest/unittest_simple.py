import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_sym(self):
        self.assertEqual(reverse('a'), 'a')

    def test_pal(self):
        self.assertEqual(reverse('дед'), 'дед')

    def test_str(self):
        self.assertEqual(reverse('дедвнутри'), 'иртунвдед')

    def test_wrong_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_list(self):
        with self.assertRaises(TypeError):
            reverse(['bob'])


unittest.main()