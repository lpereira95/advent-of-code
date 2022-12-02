def load_data(filename):
    with open(filename, 'r') as file:
        elf_calories = []
        calories = []
        for line in file:
            if line.strip() == "":
                elf_calories.append(calories)
                calories = []
                continue

            calories.append(int(line.strip()))

        if calories:
            elf_calories.append(calories)

    return elf_calories
