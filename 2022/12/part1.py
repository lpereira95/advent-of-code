from _utils import get_valid_neighbors


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


if __name__ == "__main__":
    from _utils import (
        load_data,
        get_initial_position,
        get_end_position,
        get_grid_with_no_special_pos,
    )

    naive = False
    plot = False

    filename = "input.dat"
    grid = load_data(filename)

    init_pos = get_initial_position(grid)
    end_pos = get_end_position(grid)

    new_grid = get_grid_with_no_special_pos(grid, init_pos, end_pos)

    if naive:
        path = navigate(new_grid, init_pos, end_pos)

    else:
        import networkx as nx
        from _utils import to_graph, get_node_id, get_grid_shape

        graph = to_graph(new_grid)

        if plot:
            import matplotlib.pyplot as plt

            nx.draw(graph)
            plt.show()

        grid_shape = get_grid_shape(grid)
        source = get_node_id(*init_pos, grid_shape)
        target = get_node_id(*end_pos, grid_shape)
        path = nx.shortest_path(graph, source=source, target=target)

    answer = len(path) - 1
    question = "What is the fewest steps required to move from your current position to the location that should get the best signal?"

    print(f"{question} {answer}")
