import datetime
import unittest
from unittest.mock import Mock

import requests

from my_calendar import is_weekday, get_holidays
from requests.exceptions import Timeout


#Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

#Mock datetime to control today's date
datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()

    #Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

#Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday

#Test Tuesday is a weekend
assert is_weekday()

#Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday

#Test Saturday is not a weekday
assert not is_weekday()

#Mock requests to control its behaviour
requests = Mock()

class TestCalendar(unittest.TestCase):

    def test_get_holidays_timeout(self):

        #Test a connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()


if __name__ == '__main__':
    unittest.main()