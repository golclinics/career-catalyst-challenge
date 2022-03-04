import unittest

from .convert_to_seconds import conversion


class MyTestCase(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(conversion(5), 300)
        self.assertEqual(conversion(3), 180)
        self.assertEqual(conversion(2), 120)


if __name__ == '__main__':
    unittest.main()
