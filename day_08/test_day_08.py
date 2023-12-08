import unittest
from unittest import TestCase

import day_08

test_string = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_string_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


test_string_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


class Testing(TestCase):
    def test_part_1(self):
        result = day_08.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 2, "The lenght of the path should be 2.")

        result = day_08.solve_part_1(test_string_2.split("\n"))
        self.assertEqual(result, 6, "The lenght of the path should be 6.")

    def test_part_2(self):
        result = day_08.solve_part_2(test_string_3.split("\n"))
        self.assertEqual(result, 6, "The lenght of the path should be 6.")


if __name__ == "__main__":
    unittest.main()
