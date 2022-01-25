import unittest

from unittest.mock import Mock
from delete_fun import RemovalService, UploadService

@Mock.patch('delete_fun.sys')
@Mock.patch('delete_fun.os')
@Mock.patch('delete_fun.os.path')
def test_something(self, mock_os_path, mock_os, mock_sys):
    pass

