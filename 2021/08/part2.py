
from _utils import load_data
from _utils import decode_patterns


filename = 'input.dat'
unique_signal_patterns, output_values = load_data(filename)

sum_ = 0
for unique_signal_patterns_, output_values_ in zip(unique_signal_patterns, output_values):
    num = decode_patterns(unique_signal_patterns_, output_values_)
    sum_ += int(num)

print(f'What do you get if you add up all of the output values? {sum_}')
