
from _utils import (
    _get_abs_pos_difference,
    _is_placed_diagonally,
    _get_closer_by_one,
)


def _attract_linked(mover):
    head_pos = mover.current_position
    tail_pos = mover.linked.current_position

    diff = sum(_get_abs_pos_difference(head_pos, tail_pos))
    if diff < 3 - int(not _is_placed_diagonally(head_pos, tail_pos)):
        return

    new_tail_pos = _get_closer_by_one(head_pos, tail_pos)
    mover.linked.move_to(new_tail_pos)


class Head:

    def __init__(self, start_position=(0, 0)):
        self.start_position = start_position
        self.current_position = list(start_position)
        self.linked = None

    def add_linked(self, linked):
        self.linked = linked
        return linked

    def move(self, direction, steps):
        index = 1 if direction in ("U", "D") else 0
        sign = -1 if direction in ("D", "L") else 1

        for _ in range(steps):
            self.current_position[index] += sign
            self.attract_linked()

    def attract_linked(self):
        return _attract_linked(self)


class Mid:

    def __init__(self, start_position=(0, 0)):
        self.start_position = start_position
        self.current_position = start_position
        self.linked = None

    def add_linked(self, linked):
        self.linked = linked
        return linked

    def move_to(self, position):
        if position == self.current_position:
            return

        self.current_position = position
        self.attract_linked()

    def attract_linked(self):
        return _attract_linked(self)


class Tail:

    def __init__(self, start_position=(0, 0)):
        self.start_position = start_position

        self.visited_positions = [start_position]

    @property
    def current_position(self):
        return self.visited_positions[-1]

    def move_to(self, position):
        self.visited_positions.append(position)


if __name__ == "__main__":
    from _utils import load_data, move

    n_knots = 10

    filename = "input.dat"
    instructions = load_data(filename)

    last = head = Head()
    for _ in range(n_knots - 2):
        last = last.add_linked(Mid())
    tail = last.add_linked(Tail())

    move(head, instructions)

    answer = len(set(tail.visited_positions))
    question = "How many positions does the tail of the rope visit at least once?"

    print(f"{question} {answer}")
