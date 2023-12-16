from collections import defaultdict, deque
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> tuple[str, ...]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = tuple(map(lambda line: line.strip(), f.readlines()))

    return lines


def energize_grid(
    grid: tuple[str, ...], start: tuple[int, int, tuple[int, int]]
) -> defaultdict[tuple[int, int], set[tuple[int, int]]]:
    queue = deque([start])
    tiles = defaultdict(set)

    while len(queue) > 0:
        x, y, (dx, dy) = queue.popleft()
        next_steps = []

        if (dx, dy) not in tiles[(x, y)]:
            tiles[(x, y)].add((dx, dy))
            match grid[y][x]:
                case ".":
                    next_steps.append((x + dx, y + dy, (dx, dy)))
                case "|":
                    if dx == 0:
                        next_steps.append((x + dx, y + dy, (dx, dy)))
                    else:
                        next_steps.append((x, y + 1, (0, 1)))
                        next_steps.append((x, y - 1, (0, -1)))
                case "-":
                    if dy == 0:
                        next_steps.append((x + dx, y + dy, (dx, dy)))
                    else:
                        next_steps.append((x + 1, y, (1, 0)))
                        next_steps.append((x - 1, y, (-1, 0)))
                case "/":
                    if dx == 0:
                        next_steps.append((x + (dy * (-1)), y, (dy * (-1), 0)))
                    else:
                        next_steps.append((x, y + (dx * (-1)), (0, dx * (-1))))
                case "\\":
                    if dx == 0:
                        next_steps.append((x + dy, y, (dy, 0)))
                    else:
                        next_steps.append((x, y + dx, (0, dx)))
                case _:
                    raise NotImplementedError

        next_steps = [
            step
            for step in next_steps
            if 0 <= step[0] < len(grid[0]) and 0 <= step[1] < len(grid)
        ]
        queue.extend(next_steps)

    return tiles


def energized_tiles(tiles: dict[tuple[int, int], set[tuple[int, int]]]) -> int:
    return len([t for t in tiles if len(tiles[t]) > 0])


def solve_part_1(grid: tuple[str, ...]) -> int:
    tiles = energize_grid(grid, (0, 0, (1, 0)))
    return energized_tiles(tiles)


def solve_part_2(grid: tuple[str, ...]) -> int:
    max_y = len(grid)
    max_x = len(grid[0])
    start_configs = (
        [(x, 0, (0, 1)) for x in range(max_x)]
        + [(x, len(grid) - 1, (0, -1)) for x in range(max_x)]
        + [(0, y, (1, 0)) for y in range(max_y)]
        + [(len(grid[0]) - 1, y, (-1, 0)) for y in range(max_y)]
    )
    return max([energized_tiles(energize_grid(grid, c)) for c in start_configs])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print(solve_part_1(data), "tiles are energized.")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("A maximum of", solve_part_2(data), "tiles can be energized.")


if __name__ == "__main__":
    app()
