import unittest
from hello_world import HelloWorld


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.hello_world = HelloWorld()

    def test_hello_worsld(self):
        self.assertEqual(self.hello_world.say_hi(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
