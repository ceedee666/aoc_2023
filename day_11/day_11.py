from itertools import combinations
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(lines: list[str], gap_factor=2) -> list[tuple]:
    empty_rows = []
    for i, line in enumerate(lines):
        if all(map(lambda c: c == ".", line)):
            empty_rows.append(i)

    empty_cols = []
    for i in range(len(lines[0])):
        if all(map(lambda c: c == ".", [line[i] for line in lines])):
            empty_cols.append(i)

    galaxies = []
    for y, line in enumerate(lines):
        for x, _ in enumerate(line):
            if line[x] == "#":
                gap_x = len([i for i in empty_cols if i < x]) * (gap_factor - 1)
                gap_y = len([i for i in empty_rows if i < y]) * (gap_factor - 1)
                galaxies.append((x + gap_x, y + gap_y))

    return galaxies


def manhatten_distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(galaxies: list[tuple]) -> int:
    dists = [
        manhatten_distance(combi[0], combi[1]) for combi in combinations(galaxies, 2)
    ]
    return sum(dists)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    galaxis = parse_input(data)
    print("The sum of shortest paths is", solve(galaxis))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    galaxis = parse_input(data, 1_000_000)
    print("The sum of shortest paths is", solve(galaxis))


if __name__ == "__main__":
    app()
