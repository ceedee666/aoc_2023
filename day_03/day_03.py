import re
from math import prod
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str]) -> tuple[dict, dict]:
    symbols, numbers = {}, {}
    for y, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            numbers[(match.start(), y)] = int(match.group())
        for match in re.finditer(r"[+\-*/=#@$%&]", line):
            symbols[(match.start(), y)] = match.group()
    return symbols, numbers


def all_neighbour_coords(pos: tuple, number: int):
    x_n, y_n = pos
    num_lenght = len(str(number))

    neighbour_coords = [(x, y_n - 1) for x in range(x_n - 1, x_n + num_lenght + 1)]
    neighbour_coords = neighbour_coords + [(x_n - 1, y_n), (x_n + num_lenght, y_n)]
    neighbour_coords = neighbour_coords + [
        (x, y_n + 1) for x in range(x_n - 1, x_n + num_lenght + 1)
    ]
    return neighbour_coords


def all_number_coords(pos: tuple, number: int):
    x_n, y_n = pos
    num_length = len(str(number))

    return [(x, y_n) for x in range(x_n, x_n + num_length)]


def is_part(pos: tuple, number: int, symbols: dict) -> bool:
    neighbour_coords = all_neighbour_coords(pos, number)
    return any([c in symbols for c in neighbour_coords])


def find_parts(symbols: dict, numbers: dict) -> dict:
    part_pos = filter(lambda p: is_part(p, numbers[p], symbols), numbers)
    return {p: numbers[p] for p in part_pos}


def find_gears(symbols: dict, numbers: dict):
    gears = []
    number_coords = [
        (pos, numbers[pos], set(all_number_coords(pos, numbers[pos])))
        for pos in numbers
    ]

    for pos in symbols:
        if symbols[pos] == "*":
            gear_neighbour_coords = set(all_neighbour_coords(pos, 1))
            adjacent_numbers = [
                n[1] for n in number_coords if len(n[2] & gear_neighbour_coords) >= 1
            ]
            if len(adjacent_numbers) == 2:
                gears.append((pos, adjacent_numbers))

    return gears


def solve_part_1(data: list[str]):
    symbols, numbers = parse_input(data)
    parts = find_parts(symbols, numbers)
    return sum(parts.values())


def solve_part_2(data: list[str]):
    symbols, numbers = parse_input(data)
    gears = find_gears(symbols, numbers)
    gear_ratios = [prod(g[1]) for g in gears]
    return sum(gear_ratios)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of part numbers is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of gear ratios is", solve_part_2(data))


if __name__ == "__main__":
    app()
