from collections import Counter, deque
from copy import deepcopy
from math import prod
from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = list(map(lambda line: line.strip(), f.readlines()))

    return lines


def parse_input(lines: list[str]) -> dict[str, dict]:
    gates = {}
    for line in lines:
        first, second = line.split(" -> ")
        out = second.split(", ")
        if first == "broadcaster":
            gate_type = "b"
            gate_name = "broadcaster"
        else:
            gate_type = first[0]
            gate_name = first[1:]

        gate = {"name": gate_name, "type": gate_type, "out": out, "in": [], "state": {}}
        gates[gate_name] = gate

    for gate in gates.values():
        for out in gate["out"]:
            if out in gates:
                gates[out]["in"].append(gate["name"])

    for gate in gates.values():
        match gate["type"]:
            case "%":
                gate["state"]["%"] = 0
            case "&":
                for name in gate["in"]:
                    gate["state"][name] = 0
    return gates


def process_pulse(pulse: tuple[int, str, str], gates: dict[str, dict]) -> list[tuple]:
    signal, target, source = pulse
    new_pulses = []

    if target in gates:
        gate = gates[target]
        match gate["type"]:
            case "b":
                new_signal = signal

                for name in gate["out"]:
                    new_pulses.append((new_signal, name, gate["name"]))

            case "%":
                if signal == 0:
                    gate["state"]["%"] = 1 if gate["state"]["%"] == 0 else 0
                    new_signal = 0 if gate["state"]["%"] == 0 else 1

                    for name in gate["out"]:
                        new_pulses.append((new_signal, name, gate["name"]))
            case "&":
                gate["state"][source] = signal
                if all([gate["state"][s] == 1 for s in gate["state"]]):
                    new_signal = 0
                else:
                    new_signal = 1

                for name in gate["out"]:
                    new_pulses.append((new_signal, name, gate["name"]))
            case _:
                raise NotImplementedError

    return new_pulses


def solve_part_1(gates: dict[str, dict], n: int = 1000) -> int:
    processed = []

    for _ in range(n):
        queue = deque()
        queue.append((0, "broadcaster", "button"))
        while queue:
            pulse = queue.popleft()
            signal, _, _ = pulse
            processed.append(signal)

            new_pulses = process_pulse(pulse, gates)
            queue.extend(new_pulses)
    counter = Counter(processed)
    return counter[0] * counter[1]


def solve_part_2(gates: dict[str, dict], lb_inputs: list[str]) -> int:
    steps = []
    for lb_in in lb_inputs:
        cycles = 0
        finished = False

        new_gates = deepcopy(gates)
        while not finished:
            queue = deque()
            queue.append((0, "broadcaster", "button"))
            cycles += 1

            while queue:
                pulse = queue.popleft()

                new_pulses = process_pulse(pulse, new_gates)
                queue.extend(new_pulses)
                if (1, "lb", lb_in) in new_pulses:
                    finished = True

        steps.append(cycles)

    return prod(steps)


@app.command()
def part_1(input_file: str = "input.txt"):
    gates = parse_input(read_input_file(input_file))
    print("The product of low and high pulses is", solve_part_1(gates))


@app.command()
def part_2(input_file: str = "input.txt"):
    rx_inputs = ["rz", "lf", "br", "fk"]
    gates = parse_input(read_input_file(input_file))
    result = solve_part_2(gates, rx_inputs)
    print("The number of button presses required is", result)


if __name__ == "__main__":
    app()
