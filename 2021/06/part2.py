
from _utils import load_data


def update_grouped_state(grouped_state, time_to_reproduce=6):
    new_grouped_state = grouped_state.copy()
    new_borns = new_grouped_state[0]
    for i, group in enumerate(new_grouped_state[1:]):
        new_grouped_state[i] = group
    new_grouped_state[-1] = new_borns
    new_grouped_state[time_to_reproduce] += new_borns

    return new_grouped_state


def simulate(state, n_days, time_to_reproduce=6, infancy_time=2):
    n_periods = time_to_reproduce + infancy_time + 1
    grouped_state = [initial_state.count(i) for i in range(n_periods)]

    for _ in range(n_days):
        grouped_state = update_grouped_state(grouped_state, time_to_reproduce)

    return grouped_state


filename = 'input.dat'
initial_state = load_data(filename)

n_days = 256
grouped_state = simulate(initial_state, n_days)
n_fish = sum(grouped_state)

print(f'How many lanternfish would there be after {n_days} days? {n_fish}')
