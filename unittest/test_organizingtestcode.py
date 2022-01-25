import unittest
from unittest import runner

class DefaultWidgetSizeTestCase(unittest.TestCase):

    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')
        
    def test_defaut_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100,150), 'wrong size after resize')


class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget("The widget")

    def tearDown(self):
        self.widget.dispose()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

def testSomething():
    something = makeSomething()
    assert something.name is not None

testcase = unittest.FunctionTestCase(testSomething,
                                    setUp=makeSomethingDB,
                                    tearDown=deleteSomethingDB)