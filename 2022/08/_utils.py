
import numpy as np


def load_data(filename):
    with open(filename, "r") as file:
        grid = []
        for line in file:
            row = [int(height) for height in line.strip()]
            grid.append(row)

    return np.array(grid)
