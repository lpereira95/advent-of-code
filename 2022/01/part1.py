
if __name__ == '__main__':

    from _utils import load_data

    filename = 'input.dat'
    data = load_data(filename)

    answer = max([sum(calories) for calories in data])

    question = "How many total Calories is that Elf carrying?"
    print(f"{question} {answer}")
