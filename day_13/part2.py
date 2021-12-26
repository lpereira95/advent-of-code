
from _utils import load_data
from _utils import fold_grid

filename = 'input.dat'
grid, instructions = load_data(filename)


for instruction in instructions:
    grid = fold_grid(grid, instruction)


max_x, max_y = 0, 0
for values in grid:
    if values[0] > max_x:
        max_x = values[0]
    if values[1] > max_y:
        max_y = values[1]


print(f'What code do you use to activate the infrared thermal imaging camera system?')

vis_grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for coord in grid:
    i, j = coord
    vis_grid[j][i] = '#'

for row in vis_grid:
    print(''.join(row))
