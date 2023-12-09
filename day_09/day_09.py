from pathlib import Path

import typer

app = typer.Typer()


def read_input_file(input_file_path: str) -> list[str]:
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda line: line.strip(), lines))


def parse_input(data: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in data]


def all_zero(sequence: list[int]) -> bool:
    return all(seq == 0 for seq in sequence)


def diff_sequences(sequence: list[int]) -> list[list[int]]:
    result = [sequence]

    while not all_zero(result[-1]):
        next_seq = [
            val - result[-1][i - 1] for i, val in enumerate(result[-1][1:], start=1)
        ]
        result.append(next_seq)

    return result


def all_diff_sequences(sequences: list[list[int]]) -> list[list[list[int]]]:
    return [diff_sequences(seq) for seq in sequences]


def calc_next_values(sequence_lists: list[list[list[int]]]) -> list[list[list[int]]]:
    for seq_list in sequence_lists:
        rev_seq_list = list(reversed(seq_list))
        for i, seq in enumerate(rev_seq_list[1:], start=1):
            new_val_end = seq[-1] + rev_seq_list[i - 1][-1]
            seq.append(new_val_end)

            new_val_start = seq[0] - rev_seq_list[i - 1][0]
            seq.insert(0, new_val_start)
    return sequence_lists


def solve_part_1(data: list[str]) -> int:
    sequences = parse_input(data)
    sequences = all_diff_sequences(sequences)
    sequences = calc_next_values(sequences)
    return sum(seq_list[0][-1] for seq_list in sequences)


def solve_part_2(data: list[str]) -> int:
    sequences = parse_input(data)
    sequences = all_diff_sequences(sequences)
    sequences = calc_next_values(sequences)
    return sum(seq_list[0][0] for seq_list in sequences)


@app.command()
def part_1(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of the extrapolated values is", solve_part_1(data))


@app.command()
def part_2(input_file: str = "input.txt"):
    data = read_input_file(input_file)
    print("The sum of the extrapolated values is", solve_part_2(data))


if __name__ == "__main__":
    app()
