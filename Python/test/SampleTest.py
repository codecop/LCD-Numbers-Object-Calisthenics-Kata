import unittest
from lcd.sample import Sample


class SampleTest(unittest.TestCase):

    def testOne(self):
        self.assertEqual(2, 1 + 1)


if __name__ == "__main__":
    unittest.main()
