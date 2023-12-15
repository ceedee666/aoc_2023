import unittest
from unittest import TestCase

import day_15

test_string = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


class Testing(TestCase):
    def test_hash(self):
        result = day_15.hash("HASH")
        self.assertEqual(result, 52, "The hash should be 52.")

    def test_part_1(self): result = day_15.solve_part_1(test_string.split(","))
        self.assertEqual(result, 1320, "The sum of hashes should be 1320.")

    def test_part_2(self):
        result = day_15.solve_part_2(test_string.split(","))
        self.assertEqual(result, 145, "The sum of hashes should be 145.")


if __name__ == "__main__":
    unittest.main()
