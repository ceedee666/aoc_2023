import math

import typer

app = typer.Typer()


def solve(races: list) -> int:
    races = [
        (duration, record, list(enumerate([duration] * (duration + 1))))
        for duration, record in races
    ]
    distances = [
        (duration, record, [speed * (charge - speed) for speed, charge in vars])
        for duration, record, vars in races
    ]
    new_records = [
        (
            duration,
            old_record,
            len(list(filter(lambda result: result > old_record, results))),
        )
        for duration, old_record, results in distances
    ]
    return math.prod([race[2] for race in new_records])


@app.command()
def part_1():
    races = [(49, 263), (97, 1532), (94, 1378), (94, 1851)]
    print("The result is", solve(races))


@app.command()
def part_2():
    races = [(49979494, 263153213781851)]
    print("The result is", solve(races))


if __name__ == "__main__":
    app()
