
from _utils import load_grid
from _utils import print_grid
from _utils import simulate_step


def simulate(grid, n_steps, verbose=1):
    total_flashes = 0
    if verbose:
        print('Before any steps:')
        print_grid(grid)

    for step in range(n_steps):
        grid, total_flashes_ = simulate_step(grid)
        total_flashes += total_flashes_

        if verbose:
            print(f'\nAfter step {step+1}:')
            print_grid(grid)

    return grid, total_flashes


filename = 'input.dat'
grid = load_grid(filename)
n_steps = 100


grid, total_flashes = simulate(grid, n_steps, verbose=False)


print(f'How many total flashes are there after 100 steps? {total_flashes}')
