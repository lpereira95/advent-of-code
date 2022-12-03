
from _utils import sum_priorities


def get_repeated_items(rucksacks):
    items = []

    group_rucksacks = []
    for rucksack in rucksacks:
        group_rucksacks.append(rucksack)

        if len(group_rucksacks) == 3:
            items.append(get_repeated_item(group_rucksacks))
            group_rucksacks = []

    return items


def get_repeated_item(group_rucksacks):
    rucksacks = []
    for elf_rucksack in group_rucksacks:
        rucksacks.append(elf_rucksack[0] + elf_rucksack[1])

    elf_rucksack = rucksacks[0]
    for item in elf_rucksack:
        for other_rucksack in rucksacks[1:]:
            if item not in other_rucksack:
                break
        else:
            return item

    raise ValueError("Ups... lost badges?")


if __name__ == "__main__":
    from _utils import load_data

    filename = "input.dat"
    rucksacks = load_data(filename)

    repeated_items = get_repeated_items(rucksacks)

    answer = sum_priorities(repeated_items)

    question = "What is the sum of the priorities of those item types?"

    print(f"{question} {answer}")
