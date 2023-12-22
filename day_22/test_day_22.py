import unittest
from unittest import TestCase

import day_22

test_string = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


class Testing(TestCase):
    def test_parse_input(self):
        bricks = day_22.parse_input(test_string.split("\n"))
        self.assertEqual(len(bricks), 7, "There should be 7 bricks in the result.")
        self.assertTrue(
            all([len(b) == 2 for b in bricks]),
            "Each brick should have a start and an end.",
        )
        self.assertTrue(
            all([len(s) == 3 and len(e) == 3 for s, e in bricks]),
            "Start and end should consist of 3 numbers.",
        )

    def test_part_1(self):
        bricks = day_22.parse_input(test_string.split("\n"))
        self.assertEqual(day_22.solve_part_1(bricks), 5, "The result should be 5.")

    def test_part_2(self):
        bricks = day_22.parse_input(test_string.split("\n"))
        self.assertEqual(day_22.solve_part_2(bricks), 7, "The result should be 7.")


if __name__ == "__main__":
    unittest.main()
