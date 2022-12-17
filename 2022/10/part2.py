
class Logger:

    def __init__(self, width=40):
        self.width = width
        self.crt = []

    def log(self, X, cycle):
        if (cycle - 1) % self.width == 0:
            self.crt.append('')

        draw_position = (cycle - 1) % 40
        if X - 1 <= draw_position <= X + 1:
            char_ = '#'

        else:
            char_ = '.'

        self.crt[-1] = self.crt[-1] + char_

    def print_crt(self):
        print("\n".join(self.crt))


if __name__ == "__main__":
    from _utils import load_data, apply_instructions

    filename = "input.dat"
    instructions = load_data(filename)

    logger = Logger()
    apply_instructions(instructions, logger)

    logger.print_crt()

    question = "What eight capital letters appear on your CRT?"
    answer = "Look to the CRT!"

    print(f"{question} {answer}")
