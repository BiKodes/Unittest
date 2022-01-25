import unittest
from unittest.mock import patch

from requests.api import request

from patch_mock import requests, get_holidays

class TestCalendar(unittest.TestCase):

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout(self, mock_request):
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()


if __name__ == '__main__':
    unittest.main()