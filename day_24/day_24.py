from itertools import combinations
from pathlib import Path

import numpy as np
import typer
import z3

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    parts = [line.split(" @ ") for line in lines]
    return [
        (tuple(map(int, pos.split(", "))), tuple(map(int, vel.split(", "))))
        for pos, vel in parts
    ]


def solve_part_1(
    stones: list[tuple[tuple[int, ...], tuple[int, ...]]],
    lower: int = 200000000000000,
    upper: int = 400000000000000,
) -> int:
    intersections = 0

    for s1, s2 in combinations(stones, 2):
        (x1, y1, _), (vx1, vy1, _) = s1
        (x2, y2, _), (vx2, vy2, _) = s2

        m1 = vy1 / vx1
        m2 = vy2 / vx2
        if m1 == m2:
            continue

        A = np.array([[m1, -1], [m2, -1]])
        b = np.array([m1 * x1 - y1, m2 * x2 - y2])

        x, y = np.linalg.solve(A, b)
        if lower <= x <= upper and lower <= y <= upper:
            t1 = (x - x1) / vx1
            t2 = (x - x2) / vx2
            if t1 > 0 and t2 > 0:
                intersections += 1

    return intersections


def solve_part_2(stones: list[tuple[tuple[int, ...], tuple[int, ...]]]) -> int:
    solver = z3.Solver()
    x, y, z, vx, vy, vz = z3.Ints("x y z vx vy vz")
    for i, stone in enumerate(stones[:3]):
        a, b, c = stone[0]
        va, vb, vc = stone[1]
        t = z3.Int(f"t{i}")
        solver.add(t > 0)
        solver.add(x + vx * t == a + va * t)
        solver.add(y + vy * t == b + vb * t)
        solver.add(z + vz * t == c + vc * t)

    if solver.check() == z3.sat:
        m = solver.model()
        x = m.eval(x).as_long()
        y = m.eval(y).as_long()
        z = m.eval(z).as_long()
        return x + y + z
    else:
        return -1


@app.command()
def part_1(input_file: str = "input.txt"):
    stones = parse_input(read_input_file(input_file))
    print(solve_part_1(stones), "stones intersect")


@app.command()
def part_2(input_file: str = "input.txt"):
    stones = parse_input(read_input_file(input_file))
    print("The sum of x, y, z is ", solve_part_2(stones))


if __name__ == "__main__":
    app()
