import unittest
from unittest import TestCase

import day_12

test_string = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# test_string = "?###???????? 3,2,1"


class Testing(TestCase):
    def test_part_1(self):
        result = day_12.solve_part_1(test_string.split("\n"))
        self.assertEqual(result, 21, "There should be 21 possible arrangements.")

    def test_part_2(self):
        result = day_12.solve_part_2(test_string.split("\n"))
        self.assertEqual(
            result, 525152, "There should be 525152 possible arrangements."
        )


if __name__ == "__main__":
    unittest.main()
