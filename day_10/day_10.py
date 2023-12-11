from collections import deque
from pathlib import Path

import typer
from click import group

app = typer.Typer()


TILES = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def find_start(grid: list[str]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == "S":
                return x, y


def solve_part_1(grid: list[str], start_shape: str = "7") -> tuple[int, dict, list]:
    start_x, start_y = find_start(grid)
    grid[start_y] = grid[start_y].replace("S", start_shape)

    queue = deque([(start_x, start_y)])
    dist = {(start_x, start_y): 0}

    while len(queue) > 0:
        x, y = queue.popleft()
        shape = grid[y][x]
        if shape in TILES:
            for dx, dy in TILES[shape]:
                nx = x + dx
                ny = y + dy

                if (nx, ny) not in dist:
                    dist[(nx, ny)] = dist[(x, y)] + 1
                    queue.append((nx, ny))

    return max(dist.values()), dist, grid


def solve_part_2(grid: list[str], start_shape: str = "7") -> int:
    _, dist, grid = solve_part_1(grid, start_shape)
    in_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            crosses = 0
            if (x, y) not in dist:
                for x2 in range(x + 1, len(grid[y])):
                    shape = grid[y][x2]
                    if (x2, y) in dist and shape in "|7F":
                        crosses += 1
                if crosses % 2 == 1:
                    in_count += 1

    return in_count


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The farthest position is", solve_part_1(data)[0], "steps from the start.")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(solve_part_2(data), "tiles are enclosed in the loop.")


if __name__ == "__main__":
    app()
