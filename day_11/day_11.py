from itertools import combinations
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(lines: list[str]) -> tuple[list[tuple], list[int], list[int]]:
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
                galaxies.append((x, y))

    return galaxies, empty_rows, empty_cols


def manhatten_distance(
    a: tuple, b: tuple, empty_rows: list[int], empty_cols: list[int], factor: int
) -> int:
    empty_row_count = len(
        list(filter(lambda row: (a[1] < row < b[1]) or (b[1] < row < a[1]), empty_rows))
    )

    empty_col_count = len(
        list(filter(lambda col: (a[0] < col < b[0]) or (b[0] < col < a[0]), empty_cols))
    )

    dist = (
        abs(a[0] - b[0])
        + (empty_row_count * (factor - 1))
        + abs(a[1] - b[1])
        + (empty_col_count * (factor - 1))
    )

    return dist


def solve(
    galaxies: list[tuple], empty_rows: list[int], empty_cols: list[int], factor: int = 2
) -> int:
    dists = [
        manhatten_distance(combi[0], combi[1], empty_rows, empty_cols, factor)
        for combi in combinations(galaxies, 2)
    ]
    return sum(dists)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    galaxis, empty_rows, empty_cols = parse_input(data)
    print("The sum of shortest paths is", solve(galaxis, empty_rows, empty_cols))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    galaxis, empty_rows, empty_cols = parse_input(data)
    print(
        "The sum of shortest paths is", solve(galaxis, empty_rows, empty_cols, 1000000)
    )


if __name__ == "__main__":
    app()
