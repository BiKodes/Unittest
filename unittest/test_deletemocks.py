import unittest
from unittest.mock import Mock


from delete_fun import rm, RemovalService


class RmTestCase(unittest.TestCase):


    @Mock.patch('delete_fun.os')
    @Mock.patch('delete_fun.os.path')
    def test_rm(self, mock_os, mock_path):
        #set up the mock
        mock_path.isfile.return_Value = False

        rm("any path")

        #test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        #make the file 'exist'

        mock_path.isfile.return_value = True

        rm("any path")

        #test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

class RemovalServiceTestCase(unittest.TestCase):

   
    @Mock.patch('delete_fun.os')
    @Mock.patch('delete_fun.os.path')
    def test_rm(self, mock_os, mock_path):
        #Instantiate our service
        reference = RemovalService()

        #set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        #test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present")

        #make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")
