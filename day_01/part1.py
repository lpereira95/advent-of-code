
from _utils import load_data

filename = 'input.dat'
data = load_data(filename)


count = 0
for previous_value, cur_value in zip(data, data[1:]):
    if cur_value > previous_value:
        count += 1

print(f'How many measurements are larger than the previous measurement? {count}')
