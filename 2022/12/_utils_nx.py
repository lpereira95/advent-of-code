import math

import networkx as nx

from _utils import (
    get_grid_shape,
    get_valid_neighbors,
)


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
