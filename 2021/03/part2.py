
from _utils import load_bin_numbers


def count_ones(bin_numbers, pos):
    c = 0
    for bin_number in bin_numbers:
        if bin_number[pos] == '1':
            c += 1

    return c


def filter_values(bin_numbers, pos, value):
    return [bin_number for bin_number in bin_numbers if bin_number[pos] == value]


def compute_rating(bin_numbers, bit_criteria, pos=0):
    n = len(bin_numbers)
    n_ones = count_ones(bin_numbers, pos)
    value = bit_criteria(n_ones, n)
    new_bin_numbers = filter_values(bin_numbers, pos, value)

    if len(new_bin_numbers) == 1:
        return new_bin_numbers[0]
    else:
        return compute_rating(new_bin_numbers, bit_criteria, pos + 1)


filename = 'input.dat'
bin_numbers = load_bin_numbers(filename)

bit_criteria_oxygen = lambda n_ones, n: '1' if n_ones >= n / 2 else '0'
bit_criteria_co2 = lambda n_ones, n: '0' if n_ones >= n / 2 else '1'


oxygen_rating = int(compute_rating(bin_numbers, bit_criteria_oxygen), 2)
co2_rating = int(compute_rating(bin_numbers, bit_criteria_co2), 2)
life_support_rating = oxygen_rating * co2_rating

print(f'What is the life support rating of the submarine? {life_support_rating}')
