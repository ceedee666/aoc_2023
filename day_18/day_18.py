from pathlib import Path

import typer

app = typer.Typer()
DIR_MAP = {"0": "R", "1": "D", "2": "L", "3": "U"}
DIRECTIONS = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> list[tuple[str, int]]:
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]


def parse_input_2(lines: list[str]) -> list[tuple[str, int]]:
    colors = [line.split("#")[1][:6] for line in lines]
    return [(DIR_MAP[c[-1]], int(c[:5], 16)) for c in colors]


def volume(edges: list[tuple[int, int]], perimeter: int) -> int:
    # Gaußsche Trapezformel https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Trapezformel
    # Pick's Theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
    area = abs(
        0.5
        * sum(
            [
                (e_i[1] + e_j[1]) * (e_i[0] - e_j[0])
                for e_i, e_j in zip(edges, edges[1:] + [edges[0]])
            ]
        )
    )
    inside = area - perimeter / 2 + 1
    return int(inside + perimeter)


def solve(directions: list[tuple[str, int]]) -> int:
    current_pos = (0, 0)
    edges = []
    edges.append(current_pos)
    perimeter = 0

    for d, dist in directions:
        dr, dc = DIRECTIONS[d]
        current_pos = (current_pos[0] + dr * dist, current_pos[1] + dc * dist)
        edges.append(current_pos)
        perimeter += dist

    return volume(edges, perimeter)


@app.command()
def part_1(input_file: str = "input.txt"):
    directions = parse_input(read_input_file(input_file))
    print("The lagoon can hold", solve(directions), "m3 of lava.")


@app.command()
def part_2(input_file: str = "input.txt"):
    directions = parse_input_2(read_input_file(input_file))
    print("The lagoon can hold", solve(directions), "m3 of lava.")


if __name__ == "__main__":
    app()
