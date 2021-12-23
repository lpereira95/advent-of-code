
from _utils import load_heightmap
from _utils import get_neighbors


def get_low_points(heightmap):
    low_points = []
    for i, row in enumerate(heightmap):
        for j, val in enumerate(row):
            neighbors = get_neighbors(i, j, heightmap)
            if min(neighbors) > val:
                low_points.append(val)

    return low_points


def get_risk_level_sum(low_points):
    return sum(val + 1 for val in low_points)


filename = 'input.dat'
heightmap = load_heightmap(filename)

risk_levels_sum = get_risk_level_sum(get_low_points(heightmap))
print(f'What is the sum of the risk levels of all low points on your heightmap? {risk_levels_sum}')
