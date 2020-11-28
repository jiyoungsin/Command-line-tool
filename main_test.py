import unittest

from functions import get_response_code
from functions import get_urls_from_file


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
        self.assertEqual(
            type(get_response_code("https://www.google.com")), int, "should be a int"
        )

    def test_url_from_files(self):

        self.assertEqual(
            type(get_urls_from_file('urls.txt')), list, "should be a list"
        )


if __name__ == "__main__":
    unittest.main()
