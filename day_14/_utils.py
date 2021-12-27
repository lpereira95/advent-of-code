
def load_data(filename):
    with open(filename, 'r') as file:
        template = file.readline().strip()
        file.readline()

        rules = {}
        for line in file:
            key, value = line.strip().split(' -> ')
            rules[key] = value

    return template, rules
