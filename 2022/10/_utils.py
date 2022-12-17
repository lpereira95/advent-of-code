

def load_data(filename):
    with open(filename, "r") as file:
        instructions = []
        for line in file:
            values = line.strip().split()
            if len(values) == 1:
                instructions.append((values[0], None))
            else:
                instructions.append((values[0], int(values[1])))

    return instructions


def apply_instructions(instructions, logger):
    X = 1
    cycle = 0
    for instruction in instructions:
        X, cycle = apply_instruction(instruction, X, cycle, logger)

    return X, cycle


def apply_instruction(instruction, X, cycle, logger):
    cmd, value = instruction
    return globals()[f"_apply_instruction_{cmd}"](
        value, X, cycle, logger)


def _apply_instruction_noop(value, X, cycle, logger):
    cycle += 1
    logger.log(X, cycle)

    return X, cycle


def _apply_instruction_addx(value, X, cycle, logger):
    cycle += 1
    logger.log(X, cycle)

    cycle += 1
    logger.log(X, cycle)
    X += value

    return X, cycle
