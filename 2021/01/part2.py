
from _utils import load_data

filename = 'input.dat'
data = load_data(filename)


window_size = 3
n = len(data)

count = 0
for i in range(n - 1):
    sum_previous = sum(data[i:i + window_size])
    sum_cur = sum(data[i + 1:i + window_size + 1])

    if sum_cur > sum_previous:
        count += 1


print(f'How many sums are larger than the previous sum? {count}')
