# setUpClass and tearDownClass implemented as class methods:

import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()

#setUpModule and tearDownModule should be implemented as functions:

def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()



class MyFile:
    def __init__(self, filename, content):
        self.content = content

        with open(filename, "w") as fl:
            fl.write(content)
