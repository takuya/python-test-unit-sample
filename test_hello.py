
import unittest
import sys
from io import StringIO
from Hello import Hello

class HelloTest(unittest.TestCase):
    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__


    def test_say(self):
        hello = Hello()
        hello.say()
        self.assertEqual("hello world\n",sys.stdout.getvalue())
    def test_hello(self):
        hello = Hello()
        result = hello.hello()
        self.assertTrue(type(result) is str)
        self.assertIsInstance(result, str)
        self.assertEqual("Hello", result)
    def test_raise_error(self):
        hello = Hello()
        with self.assertRaises(RuntimeError):
            hello.raise_error()

