import unittest
from unittest import TestCase

import day_17

test_string = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


test_string2 = """111111111111
999999999991
999999999991
999999999991
999999999991"""


class Testing(TestCase):
    def test_part_1(self):
        hm = day_17.parse_input(test_string.split("\n"))
        result = day_17.solve(hm)
        self.assertEqual(result, 102, "The minimal heat loss should be 102.")

    def test_part_2(self):
        hm = day_17.parse_input(test_string.split("\n"))
        result = day_17.solve(hm, 4, 10)
        self.assertEqual(result, 94, "The minimal heat loss should be 94.")

        hm = day_17.parse_input(test_string2.split("\n"))
        result = day_17.solve(hm, 4, 10)
        self.assertEqual(result, 71, "The minimal heat loss should be 71.")


if __name__ == "__main__":
    unittest.main()
