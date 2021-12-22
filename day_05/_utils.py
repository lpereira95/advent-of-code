
def read_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            left, right = line.split('->')
            pt_left = [int(val.strip()) for val in left.strip().split(',')]
            pt_right = [int(val.strip()) for val in right.strip().split(',')]

            lines.append((pt_left, pt_right))

    return lines


def is_horizontal(pt_left, pt_right):
    return pt_left[0] == pt_right[0]


def is_vertical(pt_left, pt_right):
    return pt_left[1] == pt_right[1]


def get_grid_dimensions(grid):
    if len(grid):
        return len(grid), len(grid[0])
    return 0, 0


def _increase_grid_size(grid, new_grid_dims):

    # extend columns
    for row in grid:
        row += [0 for _ in range(new_grid_dims[1] - len(row))]

    # extend rows
    for _ in range(new_grid_dims[0] - len(grid)):
        grid.append([0 for _ in range(new_grid_dims[1])])

    return grid


def _get_covered_points_parallel(pt_left, pt_right, axis):
    pt_min = pt_left if pt_left[axis] < pt_right[axis] else pt_right
    pt_max = pt_right if pt_min is pt_left else pt_left

    covered_points = []
    other_coord = pt_min[not axis]
    for coord in range(pt_min[axis], pt_max[axis] + 1):
        pt = [None, None]
        pt[axis] = coord
        pt[not axis] = other_coord

        covered_points.append(pt)

    return covered_points


def _get_covered_points_diagonal(pt_left, pt_right):
    # assumes 45 degrees
    unit_x = 1 if pt_left[0] < pt_right[0] else -1
    unit_y = 1 if pt_left[1] < pt_right[1] else -1

    covered_points = [pt_left]
    while True:
        point = (covered_points[-1][0] + unit_x, covered_points[-1][1] + unit_y)
        covered_points.append(point)
        if point[0] == pt_right[0] and point[1] == pt_right[1]:
            return covered_points


def get_covered_points(line, only_parallel=True):
    if is_horizontal(line[0], line[1]):
        return _get_covered_points_parallel(line[0], line[1], 1)

    elif is_vertical(line[0], line[1]):
        return _get_covered_points_parallel(line[0], line[1], 0)

    elif only_parallel:  # do not consider diagonals
        return []

    else:
        return _get_covered_points_diagonal(line[0], line[1])


def update_grid(grid, covered_points):
    if not covered_points:
        return grid

    # check dimensions
    grid_size = get_grid_dimensions(grid)
    larger_point = (max(pt[0] for pt in covered_points), max(pt[1] for pt in covered_points))
    if grid_size[0] < (larger_point[1] + 1) or grid_size[1] < (larger_point[0] + 1):
        new_dims = max(grid_size[0], larger_point[1] + 1), max(grid_size[1], larger_point[0] + 1)
        grid = _increase_grid_size(grid, new_dims)

    # update grid
    for point in covered_points:
        grid[point[1]][point[0]] += 1

    return grid


def count_overlaps(lines, only_parallel=True):
    grid = []
    for line in lines:
        covered_points = get_covered_points(line, only_parallel)
        grid = update_grid(grid, covered_points)

    return grid


def count_number_points_overlap(grid, threshold=1):
    count = 0
    for row in grid:
        for val in row:
            if val > threshold:
                count += 1

    return count
