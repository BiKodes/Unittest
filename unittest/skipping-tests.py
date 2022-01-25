import unittest
import sys

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("Shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library")
    def test_format(self):
        #Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        #Windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")

            #Test code that depends on the external resource
            pass
        
#Classes can be skipped just like methods:
@unittest.skip("Showing class skipping")
class MySkippedTestCase(unittest.TestCase):

    def test_not_run(self):
        pass

#Expected failures use the expectedFailure() decorator.
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken") 

if __name__ == '__main__':
    unittest.main()
    