import string
import math

import networkx as nx


def get_grid_shape(grid):
    return len(grid), len(grid[0])


def load_data(filename):
    with open(filename, "r") as file:
        grid = []
        for line in file:
            grid.append(line.strip())

    return grid


def _get_position(grid, letter, position_name):
    for i, row in enumerate(grid):
        if letter in row:
            return i, row.index(letter)

    raise Exception("Cannot find {position_name}")


def get_initial_position(grid):
    return _get_position(grid, 'S', 'initial position')


def get_end_position(grid):
    return _get_position(grid, 'E', 'end position')


def cmp_values(value, cmp_value):
    index_value = string.ascii_lowercase.index(value)
    index_cmp_value = string.ascii_lowercase.index(cmp_value)

    if index_value >= index_cmp_value - 1:
        return True

    return False


def get_grid_with_no_special_pos(grid, initial_pos, end_pos):
    new_grid = grid.copy()

    i, _ = initial_pos
    new_grid[i] = new_grid[i].replace('S', 'a')

    i, _ = end_pos
    new_grid[i] = new_grid[i].replace('E', 'z')

    return new_grid


def get_valid_neighbors(grid, position, visited=()):
    i, j = position
    val = grid[i][j]

    neighbors = []

    grid_shape = get_grid_shape(grid)

    for (a, b) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        l, m = i + a, j + b
        if l < 0 or m < 0 or l >= grid_shape[0] or m >= grid_shape[1] or (l, m) in visited:
            continue

        cmp_val = grid[l][m]
        if cmp_values(val, cmp_val):
            neighbors.append((l, m))

    return neighbors


def get_node_id(i, j, grid_shape):
    return i * grid_shape[1] + j


def get_position_from_node_id(node_id, grid_shape):
    return node_id // grid_shape[1], node_id % grid_shape[1]


def to_graph(grid):
    grid_shape = get_grid_shape(grid)

    G = nx.DiGraph()
    G.add_nodes_from(range(math.prod(grid_shape)))

    edges = []
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            node_id = get_node_id(i, j, grid_shape)
            neighbors = get_valid_neighbors(grid, (i, j))

            for neighbor in neighbors:
                neighbor_id = get_node_id(*neighbor, grid_shape)
                edges.append([node_id, neighbor_id])

    G.add_edges_from(edges)

    return G
