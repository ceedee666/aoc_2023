import unittest
from unittest import TestCase

import day_14

test_string = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

test_string_1 = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#...."""

test_string_2 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O"""

test_string_3 = """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O"""


def str_to_tuple(s):
    return tuple(s.split("\n"))


class Testing(TestCase):
    def test_transpose(self):
        self.assertEqual(
            day_14.transpose(("123", "456")),
            ("14", "25", "36"),
        )

    def test_part_1(self):
        result = day_14.solve_part_1(str_to_tuple(test_string))
        self.assertEqual(result, 136, "The total load should be 136.")

    def test_cycle(self):
        platform = str_to_tuple(test_string)
        platform_c1 = day_14.tilt_cycle(platform)
        self.assertEqual(
            platform_c1,
            str_to_tuple(test_string_1),
            "After one cycle the platform should look like this: " + test_string_1,
        )
        platform_c2 = day_14.tilt_cycle(platform_c1)
        self.assertEqual(
            platform_c2,
            str_to_tuple(test_string_2),
            "After two cycle the platform should look like this: " + test_string_1,
        )
        platform_c3 = day_14.tilt_cycle(platform_c2)
        self.assertEqual(
            platform_c3,
            str_to_tuple(test_string_3),
            "After three cycle the platform should look like this: " + test_string_1,
        )

    def test_part_2(self):
        load = day_14.solve_part_2(str_to_tuple(test_string))
        self.assertEqual(
            load, 64, "The total load after 1000000000 cycles should be 64."
        )


if __name__ == "__main__":
    unittest.main()
