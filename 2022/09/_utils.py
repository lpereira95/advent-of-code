
import numpy as np


def load_data(filename):
    with open(filename, "r") as file:
        instructions = []
        for line in file:
            direction, steps = line.strip().split(' ')
            instructions.append((direction, int(steps)))

        return instructions


def _get_abs_pos_difference(pos_a, pos_b):
    # manhattan
    return [abs(pos_a_i - pos_b_i) for pos_a_i, pos_b_i in zip(pos_a, pos_b)]


def _is_placed_diagonally(head_pos, tail_pos):
    return not(head_pos[0] == tail_pos[0] or head_pos[1] == tail_pos[1])


def _get_closer_by_one(head_pos, tail_pos):
    new_pos = list(tail_pos)
    for axis in range(2):
        dist = head_pos[axis] - new_pos[axis]
        if dist != 0:
            new_pos[axis] += np.sign(dist)

    return tuple(new_pos)


def move(head, instructions):
    for (direction, steps) in instructions:
        head.move(direction, steps)

    return head
