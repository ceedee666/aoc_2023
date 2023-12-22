from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations
from pathlib import Path

import typer

app = typer.Typer()

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def str_to_coords(s: str) -> tuple[int, int, int]:
    return tuple(map(int, s.split(",")))


def parse_input(
    lines: list[str],
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    bricks = [line.split("~") for line in lines]
    bricks = [(str_to_coords(s), str_to_coords(e)) for s, e in bricks]
    bricks = [(s, e) if s[2] <= e[2] else (e, s) for s, e in bricks]
    return bricks


def all_coords(s: tuple[int, ...], e: tuple[int, ...]) -> list[tuple[int, ...]]:
    x_s, y_s, z_s = s
    x_e, y_e, z_e = e

    if x_s != x_e:
        return [(x, y_s, z_s) for x in range(min(x_s, x_e), max(x_s, x_e) + 1)]
    elif y_s != y_e:
        return [(x_s, y, z_s) for y in range(min(y_s, y_e), max(y_s, y_e) + 1)]
    else:
        return [(x_s, y_s, z) for z in range(min(z_s, z_e), max(z_s, z_e) + 1)]


def drop_bricks(
    bricks: list[tuple[tuple[int, ...], tuple[int, ...]]]
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    height = defaultdict(int)
    dropped_bricks = []

    # sort bricks by z coordinate
    bricks = sorted(bricks, key=lambda b: b[0][2])

    for s, e in bricks:
        x_s, y_s, z_s = s
        x_e, y_e, z_e = e

        new_z = max([height[(x, y)] for x, y, _ in all_coords(s, e)]) + 1

        if x_s == x_e and y_s == y_e:
            new_s = (x_s, y_s, new_z)
            new_e = (x_e, y_e, new_z + (z_e - z_s))
        else:
            new_s = (x_s, y_s, new_z)
            new_e = (x_e, y_e, new_z)

        dropped_bricks.append((new_s, new_e))
        for x, y, z in all_coords(new_s, new_e):
            height[(x, y)] = z

    return dropped_bricks


def support_coords(coords: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    return [(x, y, z - 1) for x, y, z in coords]


def supported_by(b1: list[tuple[int, ...]], b2: list[tuple[int, ...]]) -> bool:
    return len(set(support_coords(b1)) & set(b2)) > 0


def calulate_support(
    bricks: list[tuple[tuple[int, ...], tuple[int, ...]]]
) -> dict[int, list[int]]:
    support = defaultdict(list)
    brick_coords = {}

    for id, (s, e) in enumerate(bricks):
        brick_coords[id] = all_coords(s, e)

    for id1, id2 in combinations(range(len(brick_coords)), 2):
        b1 = brick_coords[id1]
        b2 = brick_coords[id2]
        if supported_by(b1, b2):
            support[id1].append(id2)
        elif supported_by(b2, b1):
            support[id2].append(id1)

    return support


def falling_bricks(id: int, support: dict[int, list[int]]) -> int:
    _support = deepcopy(support)
    q = deque()
    q.append(id)

    falling = 0
    while q:
        id = q.popleft()
        for next_id in _support:
            if next_id != id and id in _support[next_id]:
                _support[next_id].remove(id)
                if len(_support[next_id]) == 0:
                    q.append(next_id)
                    falling += 1
    return falling


def solve_part_1(bricks: list[tuple[tuple[int, ...], tuple[int, ...]]]) -> int:
    bricks = drop_bricks(bricks)
    support = calulate_support(bricks)

    not_removeable = set()
    for id in support:
        if len(support[id]) == 1:
            not_removeable.update(support[id])
    return len(bricks) - len(not_removeable)


def solve_part_2(bricks: list[tuple[tuple[int, ...], tuple[int, ...]]]) -> int:
    bricks = drop_bricks(bricks)
    support = calulate_support(bricks)

    return sum([falling_bricks(id, support) for id, _ in enumerate(bricks)])


@app.command()
def part_1(input_file: str = "input.txt"):
    bricks = parse_input(read_input_file(input_file))
    print(solve_part_1(bricks), "can be removed.")


@app.command()
def part_2(input_file: str = "input.txt"):
    bricks = parse_input(read_input_file(input_file))
    print("The sum of bricks that would falls is", solve_part_2(bricks))


if __name__ == "__main__":
    app()
