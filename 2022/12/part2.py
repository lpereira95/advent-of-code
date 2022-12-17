
import networkx as nx

from _utils import (
    get_node_id,
    get_grid_shape,
    to_graph,
)


def find_lowest_elevations(grid):
    lowest_elevations = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 'a':
                lowest_elevations.append((i, j))

    return lowest_elevations


def _find_shortest_path(graph, init_pos, end_pos, grid_shape):
    source = get_node_id(*init_pos, grid_shape)
    target = get_node_id(*end_pos, grid_shape)
    return nx.shortest_path(graph, source=source, target=target)


def find_shortest_path(grid, end_pos):
    grid_shape = get_grid_shape(grid)

    graph = to_graph(new_grid)
    init_positions = find_lowest_elevations(grid)

    n_min_steps = 1e6
    for init_pos in init_positions:
        try:
            path = _find_shortest_path(graph, init_pos, end_pos, grid_shape)
        except nx.NetworkXNoPath:
            continue

        n_steps = len(path)
        if n_steps < n_min_steps:
            n_min_steps = n_steps

    return n_min_steps - 1


if __name__ == "__main__":
    from _utils import (
        load_data,
        get_initial_position,
        get_end_position,
        get_grid_with_no_special_pos,
    )

    filename = "input.dat"
    grid = load_data(filename)

    init_pos = get_initial_position(grid)
    end_pos = get_end_position(grid)

    new_grid = get_grid_with_no_special_pos(grid, init_pos, end_pos)

    answer = find_shortest_path(new_grid, end_pos)
    question = "What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?"

    print(f"{question} {answer}")
