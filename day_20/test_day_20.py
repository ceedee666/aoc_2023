import unittest
from unittest import TestCase

import day_20

test_string = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""


class Testing(TestCase):
    def test_part_1(self):
        gates = day_20.parse_input(test_string.split("\n"))
        result = day_20.solve_part_1(gates)
        self.assertEqual(result, 32000000, "The result should be 32000000.")


if __name__ == "__main__":
    unittest.main()
