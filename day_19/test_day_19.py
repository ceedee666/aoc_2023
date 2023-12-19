import unittest
from unittest import TestCase

import day_19

test_string = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


class Testing(TestCase):
    def test_parse(self):
        rules, parts = day_19.parse_input(test_string.split("\n"))
        self.assertEqual(len(rules), 11, "There should be 11 workflows.")
        self.assertEqual(
            len(rules["pv"]), 2, "There should be 2 rules in the pv workflow."
        )
        self.assertEqual(
            len(rules["hdj"]), 2, "There should be 2 rules in the hdj workflow."
        )
        self.assertEqual(len(parts), 5, "There should be 5 parts.")
        self.assertEqual(
            parts[-1].s,
            1013,
            "There s attribute of the last past should have the value 1013.",
        )

    def test_part_1(self):
        rules, parts = day_19.parse_input(test_string.split("\n"))
        result = day_19.solve_part_1(rules, parts)
        self.assertEqual(result, 19114, "The total rating should be 19114.")

    def test_part_2(self):
        rules = day_19.parse_input_part_2(test_string.split("\n"))
        result = day_19.solve_part_2(rules)
        self.assertEqual(
            result,
            167409079868000,
            "The number of possible combinations should be 167409079868000.",
        )


if __name__ == "__main__":
    unittest.main()
