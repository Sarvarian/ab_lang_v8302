import unittest
from main import Main
from examples import examples


class MainTest(unittest.TestCase):
    """ Testing The Main Routine """

    def test_expected_output_from_input(self):
        for example in examples:
            result = Main(example[0]).strip()
            expected = example[1].strip()
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
