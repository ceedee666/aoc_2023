import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import typer

app = typer.Typer()


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int
    total: int = field(init=False)

    def __post_init__(self):
        self.total = self.x + self.m + self.a + self.s


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def create_rule_fn(attr: str, value: int, op: str, res: str):
    if op == ">":
        return lambda p: res if getattr(p, attr) > value else ""
    else:
        return lambda p: res if getattr(p, attr) < value else ""


def create_res_fn(res: str):
    return lambda _: res


def parse_input(lines: list[str]) -> tuple[dict[str, list], list[Part]]:
    rule_lines = lines[: lines.index("")]
    part_lines = lines[lines.index("") + 1 :]

    parts = []
    for line in part_lines:
        parts.append(Part(*map(int, re.findall(r"\d+", line))))

    rules = {}
    for line in rule_lines:
        name, elements = line.split("{")
        rules[name] = []
        for element in elements[:-1].split(","):
            if len(element) > 1 and ":" in element:
                attr = element[0]
                op = element[1]
                value = int(element[2 : element.index(":")])
                res = element[element.index(":") + 1 :]

                rules[name].append(create_rule_fn(attr, value, op, res))
            else:
                rules[name].append(create_res_fn(element))

    return rules, parts


def apply_rules(
    rules: dict[str, list], part: Part, start: str = "in"
) -> tuple[str, Part]:
    next_wf = start
    finished = False
    res = ""

    while not finished:
        for rule in rules[next_wf]:
            res = rule(part)
            if res:
                if res in ["A", "R"]:
                    finished = True
                else:
                    next_wf = res
                break

    return res, part


def solve_part_1(rules: dict[str, list], parts: list[Part]) -> int:
    wf_results = [apply_rules(rules, part) for part in parts]
    return sum([r[1].total for r in wf_results if r[0] == "A"])


def parse_input_part_2(lines: list[str]) -> dict[str, list]:
    rule_lines = lines[: lines.index("")]

    rules = {}
    for line in rule_lines:
        name, elements = line.split("{")
        rules[name] = []
        for element in elements[:-1].split(","):
            if len(element) > 1 and ":" in element:
                cond, res = element.split(":")
                rules[name].append((cond, res))
            else:
                rules[name].append(("", element))

    return rules


def possible_combinations(
    part: dict[str, tuple[int, int]], wf: str, workflows: dict[str, list]
) -> int:
    if wf == "R":
        return 0
    if wf == "A":
        return math.prod([e - s + 1 for s, e in part.values()])

    count = 0

    for cond, res in workflows[wf]:
        if cond == "":
            count += possible_combinations(part, res, workflows)

        else:
            attr = cond[0]
            op = cond[1]
            value = int(cond[2:])

            s, e = part[attr]

            if op == "<":
                pass_s, pass_e = (s, value - 1)
                fail_s, fail_e = (value, e)
            else:
                fail_s, fail_e = (s, value)
                pass_s, pass_e = (value + 1, e)

            # possible interval -> move to next wf
            if pass_s < pass_e:
                new_part = dict(part)
                new_part[attr] = (pass_s, pass_e)
                count += possible_combinations(new_part, res, workflows)

            # fail range not empty -> move to nex rule
            if fail_s < fail_e:
                new_part = dict(part)
                new_part[attr] = (fail_s, fail_e)
                part = new_part

    return count


def solve_part_2(rules: dict[str, list]) -> int:
    p = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    return possible_combinations(p, "in", rules)


@app.command()
def part_1(input_file: str = "input.txt"):
    rules, parts = parse_input(read_input_file(input_file))
    print("The total rating of all accepted parts is", solve_part_1(rules, parts))


@app.command()
def part_2(input_file: str = "input.txt"):
    rules = parse_input_part_2(read_input_file(input_file))
    print("The total number of possibilities is", solve_part_2(rules))


if __name__ == "__main__":
    app()
