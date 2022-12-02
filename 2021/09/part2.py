
from _utils import load_heightmap
from _utils import get_neighbors
from _utils import get_neighbors_indices


def get_low_points_loc(heightmap):
    low_points_loc = []
    for i, row in enumerate(heightmap):
        for j, val in enumerate(row):
            neighbors = get_neighbors(i, j, heightmap)
            if min(neighbors) > val:
                low_points_loc.append((i, j))

    return low_points_loc


def get_basin(heightmap, point_loc, basin_points=None):

    if basin_points is None:
        basin_points = []

    try:
        value = heightmap[point_loc[0]][point_loc[1]]
    except IndexError:
        return basin_points

    if value == 9 or point_loc in basin_points:
        return basin_points

    basin_points.append(point_loc)

    for neighbor_indices in get_neighbors_indices(point_loc[0], point_loc[1]):
        basin_points = get_basin(heightmap, neighbor_indices, basin_points)

    return basin_points


filename = 'input.dat'
heightmap = load_heightmap(filename)

low_points_loc = get_low_points_loc(heightmap)

basins = [get_basin(heightmap, low_point_loc) for low_point_loc in low_points_loc]

basin_sizes = sorted([len(basin) for basin in basins])

sizes_prod = 1
for basin_size in basin_sizes[-3:]:
    sizes_prod *= basin_size

print(f'What do you get if you multiply together the sizes of the three largest basins? {sizes_prod}')
