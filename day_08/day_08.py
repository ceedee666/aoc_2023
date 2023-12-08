import itertools
import math
from collections.abc import Iterable
from functools import reduce
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str]) -> tuple:
    directions = itertools.cycle(data[0].strip())
    _maps = {line[:3]: (line[7:10], line[12:15]) for line in data[2:]}
    return directions, _maps


def navigate(directions: Iterable[str], _map: dict[str, tuple[str, str]]) -> list[str]:
    route = ["AAA"]

    while route[-1] != "ZZZ":
        left, right = _map[route[-1]]
        route.append(left if next(directions) == "L" else right)

    return route


def navigate_ghost(
    directions: Iterable[str], _map: dict[str, tuple[str, str]], start: str
) -> list[str]:
    route = [start]

    while route[-1][-1] != "Z":
        left, right = _map[route[-1]]
        route.append(left if next(directions) == "L" else right)

    return route


def navigate_ghosts(
    directions: Iterable[str], _map: dict[str, tuple[str, str]]
) -> list[tuple]:
    starting_nodes = list(filter(lambda k: k[-1] == "A", _map.keys()))
    routes = [(s, navigate_ghost(directions, _map, s)) for s in starting_nodes]

    return routes


def solve_part_1(data: list[str]) -> int:
    directions, _map = parse_input(data)
    route = navigate(directions, _map)
    return len(route) - 1


def solve_part_2(data: list[str]) -> int:
    directions, _map = parse_input(data)
    routes = navigate_ghosts(directions, _map)
    route_lengths = [len(r[1]) - 1 for r in routes]
    gcd = math.gcd(*route_lengths)
    return reduce(lambda x, y: x * y // gcd, route_lengths)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total winnings are", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total winnings are", solve_part_2(data))


if __name__ == "__main__":
    app()
