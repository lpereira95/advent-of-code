import numpy as np


def _get_visibility(grid):
    visibility = np.ones_like(grid, dtype=bool)
    max_values = grid[0, 1:-1]
    for i, row in enumerate(grid[1:-1]):
        for j, height in enumerate(row[1:-1]):
            if height <= max_values[j]:
                visibility[i + 1, j + 1] = False
            else:
                max_values[j] = height

    return visibility


def get_visibility_top(grid):
    return _get_visibility(grid)


def get_visibility_bottom(grid):
    visibility = _get_visibility(np.rot90(grid, k=2))
    return np.rot90(visibility, k=2)


def get_visibility_right(grid):
    visibility = _get_visibility(np.rot90(grid, k=1))
    return np.rot90(visibility, k=3)


def get_visibility_left(grid):
    visibility = _get_visibility(np.rot90(grid, k=3))
    return np.rot90(visibility, k=1)


def get_visibility(grid):
    visibility_top = get_visibility_top(grid)
    visibility_bottom = get_visibility_bottom(grid)
    visibility_right = get_visibility_right(grid)
    visibility_left = get_visibility_left(grid)

    visibility = (
        visibility_top | visibility_bottom | visibility_left | visibility_right
    )

    return visibility


def count_visible(visibility):
    return np.sum(visibility)


if __name__ == "__main__":
    from _utils import load_data

    filename = "input.dat"
    grid = load_data(filename)
    visibility = get_visibility(grid)

    answer = count_visible(visibility)
    question = "How many trees are visible from outside the grid?"

    print(f"{question} {answer}")
