import unittest
from unittest import TestCase

import day_01

test_string = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_string_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteeni"""


class Testing(TestCase):
    def test_part_1(self):
        r = day_01.solve_part_1(test_string.split("\n"))

        self.assertEqual(
            142,
            r,
            "The result shoud be correct.",
        )

    def test_part_2(self):
        r = day_01.solve_part_2(test_string_2.split("\n"))

        self.assertEqual(
            281,
            r,
            "The result shoud be correct.",
        )


if __name__ == "__main__":
    unittest.main()
