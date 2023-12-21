from collections import Counter, deque
from math import ceil
from pathlib import Path

import typer

app = typer.Typer()

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(
    lines: list[str],
) -> tuple[tuple[int, int], dict, int, int]:
    grid = {(r, c): ch for r, l in enumerate(lines) for c, ch in enumerate(l)}
    start = list(filter(lambda p: grid[p] == "S", grid))[0]
    row_count = len(lines)
    col_count = len(lines[0])
    return start, grid, row_count, col_count


def neighbors(
    pos: tuple[int, int],
    grid: dict,
    wrap: bool = False,
    row_count: int = 0,
    col_count: int = 0,
) -> list[tuple[int, int]]:
    r, c = pos
    neighbors = []
    for dr, dc in DIRS:
        new_pos = (r + dr, c + dc)
        new_r, new_c = new_pos
        if wrap:
            if grid[(new_r % row_count, new_c % col_count)] in ".S":
                neighbors.append(new_pos)
        else:
            if new_pos in grid and grid[new_pos] in ".S":
                neighbors.append(new_pos)

    return neighbors


def bfs(
    start: tuple[int, int],
    grid: dict,
    steps: int = 64,
    wrap: bool = False,
    row_count: int = 0,
    col_count: int = 0,
) -> int:
    queue = deque([(start, 0)])
    distances = {}
    seen = set()

    while len(queue) > 0:
        ((r, c), step) = queue.popleft()
        for n in neighbors(
            (r, c),
            grid,
            wrap,
            row_count,
            col_count,
        ):
            if n not in seen:
                seen.add(n)
                distances[n] = step + 1
                if distances[n] < steps:
                    queue.append((n, step + 1))

    reachable_distances = [
        d for d in distances if distances[d] <= steps and distances[d] % 2 == steps % 2
    ]
    destinations = list(Counter(reachable_distances).keys())
    return len(destinations)


def quadratic_seq_formula(A: int, B: int, C: int):
    return lambda n: A * n**2 + B * n + C


def solve_part_1(
    start: tuple[int, int],
    grid: dict,
    steps: int = 64,
) -> int:
    return bfs(start, grid, steps)


def solve_part_2(
    start: tuple[int, int],
    grid: dict,
    row_count: int,
    col_count: int,
    steps: int = 26501365,
) -> int:
    mod = steps % row_count

    a = bfs(start, grid, mod, True, row_count, col_count)
    b = bfs(start, grid, mod + row_count, True, row_count, col_count)
    c = bfs(start, grid, mod + 2 * row_count, True, row_count, col_count)

    diff_1_1 = b - a
    diff_1_2 = c - b
    diff_2 = diff_1_2 - diff_1_1

    # https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
    A = diff_2 // 2
    B = diff_1_1 - 3 * A
    C = a - B - A
    f = quadratic_seq_formula(A, B, C)

    # f(n) = num of reachable cells in n * H steps
    result = f(ceil(steps / row_count))

    return result


@app.command()
def part_1(input_file: str = "input.txt"):
    start, grid, _, _ = parse_input(read_input_file(input_file))
    print(solve_part_1(start, grid), "positions are reachable with 64 steps.")


@app.command()
def part_2(input_file: str = "input.txt"):
    start, grid, row_count, col_count = parse_input(read_input_file(input_file))
    print(solve_part_2(start, grid, row_count, col_count), "positions are reachable.")


if __name__ == "__main__":
    app()
