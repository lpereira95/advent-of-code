
from _utils import load_bin_numbers


def negate_bin(bin_number):
    # assumes number as string
    return bin_number.replace('1', '2').replace('0', '1').replace('2', '0')


filename = 'input.dat'
bin_numbers = load_bin_numbers(filename)

n_bins = len(bin_numbers)

count_ones = [0 for _ in bin_numbers[0]]
for bin_number in bin_numbers:
    for i, val in enumerate(bin_number):
        if val == '1':
            count_ones[i] += 1


gamma_rate = ''
for val in count_ones:
    if val >= n_bins / 2:
        gamma_rate += '1'
    else:
        gamma_rate += '0'

epsilon_rate = negate_bin(gamma_rate)

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(f"What is the power consumption of the submarine? {power_consumption}")
