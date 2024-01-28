import re
from pathlib import Path

import typer

app = typer.Typer()

DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


DIGIT_REGEX = re.compile(r"(?=(\d|" + "|".join(DIGIT_MAP.keys()) + "))")


def read_input_file(input_file_path: str) -> list:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def solve(data: list[str]) -> int:
    converted_lines = [[int(c) for c in line if c.isdigit()] for line in data]
    calibration_values = [line[0] + line[-1] for line in converted_lines]
    return sum(calibration_values)


def map_digits(line: str):
    mapped_line = "".join(DIGIT_MAP.get(d, d) for d in DIGIT_REGEX.findall(line))
    return mapped_line


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The sum of all calibration values is {solve(data)}")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    data = [map_digits(line) for line in data]
    print(f"The sum of all values is {solve(data)}")


if __name__ == "__main__":
    app()
