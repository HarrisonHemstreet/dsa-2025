import unittest


class HelloWorld:
    def say_hi(self):
        return "Hello, World!"


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hello_world = HelloWorld()

    def test_say_hi(self):
        self.assertEqual(self.hello_world.say_hi(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
