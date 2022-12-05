
def step(stacks, move):
    n, stack_from_id, stack_to_id = move
    stack_from = stacks[stack_from_id]
    stack_to = stacks[stack_to_id]

    stack_to.extend(stack_from[-n:])

    for _ in range(n):
        stack_from.pop()


if __name__ == "__main__":
    from _utils import load_data, collect_top_letters, move_crates

    filename = "input.dat"
    stacks, moves = load_data(filename)

    move_crates(stacks, moves, step)

    answer = collect_top_letters(stacks)
    question = "After the rearrangement procedure completes, what crate ends up on top of each stack?"

    print(f"{question} {answer}")
