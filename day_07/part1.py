
from _utils import load_data
from _utils import compute_fuel
from _utils import optimize


def compute_fuel_pos(x, pos):
    return abs(pos - x)


filename = 'input.dat'
positions = load_data(filename)

compute_fuel_linear = lambda x, positions, fnc_pos=compute_fuel_pos: compute_fuel(x, positions, fnc_pos=fnc_pos)
x = optimize(min(positions), max(positions), compute_fuel_linear, positions)
fuel = min([compute_fuel_linear(xx, positions) for xx in x])

print(f'How much fuel must they spend to align to that position? {fuel}')
