import unittest
from unittest import TestCase

import day_23

test_string = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


class Testing(TestCase):
    def test_part_1(self):
        start, end, map = day_23.parse_input(test_string.split("\n"))
        self.assertEqual(
            day_23.solve_part_1(start, end, map), 94, "The result should be 94."
        )

    def test_part_2(self):
        start, end, map = day_23.parse_input(test_string.split("\n"))
        self.assertEqual(
            day_23.solve_part_2(start, end, map), 154, "The result should be 154."
        )


if __name__ == "__main__":
    unittest.main()
