
def load_data(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split('-') for line in file]

    return data


def print_paths(paths):
    for path in paths:
        print(','.join(path))
