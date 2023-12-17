import heapq
from collections import defaultdict
from functools import reduce
from pathlib import Path

import typer

app = typer.Typer()

DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> list[list[int]]:
    return [[int(c) for c in line] for line in lines]


def solve(heatloss_map: list[list[int]], min_dist=1, max_dist=3) -> int:
    max_y = len(heatloss_map)
    max_x = len(heatloss_map[0])

    heap = []
    # loss, x,y, direction
    heapq.heappush(heap, (0, 0, 0, -1))
    loss = defaultdict(lambda: 1e9)
    seen = set()

    while heap:
        current_loss, x, y, direction = heapq.heappop(heap)

        if x == max_x - 1 and y == max_y - 1:
            return current_loss

        if (x, y, direction) in seen:
            continue
        else:
            seen.add((x, y, direction))

        for new_direction, (dx, dy) in enumerate(DIRECTIONS):
            if new_direction == direction or (new_direction + 2) % 4 == direction:
                continue

            additional_loss = 0

            for dist in range(1, max_dist + 1):
                new_x = x + dx * dist
                new_y = y + dy * dist

                if 0 <= new_x < max_x and 0 <= new_y < max_y:
                    additional_loss += heatloss_map[new_y][new_x]
                    new_loss = current_loss + additional_loss
                    if (
                        dist >= min_dist
                        and new_loss < loss[(new_x, new_y, new_direction)]
                    ):
                        loss[(new_x, new_y, new_direction)] = new_loss
                        heapq.heappush(
                            heap,
                            (
                                new_loss,
                                new_x,
                                new_y,
                                new_direction,
                            ),
                        )

    return -1


@app.command()
def part_1(input_file: str = "input.txt"):
    heatloss_map = parse_input(read_input_file(input_file))
    print("The minimal heatloss is", solve(heatloss_map))


@app.command()
def part_2(input_file: str = "input.txt"):
    heatloss_map = parse_input(read_input_file(input_file))
    print("The minimal heatloss is", solve(heatloss_map, 4, 10))


if __name__ == "__main__":
    app()
