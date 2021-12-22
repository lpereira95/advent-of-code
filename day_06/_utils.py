
def load_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [int(value.strip()) for value in data[0].strip().split(',')]
