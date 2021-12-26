
from _utils import load_data
from _utils import fold_grid

filename = 'input.dat'
grid, instructions = load_data(filename)


for instruction in instructions[:1]:
    grid = fold_grid(grid, instruction)


n_dots = len(grid)

print(f'How many dots are visible after completing just the first fold instruction on your transparent paper? {n_dots}')
