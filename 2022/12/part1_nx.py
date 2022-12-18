

if __name__ == "__main__":
    import networkx as nx
    from matplotlib import pyplot as plt

    from _utils import (
        load_data,
        get_initial_position,
        get_end_position,
        get_grid_with_no_special_pos,
        get_grid_shape,
    )
    from _utils_nx import (
        to_graph,
        get_node_id,
    )

    plot = False

    filename = "input.dat"
    grid = load_data(filename)

    init_pos = get_initial_position(grid)
    end_pos = get_end_position(grid)

    new_grid = get_grid_with_no_special_pos(grid, init_pos, end_pos)

    graph = to_graph(new_grid)

    if plot:
        nx.draw(graph)
        plt.show()

    grid_shape = get_grid_shape(grid)
    source = get_node_id(*init_pos, grid_shape)
    target = get_node_id(*end_pos, grid_shape)
    path = nx.shortest_path(graph, source=source, target=target)
    answer = len(path) - 1

    question = "What is the fewest steps required to move from your current position to the location that should get the best signal?"

    print(f"{question} {answer}")
