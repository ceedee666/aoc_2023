from functools import cache
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_line(line: str, folds) -> tuple[str, tuple[int, ...]]:
    pattern, nums = line.split()
    nums = tuple(map(int, nums.split(",")))

    if folds > 1:
        pattern = "?".join([pattern] * folds)
        nums = nums * folds
    return (pattern, nums)


def parse_input(lines: list[str], folds=1) -> list[tuple[str, tuple[int, ...]]]:
    return [parse_line(line, folds) for line in lines]


@cache
def num_of_solutions(pattern: str, nums: tuple[int, ...], current_group_size=0) -> int:
    if len(pattern) == 0:
        # Check if this is a sollution.
        # It is a sollution if all numbers are used and no group is open.
        if not nums and current_group_size == 0:
            return 1
        else:
            return 0

    result = 0

    possible = [".", "#"] if pattern[0] == "?" else [pattern[0]]

    for p in possible:
        if p == "#":
            if len(pattern) > 1:
                # expand the group by one letter
                result += num_of_solutions(pattern[1:], nums, current_group_size + 1)
            else:
                if nums and len(nums) == 1 and nums[0] == current_group_size + 1:
                    # possible solution
                    result += 1
        else:
            if current_group_size > 0:
                # check if we are inside group
                if nums and nums[0] == current_group_size:
                    # group is full. remove it from the list
                    result += num_of_solutions(pattern[1:], nums[1:], 0)
            else:
                # if not inside group, check the next letter
                result += num_of_solutions(pattern[1:], nums, 0)

    return result


def solve_part_1(data: list[str]) -> int:
    records = parse_input(data)
    solutions = [num_of_solutions(pattern, nums) for pattern, nums in records]
    return sum(solutions)


def solve_part_2(data: list[str]) -> int:
    records = parse_input(data, folds=5)
    solutions = [num_of_solutions(pattern, nums) for pattern, nums in records]
    return sum(solutions)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total number of arrangements is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total number of arrangements is", solve_part_2(data))


if __name__ == "__main__":
    app()
