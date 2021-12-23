
def load_heightmap(filename):
    with open(filename, 'r') as file:
        heightmap = []
        for line in file:
            heightmap.append([int(value.strip()) for value in line.strip()])

    return heightmap


def get_neighbors_indices(i, j):
    indices = []
    for delta_x, delta_y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
        neigh_i = i + delta_x
        neigh_j = j + delta_y
        if neigh_i > -1 and neigh_j > -1:
            indices.append((neigh_i, neigh_j))

    return indices


def get_neighbors(i, j, heightmap):
    neighbors = []
    for (neigh_i, neigh_j) in get_neighbors_indices(i, j):

        try:
            neighbors.append(heightmap[neigh_i][neigh_j])
        except IndexError:
            pass

    return neighbors
