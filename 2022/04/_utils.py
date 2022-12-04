def _transform_pair(pair):
    left, right = pair.split('-')
    return int(left), int(right)


def load_data(filename):
    with open(filename, "r") as file:
        ranges = []
        for line in file:
            pair_1, pair_2 = line.strip().split(",")
            ranges.append([_transform_pair(pair_1), _transform_pair(pair_2)])

    return ranges
