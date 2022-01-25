import unittest
from unittest.mock import Mock

from delete_fun import RemovalService, UploadService

class RemovalServiceTestCase(unittest.TestCase):

    @Mock.patch('delete_fun.os.path')
    @Mock.path('delete_fun.os')
    def test_rm(self, mock_os, mock_path):

        #Instantiate our service
        reference = RemovalService()

        #set up the mock

        mock_path.isfile.return_value = False

        reference.rm("Any Path")

        # test that the remove call was NOT called.

        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("Any Path")

        mock_os.remove.assert_called_with("Any Path")


class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self, mock_rm):
        #build our dependencies
        mock_removal_service = Mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        #call upload_complete, which should, in turn, call `rm`:

        reference.upload_complete("My Uploaded File")

        #Test that it called the rm method
        mock_removal_service.rm.assert_called_with("My Uploaded File")
