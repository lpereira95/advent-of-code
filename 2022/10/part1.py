

class Logger:

    def __init__(self, cycles_to_save):
        self.cycles_to_save = cycles_to_save
        self.values = []

    def log(self, X, cycle):
        if cycle not in self.cycles_to_save:
            return

        self.values.append(X)


def _create_values_to_save():
    val = 20
    step = 40
    values_to_save = [val]
    while True:
        val += step
        if val > 220:
            break
        values_to_save.append(val)

    return values_to_save


def compute_strenght(cycles, values):
    strength = 0
    for cycle, value in zip(cycles, values):
        strength += cycle * value

    return strength


if __name__ == "__main__":
    from _utils import load_data, apply_instructions

    filename = "input.dat"
    instructions = load_data(filename)

    logger = Logger(_create_values_to_save())
    apply_instructions(instructions, logger)

    answer = compute_strenght(logger.cycles_to_save, logger.values)
    question = "What is the sum of these six signal strengths?"

    print(f"{question} {answer}")
