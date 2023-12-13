from enum import Enum
from itertools import groupby
from pathlib import Path

import typer

app = typer.Typer()


class Direction(Enum):
    NONE = -1
    HORIZONTAL = 0
    VERTICAL = 1


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> list[list[str]]:
    return [list(grp) for key, grp in groupby(lines, lambda x: x != "") if key]


def transpose(pattern: list[str]) -> list[str]:
    return list(map(lambda x: "".join(x), zip(*pattern)))


def find_horizontal_line_of_reflection(
    pattern: list[str], allow_errors: int = 0
) -> int:
    for i in range(1, len(pattern)):
        if (
            sum(
                [
                    0 if c == d else 1
                    for a, b in zip(reversed(pattern[:i]), pattern[i:])
                    for c, d in zip(a, b)
                ]
            )
            == allow_errors
        ):
            return i
    return 0


def find_line_of_reflection(
    pattern: list[str], allow_errors: int = 0
) -> tuple[Direction, int]:
    hr = find_horizontal_line_of_reflection(pattern, allow_errors)
    if hr > 0:
        return (Direction.HORIZONTAL, hr)

    vr = find_horizontal_line_of_reflection(transpose(pattern), allow_errors)
    if vr > 0:
        return (Direction.VERTICAL, vr)

    return (Direction.NONE, 0)


def find_lines_of_reflection(
    patterns: list[list[str]], allowed_errors: int = 0
) -> list[tuple[Direction, int]]:
    return [find_line_of_reflection(pattern, allowed_errors) for pattern in patterns]


def solve_part_1(data: list[str]) -> int:
    patterns = parse_input(data)
    lors = find_lines_of_reflection(patterns)
    return sum([r[1] if r[0] == Direction.VERTICAL else r[1] * 100 for r in lors])


def solve_part_2(data: list[str]) -> int:
    patterns = parse_input(data)
    lors = find_lines_of_reflection(patterns, allowed_errors=1)
    return sum([r[1] if r[0] == Direction.VERTICAL else r[1] * 100 for r in lors])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of notes is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of notes after clearing the smudges is", solve_part_2(data))


if __name__ == "__main__":
    app()
