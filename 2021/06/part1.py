
from _utils import load_data


def update_state(state, time_to_reproduce=6, infancy_time=2):
    new_state = state.copy()
    n_new_fishes = 0
    for i, fish_state in enumerate(new_state):
        if fish_state == 0:
            n_new_fishes += 1
            new_state[i] = time_to_reproduce
        else:
            new_state[i] -= 1

    new_state.extend([time_to_reproduce + infancy_time for _ in range(n_new_fishes)])

    return new_state


def simulate(state, n_days, time_to_reproduce=6, infancy_time=2):
    for _ in range(n_days):
        state = update_state(state, time_to_reproduce, infancy_time)

    return state


filename = 'input.dat'
initial_state = load_data(filename)

n_days = 80
state = simulate(initial_state, n_days)
n_fish = len(state)

print(f'How many lanternfish would there be after {n_days} days? {n_fish}')
