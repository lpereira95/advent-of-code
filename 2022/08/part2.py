import numpy as np


def _get_n_visible_trees(grid):
    n_visible = np.zeros_like(grid)

    for i, row in enumerate(grid[1:-1]):
        for j, height in enumerate(row[1:-1]):
            for cmp_height in grid[i + 2:, j + 1]:
                n_visible[i + 1, j + 1] += 1
                if cmp_height >= height:
                    break

    return n_visible


def get_n_visible_trees_top(grid):
    return _get_n_visible_trees(grid)


def get_n_visible_trees_bottom(grid):
    n_visible_trees = _get_n_visible_trees(np.rot90(grid, k=2))
    return np.rot90(n_visible_trees, k=2)


def get_n_visible_trees_right(grid):
    n_visible_trees = _get_n_visible_trees(np.rot90(grid, k=1))
    return np.rot90(n_visible_trees, k=3)


def get_n_visible_trees_left(grid):
    n_visible_trees = _get_n_visible_trees(np.rot90(grid, k=3))
    return np.rot90(n_visible_trees, k=1)


def get_n_vibible_trees(grid):
    n_visible_trees_top = get_n_visible_trees_top(grid)
    n_visible_trees_bottom = get_n_visible_trees_bottom(grid)
    n_visible_trees_right = get_n_visible_trees_right(grid)
    n_visible_trees_left = get_n_visible_trees_left(grid)

    return np.stack([
        n_visible_trees_top,
        n_visible_trees_bottom,
        n_visible_trees_right,
        n_visible_trees_left
    ])


def get_scenic_score(n_visible_trees):
    return np.prod(n_visible_trees, axis=0)


if __name__ == "__main__":
    from _utils import load_data

    filename = "input.dat"
    grid = load_data(filename)

    n_visible_trees = get_n_vibible_trees(grid)

    answer = np.max(get_scenic_score(n_visible_trees))
    question = "What is the highest scenic score possible for any tree?"

    print(f"{question} {answer}")
