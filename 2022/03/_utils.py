import string


def load_data(filename):
    with open(filename, 'r') as file:
        rucksacks = []
        for line in file:
            items = line.strip()
            half = len(items) // 2
            rucksacks.append(
                [items[:half], items[half:]]
            )

    return rucksacks


def sum_priorities(items):
    return sum([get_priority(item) for item in items])


def get_priority(item):
    item_ = item.lower()
    priority = string.ascii_lowercase.index(item_) + 1

    if item.isupper():
        return priority + 26

    return priority
