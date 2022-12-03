
from _utils import sum_priorities


def get_repeated_item(rucksack):
    for item in rucksack[0]:
        if item in rucksack[1]:
            return item

    raise ValueError("No repeated items")


def get_repeated_items(rucksacks):
    return [get_repeated_item(rucksack) for rucksack in rucksacks]


if __name__ == "__main__":
    from _utils import load_data

    filename = "input.dat"
    rucksacks = load_data(filename)

    repeated_items = get_repeated_items(rucksacks)
    answer = sum_priorities(repeated_items)

    question = "What is the sum of the priorities of those item types?"

    print(f"{question} {answer}")
