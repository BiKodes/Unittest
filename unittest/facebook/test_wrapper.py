import unittest
from unittest import mock

import facebook
import wrapper_class

class SimpleFacebookTestCase(unittest.TestCase):

    @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
    def test_post_message(self, mock_put_object):
        sf = wrapper_class.SimpleFacebook("fake oauth token")
        sf.post_message("Hello World")

        #Verify
        mock_put_object.assert_called_with(message="Hello World")