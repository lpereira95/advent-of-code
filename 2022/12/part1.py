from _utils import get_valid_neighbors, get_grid_shape


def navigate(grid, initial_pos, end_pos):
    # naive implementation
    stack = [[initial_pos]]
    possible_paths = []

    min_n_steps = 1e6

    while len(stack) > 0:
        last_path = stack.pop()
        neighbors = get_valid_neighbors(grid, last_path[-1], last_path)

        if len(neighbors) == 0:
            continue

        if end_pos in neighbors:
            n_steps = len(last_path)
            if n_steps < min_n_steps:
                min_n_steps = n_steps

            possible_paths.append(last_path.copy() + [end_pos])
            continue

        for neighbor in neighbors:
            n_steps = len(last_path)
            if n_steps > min_n_steps:
                continue

            leave = False
            for path in stack:
                if neighbor in path:
                    if n_steps > path.index(neighbor):
                        leave = True
                    else:
                        stack.remove(path)
            if leave:
                break

            stack.append(last_path.copy() + [neighbor])

    sorted_possible_paths = sorted(possible_paths, key=lambda x: len(x))
    return sorted_possible_paths[0]


def _get_init_costs(grid):
    grid_shape = get_grid_shape(grid)
    costs = {}
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            costs[(i, j)] = None

    return costs


def navigate2(grid, initial_pos, end_pos):
    costs = _get_init_costs(grid)
    costs[initial_pos] = 0

    new_positions = [initial_pos]
    while costs[end_pos] is None:

        next_positions = []
        for pos in new_positions:
            neighbors = get_valid_neighbors(grid, pos)
            for neigh in neighbors:
                if costs[neigh] is None:
                    next_positions.append(neigh)
                    costs[neigh] = costs[pos] + 1

        new_positions = next_positions
    return costs[end_pos]


if __name__ == "__main__":
    from _utils import (
        load_data,
        get_initial_position,
        get_end_position,
        get_grid_with_no_special_pos,
    )

    impl = 1  # 0 : naive; 1 : less naive
    plot = False  # only with networkx

    filename = "input.dat"
    grid = load_data(filename)

    init_pos = get_initial_position(grid)
    end_pos = get_end_position(grid)

    new_grid = get_grid_with_no_special_pos(grid, init_pos, end_pos)

    if impl == 0:
        path = navigate(new_grid, init_pos, end_pos)
        answer = len(path - 1)

    if impl == 1:
        answer = navigate2(new_grid, init_pos, end_pos)

    question = "What is the fewest steps required to move from your current position to the location that should get the best signal?"

    print(f"{question} {answer}")
