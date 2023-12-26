from collections import defaultdict, deque
from copy import copy
from pathlib import Path

import networkx as nx
import typer

app = typer.Typer()

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(
    lines: list[str],
) -> tuple[tuple[int, int], tuple[int, int], dict[tuple[int, int], str]]:
    map = {(r, c): lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}
    start = (0, lines[0].index("."))
    end = (len(lines) - 1, lines[-1].index("."))
    return start, end, map


def neighbors(
    pos: tuple[int, int], map: dict[tuple[int, int], str], slippery: bool = True
) -> list[tuple[int, int]]:
    r, c = pos
    if slippery:
        if map[pos] == "v":
            return [(r + 1, c)]
        if map[pos] == "^":
            return [(r - 1, c)]
        if map[pos] == ">":
            return [(r, c + 1)]
        if map[pos] == "<":
            return [(r, c - 1)]

    next = []
    for dr, dc in DIRS:
        n_r, n_c = r + dr, c + dc
        if (n_r, n_c) in map and map[(n_r, n_c)] != "#":
            next.append((n_r, n_c))

    return next


def longest_hike(
    start: tuple[int, int],
    end: tuple[int, int],
    map: dict[tuple[int, int], str],
    slippery: bool = True,
) -> int:
    dists = defaultdict(int)
    dists[start] = 0

    q = deque([(start, set())])

    while q:
        pos, path = q.popleft()
        new_dist = dists[pos] + 1

        for next_pos in neighbors(pos, map, slippery):
            if next_pos not in path:
                if new_dist > dists[next_pos]:
                    dists[next_pos] = new_dist
                    new_path = copy(path)
                    new_path.add(next_pos)
                    q.append((next_pos, new_path))

    return dists[end]


def find_vertices(
    map: dict[tuple[int, int], str], start: tuple[int, int], end: tuple[int, int]
) -> set[tuple[int, int]]:
    vertices = set(
        pos for pos in map if map[pos] == "." and len(neighbors(pos, map, False)) > 2
    )
    vertices.add(start)
    vertices.add(end)
    return vertices


def create_graph(
    start: tuple[int, int],
    end: tuple[int, int],
    map: dict[tuple[int, int], str],
) -> dict[tuple[int, int], list[tuple[tuple[int, int], int]]]:
    graph = defaultdict(list)
    vertices = find_vertices(map, start, end)

    for v in vertices:
        queue = deque()
        queue.append((v, 0))
        visited = set()

        while queue:
            pos, dist = queue.popleft()
            visited.add(pos)

            for n in neighbors(pos, map, False):
                if n in visited:
                    continue
                if n in vertices:
                    graph[v].append((n, dist + 1))
                    continue
                queue.append((n, dist + 1))

    return graph


def solve_part_1(
    start: tuple[int, int], end: tuple[int, int], map: dict[tuple[int, int], str]
):
    return longest_hike(start, end, map)


def solve_part_2(
    start: tuple[int, int], end: tuple[int, int], map: dict[tuple[int, int], str]
):
    g = create_graph(start, end, map)
    graph = nx.Graph()
    for u in g:
        graph.add_node(u)
        for v, d in g[u]:
            graph.add_edge(u, v, weight=d)

    all_path_lenght = []
    for p in nx.all_simple_paths(graph, start, end):
        path_lenght = sum(
            [graph.get_edge_data(p[i], p[i + 1])["weight"] for i in range(len(p) - 1)]
        )
        all_path_lenght.append(path_lenght)
    return max(all_path_lenght)


@app.command()
def part_1(input_file: str = "input.txt"):
    start, end, map = parse_input(read_input_file(input_file))
    print("The longest hike is", solve_part_1(start, end, map), "steps.")


@app.command()
def part_2(input_file: str = "input.txt"):
    start, end, map = parse_input(read_input_file(input_file))
    print("The longest hike is", solve_part_2(start, end, map), "steps.")


if __name__ == "__main__":
    app()
