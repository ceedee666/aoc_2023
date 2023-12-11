import unittest
from unittest import TestCase

import day_10

test_string = """.....
.S-7.
.|.|.
.L-J.
....."""

test_string_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

test_string_3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test_string_4 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


class Testing(TestCase):
    def test_part_1(self):
        result = day_10.solve_part_1(test_string.split("\n"), "F")
        self.assertEqual(result[0], 4, "The distance should be 4.")

        result = day_10.solve_part_1(test_string_2.split("\n"), "F")
        self.assertEqual(result[0], 8, "The distance should be 8.")

    def test_part_2(self):
        result = day_10.solve_part_2(test_string_3.split("\n"), "F")
        self.assertEqual(result, 4, "4 shapes should be inside the loop.")

        result = day_10.solve_part_2(test_string_4.split("\n"), "7")
        self.assertEqual(result, 10, "10 shapes should be inside the loop.")


if __name__ == "__main__":
    unittest.main()
