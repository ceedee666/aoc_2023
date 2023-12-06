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


def solve_quad_equation(a: int, b: int, c: int) -> tuple[float, float]:
    sol_1 = (-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a)
    sol_2 = (-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a)
    return sol_1, sol_2


def solve_quad_equations(races: list) -> int:
    # dist = t * (dur - t)
    # dist = -t^2 + t * dur
    # -t^2 + t * dur - dist = 0
    solutions = [solve_quad_equation(-1, race[0], race[1] * -1) for race in races]
    new_records = [int(y) - int(x) for x, y in solutions]
    return math.prod(new_records)


@app.command()
def part_1():
    races = [(49, 263), (97, 1532), (94, 1378), (94, 1851)]
    print("The result is", solve(races))
    print("The result by solving the equations is", solve_quad_equations(races))


@app.command()
def part_2():
    races = [(49979494, 263153213781851)]
    print("The result is", solve_quad_equations(races))


if __name__ == "__main__":
    app()
