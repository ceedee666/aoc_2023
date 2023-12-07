from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import typer

app = typer.Typer()

CARD_STRENGTH = "23456789TJQKA"
CARD_STRENGTH_WITH_JOKER = "J23456789TQKA"

HAND_STRENGTH = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5],
]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def strength(hand: str, with_joker: bool) -> tuple[int, list[int]]:
    if with_joker:
        possible_hands = [hand.replace("J", c) for c in CARD_STRENGTH_WITH_JOKER[1:]]
    else:
        possible_hands = [hand]

    hand_s = max(
        [HAND_STRENGTH.index(sorted(Counter(h).values())) for h in possible_hands]
    )

    if with_joker:
        card_s = [CARD_STRENGTH_WITH_JOKER.index(c) for c in hand]
    else:
        card_s = [CARD_STRENGTH.index(c) for c in hand]

    return hand_s, card_s


def solve_part_1(data: list[str]) -> int:
    hands = [(hand, int(bid)) for hand, bid in map(str.split, data)]
    hands = sorted(hands, key=lambda h: strength(h[0], False))
    return sum([(i + 1) * h[1] for i, h in enumerate(hands)])


def solve_part_2(data: list[str]) -> int:
    hands = [(hand, int(bid)) for hand, bid in map(str.split, data)]
    hands = sorted(hands, key=lambda h: strength(h[0], True))
    return sum([(i + 1) * h[1] for i, h in enumerate(hands)])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total winnings are", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The total winnings are", solve_part_2(data))


if __name__ == "__main__":
    app()
