if __name__ == '__main__':

    from _utils import load_data

    filename = 'input.dat'
    data = load_data(filename)

    sorted_cal = sorted([sum(calories) for calories in data])

    print(sorted_cal[-3:])
    answer = sum(sorted_cal[-3:])

    question = "How many Calories are those Elves carrying in total?"
    print(f"{question} {answer}")
