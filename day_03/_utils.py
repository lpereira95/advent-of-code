
def load_bin_numbers(filename):
    with open(filename, 'r') as file:
        bin_numbers = [line.strip() for line in file]

    return bin_numbers
