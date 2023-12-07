import unittest
from unittest import TestCase

import day_07

test_string = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


class Testing(TestCase):
    def test_part_1(self):
        result = day_07.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 6440, "The total winnings should be 6440")

    def test_part_2(self):
        result = day_07.solve_part_2(test_string.split("\n"))
        self.assertEqual(result, 5905, "The total winnings with Jokers should be 5905")


if __name__ == "__main__":
    unittest.main()
