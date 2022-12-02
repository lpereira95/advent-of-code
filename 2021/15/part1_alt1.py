
import copy

from _utils import load_grid
from _utils import get_grid_dims
from _utils import get_dp_matrix

# dynamic programming based solution

if __name__ == '__main__':

    filename = 'input_example.dat'
    grid = load_grid(filename)

    dp_matrix = get_dp_matrix(grid)

    lowest_total_risk = dp_matrix[-1][-1] - grid[0][0]
    print(f'What is the lowest total risk of any path from the top left to the bottom right? {lowest_total_risk}')
