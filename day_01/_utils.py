

def load_data(filename):

    with open(filename, 'r') as file:
        data = [int(line.strip()) for line in file]

    return data
