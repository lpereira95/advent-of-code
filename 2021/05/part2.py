
from _utils import read_lines
from _utils import count_overlaps
from _utils import count_number_points_overlap


filename = 'input.dat'
lines = read_lines(filename)

grid = count_overlaps(lines, only_parallel=False)
n_points_overlap = count_number_points_overlap(grid)

print(f'At how many points do at least two lines overlap? {n_points_overlap}')
