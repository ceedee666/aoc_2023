import itertools as it
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> tuple[str, ...]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = tuple(map(lambda line: line.strip(), f.readlines()))

    return lines


def transpose(strings: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(map(lambda x: "".join(x), zip(*strings)))


def sort_line(line: str, reverse: bool = False) -> str:
    parts = line.split("#")
    parts = [
        sorted(p, key=lambda c: 1 if c == "." else 0, reverse=reverse) for p in parts
    ]
    parts = list(map(lambda p: "".join(p), parts))
    return "#".join(parts)


def sort_lines(lines: tuple[str, ...], reverse: bool = False) -> tuple[str, ...]:
    return tuple(sort_line(line, reverse) for line in lines)


def tilt(platform: tuple[str, ...], direction: str = "N") -> tuple[str, ...]:
    match direction:
        case "N" | "S":
            platform = transpose(platform)
            platform = sort_lines(platform, direction == "S")
            platform = transpose(platform)
        case "E" | "W":
            platform = sort_lines(platform, direction == "E")
        case _:
            raise NotImplementedError

    return platform


def tilt_cycle(platform: tuple[str, ...]) -> tuple[str, ...]:
    for d in "NWSE":
        platform = tilt(platform, d)
    return platform


def find_cycle(platform: tuple[str, ...]) -> tuple[int, int, dict]:
    states = {platform: 0}

    for i in it.count(1):
        platform = tilt_cycle(platform)
        if platform in states:
            start = states[platform]
            return start, i - start, states
        else:
            states[platform] = i

    return 0, 0, {}


def row_weights(platform: tuple[str, ...]) -> int:
    weights = [i * r.count("O") for i, r in enumerate(reversed(platform), start=1)]
    return sum(weights)


def solve_part_1(platform: tuple[str, ...]) -> int:
    platform = tilt(platform)
    return row_weights(platform)


def solve_part_2(platform: tuple[str, ...]) -> int:
    N = 1_000_000_000

    start, length, stats = find_cycle(platform)
    idx = start + (N - start) % length

    rev_map = {v: k for k, v in stats.items()}
    return row_weights(rev_map[idx])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total load is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    load = solve_part_2(data)
    print("The total load is", load)


if __name__ == "__main__":
    app()
