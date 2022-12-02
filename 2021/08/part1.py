
from _utils import load_data
from _utils import count_uniques


filename = 'input.dat'
unique_signal_patterns, output_values = load_data(filename)


counts = count_uniques(output_values)


print(f'In the output values, how many times do digits 1, 4, 7, or 8 appear? {counts}')
