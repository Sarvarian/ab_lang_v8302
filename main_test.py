import unittest
from main import Main


class MainTest(unittest.TestCase):
    """ Testing The Main Routine """

    examples: list[list[str]] = [
        [
            """
		printf 'Hello, world!'
		""",
            """
		printf("Hello, world!");
		"""
        ],
    ]

    def test_expected_output_from_input(self):
        for example in self.examples:
            result = Main(example[0]).strip()
            expected = example[1].strip()
            self.assertEqual(expected, result,
                             f"\nexpected:\n{expected}\nresult:\n{result}\n")


if __name__ == '__main__':
    unittest.main()
