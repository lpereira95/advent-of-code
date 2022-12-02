
import copy


def load_grid(filename):
    with open(filename, 'r') as file:
        grid = [[int(val) for val in line.strip()] for line in file]

    return grid


def print_grid(grid):
    print(_get_grid_str(grid))


def get_grid_dims(grid):
    return len(grid), len(grid[0])


def _get_grid_vis(grid, path):
    grid_vis = copy.deepcopy(grid)
    for (i, j) in path:
        grid_vis[i][j] = '.'

    return grid_vis


def _get_grid_str(grid):
    rows = [''.join([str(val) for val in row]) for row in grid]
    return '\n'.join(rows)


def print_path(grid, path):
    grid_vis = _get_grid_vis(grid, path)

    print_grid(grid_vis)


def get_neighbors(i, j, dims):
    positions = ((1, 0), (0, 1), (0, -1), (-1, 0))
    neighbors = []
    for delta_i, delta_j in positions:
        neigh_i = i + delta_i
        neigh_j = j + delta_j
        if neigh_i >= 0 and neigh_j >= 0 and neigh_i < dims[0] and neigh_j < dims[1]:
            neighbors.append((neigh_i, neigh_j))

    return neighbors


def _initialize_dp_matrix(grid):

    return [[grid_val + (i + j) * 5 for j, grid_val in enumerate(row)]
            for i, row in enumerate(grid)]


def get_dp_matrix(grid):

    dims = get_grid_dims(grid)
    dp_matrix = _initialize_dp_matrix(grid)

    keep_going = True
    while keep_going:
        keep_going = False
        c = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i == j == 0:
                    continue

                previous = dp_matrix[i][j]
                neighs = get_neighbors(i, j, dims)
                dp_matrix[i][j] = val + min([dp_matrix[neigh_i][neigh_j]
                                             for (neigh_i, neigh_j) in neighs])
                if previous != dp_matrix[i][j]:
                    keep_going = True
                    c += 1

        print(c, dp_matrix[-1][-1])
        if previous == dp_matrix[i][j]:  # check last
            break

    return dp_matrix
