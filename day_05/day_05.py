from itertools import batched
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str], part_2: bool = False) -> tuple[list, list[list]]:
    first = data[0]
    rest = data[3:]

    seeds = list(map(int, first.split(": ")[1].split()))
    if part_2:
        seeds = [(batch[0], batch[0] + batch[1] - 1) for batch in batched(seeds, 2)]

    maps = []
    _map = []

    for line in rest:
        if len(line) == 0:
            continue  # empty line, skip.
        if line[-1] == ":":
            maps.append(_map)
            _map = []
        if line[0].isdigit():
            dest, source, lenght = map(int, line.split())
            if not part_2:
                _map.append((range(source, source + lenght), dest - source))
            else:
                _map.append(([source, source + lenght - 1], dest - source))

    maps.append(_map)

    return seeds, maps


def map_location(location: int, maps: list[tuple[range, int]]) -> int:
    for mapping in maps:
        if location in mapping[0]:
            return location + mapping[1]
    return location


def map_seed_location(seed: int, maps: list[list]) -> int:
    location = seed
    for _map in maps:
        location = map_location(location, _map)
    return location


def min_location_for_range(range: tuple[int, int], maps: list[list]) -> int:
    start, end = range

    if not maps:
        return start

    _map = maps[0]

    for mapping in _map:
        map_start, map_end = mapping[0]
        diff = mapping[1]
        # range is map
        if map_start <= start <= map_end and map_start <= end <= map_end:
            new_range = (start + diff, end + diff)
            return min_location_for_range(new_range, maps[1:])

        # range ends outside
        elif map_start <= start <= map_end and end > map_end:
            new_range_1 = (start + diff, map_end + diff)
            new_range_2 = (map_end + 1, end)
            return min(
                min_location_for_range(new_range_1, maps[1:]),
                min_location_for_range(new_range_2, maps),
            )

        # range starts outside
        elif start < map_start and map_start <= end <= map_end:
            new_range_1 = (start, map_start - 1)
            new_range_2 = (map_start + diff, end + diff)
            return min(
                min_location_for_range(new_range_1, maps),
                min_location_for_range(new_range_2, maps[1:]),
            )
        # range starts and ends outside
        elif start < map_start and end > map_end:
            new_range_1 = (start, map_start - 1)
            new_range_2 = (map_start + diff, map_end + diff)
            new_range_3 = (map_end + 1, end)
            return min(
                min_location_for_range(new_range_1, maps),
                min_location_for_range(new_range_2, maps[1:]),
                min_location_for_range(new_range_3, maps),
            )
    # no match to a map
    return min_location_for_range((start, end), maps[1:])


def solve_part_1(data: list[str]) -> int:
    seeds, almanac_maps = parse_input(data)
    locations = [map_seed_location(seed, almanac_maps) for seed in seeds]
    return min(locations)


def solve_part_2(data: list[str]) -> int:
    seed_ranges, maps = parse_input(data, True)
    min_locations = [
        min_location_for_range(seed_range, maps) for seed_range in seed_ranges
    ]
    return min(min_locations)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The lowest location numbers is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The lowest location numbers is", solve_part_2(data))


if __name__ == "__main__":
    app()
