
import copy


from _utils import load_grid
from _utils import print_grid
from _utils import get_grid_dims
from _utils import get_dp_matrix


def _repeat_grid_horizontally(grid, k):
    dims = get_grid_dims(grid)
    new_dims = dims[0], dims[1] * k

    new_grid = []
    for i in range(new_dims[0]):
        row = grid[i].copy()
        for j in range(dims[1], new_dims[1]):
            local_j = j % dims[1]
            val = (grid[i][local_j] + 1 * (j // dims[1])) % 9
            if val == 0:
                val = 9
            row.append(val)

        new_grid.append(row)

    return new_grid


def _repeat_grid_vertically(grid, k):
    dims = get_grid_dims(grid)
    new_dims = dims[0] * k, dims[1]

    new_grid = copy.deepcopy(grid)
    for i in range(dims[0], new_dims[0]):
        row = []
        for j in range(new_dims[1]):
            local_i = i % dims[0]
            val = (grid[local_i][j] + 1 * (i // dims[0])) % 9
            if val == 0:
                val = 9
            row.append(val)

        new_grid.append(row)

    return new_grid


def repeat_grid(grid, k=2):
    new_grid = _repeat_grid_horizontally(grid, k)
    return _repeat_grid_vertically(new_grid, k)


if __name__ == '__main__':

    filename = 'input.dat'
    init_grid = load_grid(filename)
    grid = repeat_grid(init_grid, k=5)

    dp_matrix = get_dp_matrix(grid)

    lowest_total_risk = dp_matrix[-1][-1] - grid[0][0]
    print(f'What is the lowest total risk of any path from the top left to the bottom right? {lowest_total_risk}')
