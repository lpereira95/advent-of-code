
def load_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [int(value.strip()) for value in data[0].strip().split(',')]


def compute_fuel(x, positions, fnc_pos):
    return sum(fnc_pos(x, x_i) for x_i in positions)


def optimize(left, right, fnc, positions):
    # very naive strategy (similar to bisection)
    if (right - left) < 2:
        return left, right

    c = (left + right) // 2

    left_c = (left + c) // 2
    val_left_c = fnc(left_c, positions)

    right_c = (right + c) // 2
    val_right_c = fnc(right_c, positions)

    if val_left_c < val_right_c:
        right = c
    else:
        left = c

    return optimize(left, right, fnc, positions)
