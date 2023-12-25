from pathlib import Path
from random import sample

import networkx as nx
import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> tuple[set, list]:
    vertices = set()
    edges = []

    for line in lines:
        comp, target_str = line.split(": ")
        target_comps = target_str.split(" ")
        vertices.add(comp)
        vertices.update(target_comps)

        for comp2 in target_comps:
            edges.append([comp, comp2])

    return vertices, edges


def solve_part_1(vertices: set, edges: list) -> int:
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    for u, v in edges:
        graph.add_edge(u, v, capacity=1.0)

    nodes = list(graph.nodes())
    finished = False
    partitions = [[], []]
    while not finished:
        s, t = sample(nodes, 2)
        val, partitions = nx.minimum_cut(graph, s, t)
        if val == 3:
            finished = True
    return len(partitions[0]) * len(partitions[1])


@app.command()
def part_1(input_file: str = "input.txt"):
    vertices, edges = parse_input(read_input_file(input_file))
    print("The result is", solve_part_1(vertices, edges))


@app.command()
def part_2(input_file: str = "input.txt"):
    pass


if __name__ == "__main__":
    app()
