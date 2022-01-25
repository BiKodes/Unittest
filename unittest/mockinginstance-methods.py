from unittest import mock
from unittest.mock import Mock
from delete_fun import RemovalService, UploadService

import unittest

class RemovalServiceTestCase(unittest.TestCase):

    
    @Mock.path('delete_fun.os')
    @Mock.path('delete_fun.os.path')
    def test_rm(self, mock_os, mock_path):
        #Instantiate Our Service
        reference = RemovalService()

        #setup the mock
        mock_path.isfile.return_value = False

        reference.rm("Any Path")

        #test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm =("Any Path")

        mock_os.remove.assert_called_with("Any Path")

class UploadServiceTestCase(unittest.TestCase):

    @Mock.path.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):

        #Build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my upload file")

        #check that it called the rm method of our removal_service
        removal_service.rm.assert_called_with("my upload file")
