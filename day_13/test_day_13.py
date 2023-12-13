import unittest
from unittest import TestCase

import day_13

test_string = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


class Testing(TestCase):
    def test_transpose(self):
        self.assertEqual(
            day_13.transpose(["123", "456"]),
            ["14", "25", "36"],
        )

    def test_part_1(self):
        result = day_13.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 405, "The sum of the notes should be 405.")

    def test_part_2(self):
        result = day_13.solve_part_2(test_string.split("\n"))
        self.assertEqual(
            result,
            400,
            "The sum of the notes after removing the smudges should be 400.",
        )


if __name__ == "__main__":
    unittest.main()
