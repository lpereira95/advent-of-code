

def count_overlaps(ranges):
    c = 0
    for pairs in ranges:
        c += is_overlapping(pairs)

    return c


def _pair_is_overlapped(pair_1, pair_2):
    return pair_1[0] <= pair_2[0] and pair_1[1] >= pair_2[0]


def is_overlapping(pairs):
    pair_1, pair_2 = pairs

    return _pair_is_overlapped(pair_1, pair_2) or _pair_is_overlapped(pair_2, pair_1)


if __name__ == "__main__":

    from _utils import load_data

    filename = "input.dat"
    ranges = load_data(filename)

    answer = count_overlaps(ranges)

    question = "In how many assignment pairs do the ranges overlap?"

    print(f"{question} {answer}")
