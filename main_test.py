import unittest

from functions import get_response_code


class MainTest(unittest.TestCase):
    """
    Testing CLI Command Repository
    """

    def test_response(self):
        """
        Testing for URL response code for status 200 and 404.
        """
        self.assertEqual(
            get_response_code("https://www.google.com"), 200, "Should be 200"
        )
        self.assertEqual(
            get_response_code("https://www.google.com/incorrect_url"),
            404,
            "Should be 404",
        )


if __name__ == "__main__":
    unittest.main()
