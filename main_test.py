import unittest

from functions import *


class MainTest(unittest.TestCase):
    # def test_sum(self):
    #     self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_response(self):
        self.assertEqual(get_response_code('https://www.google.com'), 200, "Should be 200")
        self.assertEqual(get_response_code('https://www.google.com/incorrect_url'), 404, "Should be 404")


if __name__ == '__main__':
    unittest.main()
