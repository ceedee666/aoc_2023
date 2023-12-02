from collections import defaultdict
from functools import reduce
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str]) -> list:
    games = []
    for line in data:
        game, rounds = line.split(": ")
        _, id = game.split()

        result = []
        for round in rounds.split("; "):
            cubes = {}
            for colors in round.split(", "):
                count, color = colors.split()
                cubes[color] = int(count)

            result.append(cubes)

        games.append((int(id), result))

    return games


def filter_valid_games(games: list, cubes: dict = {"red": 12, "green": 13, "blue": 14}):
    return list(filter(lambda game: is_valid_game(game, cubes), games))


def is_valid_game(game: tuple, cubes: dict):
    return all(
        [all([round[color] <= cubes[color] for color in round]) for round in game[1]]
    )


def min_cubes_for_game(game: tuple[int, list]):
    min_cubes = defaultdict(int)
    for round in game[1]:
        for color in round:
            min_cubes[color] = max(min_cubes[color], round[color])
    return game[0], game[1], min_cubes


def power_of_game(game: tuple[int, list, dict]):
    id, rounds, min_cubes = game
    power = reduce(lambda x, y: x * y, [min_cubes[color] for color in min_cubes])
    return id, rounds, min_cubes, power


def solve_part_1(data: list[str]):
    games = parse_input(data)
    valid_games = filter_valid_games(games)
    return sum([g[0] for g in valid_games])


def solve_part_2(data: list[str]):
    games = parse_input(data)
    games = [min_cubes_for_game(game) for game in games]
    games = [power_of_game(game) for game in games]
    return sum([game[3] for game in games])


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of the IDs of possible games is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of the power of the sets is", solve_part_2(data))


if __name__ == "__main__":
    app()
