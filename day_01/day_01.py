import re
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def solve_part_1(data: list[str]):
    digits = [list(filter(lambda str: str.isdigit(), line)) for line in data]
    calibration_values = [int(line[0] + line[-1]) for line in digits]
    return sum(calibration_values)


def map_digits(line: str):
    digit_map = {
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

    mapped_line = ""
    regex = r"(?=(\d|" + "|".join(digit_map.keys()) + "))"
    for m in re.findall(regex, line):
        if m.isdigit():
            mapped_line += m
        else:
            mapped_line += digit_map[m]

    return mapped_line


def solve_part_2(data: list[str]):
    data = [map_digits(line) for line in data]
    return solve_part_1(data)


@app.command()
def part_1(input_file: str):
    data = read_input_file(input_file)
    print(f"The sum of all calibration values is {solve_part_1(data)}")


@app.command()
def part_2(input_file: str):
    data = read_input_file(input_file)
    print(f"The sum of all calibration values is {solve_part_2(data)}")


if __name__ == "__main__":
    app()
