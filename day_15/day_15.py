from collections import defaultdict
from functools import reduce
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = tuple(map(lambda line: line.strip(), f.readlines()))

    return lines[0].split(",")


def hash(str: str) -> int:
    return reduce(lambda ac, c: ((ac + ord(c)) * 17) % 256, str, 0)


def parse_step(str) -> tuple:
    return (
        (str[-1], str[:-1], 0) if str[-1] == "-" else (str[-2], str[:-2], int(str[-1]))
    )


def arrange_lenses(sequence: list[str]) -> dict:
    boxes = defaultdict(lambda: ([], []))
    ops = [parse_step(s) for s in sequence]

    for op in ops:
        box = boxes[hash(op[1])]

        match op[0]:
            case "=":
                if op[1] in box[0]:
                    box[1][box[0].index(op[1])] = op[2]
                else:
                    box[0].append(op[1])
                    box[1].append(op[2])

            case "-":
                if op[1] in box[0]:
                    pos = box[0].index(op[1])
                    box[0].pop(pos)
                    box[1].pop(pos)
            case _:
                raise NotImplementedError

    return boxes


def focusing_power(box: tuple[list, list]) -> int:
    return sum([i * f for i, f in enumerate(box[1], start=1)])


def solve_part_1(sequence: list[str]) -> int:
    return sum([hash(s) for s in sequence])


def solve_part_2(sequence: list[str]) -> int:
    boxes = arrange_lenses(sequence)
    return sum([(box + 1) * focusing_power(boxes[box]) for box in boxes])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of hashes is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of hashes is", solve_part_2(data))


if __name__ == "__main__":
    app()
