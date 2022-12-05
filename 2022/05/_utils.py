import re


def load_data(filename):
    with open(filename, "r") as file:
        stacks = dict()
        while True:
            line = file.readline()
            if line.strip()[0] == "1":
                break

            for i, letter in enumerate(line[1::4]):
                k = i + 1
                if letter == " ":
                    continue

                stacks[k] = [letter] + stacks.get(k, [])

        file.readline()
        line = file.readline()
        moves = []

        regexp = re.compile(r"move (\d+) from (\d+) to (\d+)")
        while line:
            res = regexp.search(line.strip())

            moves.append([int(m) for m in res.groups()])

            line = file.readline()
            if not line:
                break

    sorted_stacks = dict(sorted(stacks.items(), key=lambda item: item[0]))
    return sorted_stacks, moves


def move_crates(stacks, moves, step):
    for move in moves:
        step(stacks, move)


def collect_top_letters(stacks):
    letters = ""
    for stack in stacks.values():
        letters += stack[-1]

    return letters
