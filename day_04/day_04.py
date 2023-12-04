import math
from collections import defaultdict
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str]) -> list[tuple]:
    return [parse_line(line) for line in data]


def parse_line(line: str):
    card, numbers = line.split(": ")
    _, cardid = card.split()
    cardid = int(cardid)

    winning_nums, my_nums = numbers.split(" | ")
    winning_nums = list(map(int, winning_nums.split()))
    my_nums = list(map(int, my_nums.split()))

    return cardid, winning_nums, my_nums


def matching_numbers(cards: list[tuple]) -> list[tuple]:
    return [(card[0], len(set(card[1]) & set(card[2]))) for card in cards]


def solve_part_1(data: list[str]):
    cards = parse_input(data)
    card_values = [
        math.pow(2, matching - 1)
        for _, matching in matching_numbers(cards)
        if matching >= 1
    ]
    return sum(card_values)


def solve_part_2(data: list[str]) -> int:
    cards = parse_input(data)
    card_count = defaultdict(lambda: 1)

    for id, matching in matching_numbers(cards):
        for next_id in range(id + 1, id + matching + 1):
            card_count[next_id] += card_count[id]

    return sum([card_count[c[0]] for c in cards])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The cards are worth", solve_part_1(data), "points.")


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total number of cards is", solve_part_2(data))


if __name__ == "__main__":
    app()
