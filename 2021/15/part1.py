

from _utils import load_grid
from _utils import get_grid_dims
from _utils import print_path

# recursive solution, not efficient


def _get_neighbors(grid, i, j, positions):
    neighbors = []
    for delta_i, delta_j in positions:
        neigh_i = i + delta_i
        neigh_j = j + delta_j

        try:
            grid[neigh_i][neigh_j]
        except IndexError:
            continue

        if neigh_i >= 0 and neigh_j >= 0:
            neighbors.append((neigh_i, neigh_j))

    return neighbors


def get_neighbors(grid, i, j):
    positions = ((1, 0), (0, 1), (0, -1), (-1, 0))
    return _get_neighbors(grid, i, j, positions)


def get_neighbors_simplified(grid, i, j):
    positions = ((1, 0), (0, 1))
    return _get_neighbors(grid, i, j, positions)


def compute_path_risk(grid, path):
    return sum([grid[i][j] for (i, j) in path])


def insert_new_path(grid, paths, new_path):
    # if the current best route
    pos = new_path[-1]

    for path in paths.copy():
        if pos not in path:
            continue

        index = path.index(pos)
        new_path_risk = compute_path_risk(grid, new_path + path[index + 1:])
        path_risk = compute_path_risk(grid, path)
        if path_risk < new_path_risk:
            break
        else:
            paths.remove(path)
    else:
        paths.add(new_path)

    return paths


def find_shortest_path(grid, min_score_estimation=1e6, all_neighs=True):
    get_neighbors_fnc = get_neighbors if all_neighs else get_neighbors_simplified
    max_i, max_j = get_grid_dims(grid)

    paths = set((((0, 0),),))

    keep_going = True
    min_score = min_score_estimation
    while keep_going:
        for path in paths.copy():
            if path not in paths:
                continue

            i, j = path[-1]
            if i == max_i - 1 and j == max_j - 1:
                score = compute_path_risk(grid, path)
                if score < min_score:
                    min_score = score
                    print(f'new min_score: {min_score}')
                continue

            paths.remove(path)

            min_req = max_i - i + max_j - j - 2
            if compute_path_risk(grid, path) + min_req > min_score:
                continue

            neighbors = get_neighbors_fnc(grid, i, j)

            for neigh in neighbors:
                i, j = neigh

                if neigh in path:
                    continue

                new_path = path + (neigh,)

                paths = insert_new_path(grid, paths, new_path)

        for path in paths:
            if path[-1][0] != max_i - 1 or path[-1][1] != max_j - 1:
                break
        else:
            keep_going = False

    if len(paths) != 1:
        raise Exception(f'Something went wrong... {len(paths)} paths')

    return paths.pop()


def estimate_min_score(grid):
    path = find_shortest_path(grid, all_neighs=False)
    return compute_path_risk(grid, path)


if __name__ == '__main__':

    filename = 'input_example.dat'
    grid = load_grid(filename)

    min_score_est = estimate_min_score(grid)
    print(f'Score estimation: {min_score_est}')
    shortest_path = find_shortest_path(grid, min_score_estimation=min_score_est)

    print_path(grid, shortest_path)

    lowest_total_risk = compute_path_risk(grid, shortest_path) - grid[0][0]
    print(f'What is the lowest total risk of any path from the top left to the bottom right? {lowest_total_risk}')
