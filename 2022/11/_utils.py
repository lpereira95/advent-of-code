import re
import math


def plus(a, b):
    return a + b


def times(a, b):
    return a * b


MAP_OPERATORS = {'+': plus, '*': times}


MONKEY_REGEX = re.compile(
    r"Monkey (\d+):.+?items: ([\d, ]+){1}?  Op.+?new = (\w+) ([*+]{1}) (\w+).+?by (\d+).+?monkey (\d+).+?monkey (\d+)"
)


def create_monkey(monkey_info, Monkey):
    # monkey_info: result of regexp
    (
        id_, starting_items, left, op, right, divisible_by, *receiving_monkeys
    ) = monkey_info

    starting_items = [int(item.strip()) for item in starting_items.split(',')]
    operation = create_operation(left, op, right)
    return Monkey(id_, starting_items, operation, int(divisible_by), receiving_monkeys)


def _manipulate_old(value, item):
    if value == "old":
        return item

    return int(value)


def create_operation(left, op, right):
    op = MAP_OPERATORS[op]

    def operation(item):
        a = _manipulate_old(left, item)
        b = _manipulate_old(right, item)
        return op(a, b)

    return operation


def load_data(filename, Monkey):
    with open(filename, "r") as file:
        monkeys_info = MONKEY_REGEX.findall(file.read().replace('\n', ''))

        monkeys = [create_monkey(monkey_info, Monkey) for monkey_info in monkeys_info]
        for monkey in monkeys:
            monkey.update_receiving_monkeys(monkeys)

    return monkeys


def play(monkeys, n_rounds):
    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.play()


def get_most_active_monkeys(monkeys, n=2):
    return sorted(monkeys, key=lambda x: x.n_inspecs)[-n:]


def multiply_activity(monkeys):
    return math.prod(monkey.n_inspecs for monkey in monkeys)
