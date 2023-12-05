import unittest
from unittest import TestCase

import day_05

test_string = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class Testing(TestCase):
    def test_parse_input(self):
        parsed = day_05.parse_input(test_string.split("\n"))
        self.assertEqual(len(parsed[0]), 4, "The data should contain 4 seeds.")
        self.assertEqual(len(parsed[1]), 7, "The data should contian 7 maps.")

    def test_part_1(self):
        result = day_05.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 35, "The result should be 35")

    def test_part_2(self):
        result = day_05.solve_part_2(test_string.split("\n"))
        self.assertEqual(result, 46, "The result should be 46")


if __name__ == "__main__":
    unittest.main()
