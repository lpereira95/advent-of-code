class Monkey:

    def __init__(self, id_, starting_items, operation, divisible_by,
                 receiving_monkeys):
        self.id = id_
        self.items = starting_items

        self.operate_on_item = operation
        self.divisible_by = divisible_by

        self.receiving_monkeys = {
            True: receiving_monkeys[0],
            False: receiving_monkeys[1],
        }

        self.n_inspecs = 0

    def update_receiving_monkeys(self, monkeys):
        for key, monkey_id in self.receiving_monkeys.items():
            self.receiving_monkeys[key] = monkeys[int(monkey_id)]

    def decrease_human_worry_level(self, item):
        return item // 3

    def play(self):
        while len(self.items):
            self.n_inspecs += 1
            item = self.operate_on_item(self.items.pop(0))
            item = self.decrease_human_worry_level(item)
            self.throw_item(item)

    def test_item(self, item):
        val = item / self.divisible_by
        return int(val) == val

    def throw_item(self, item):
        self.receiving_monkeys[self.test_item(item)].receive_item(item)

    def receive_item(self, item):
        self.items = [item] + self.items


if __name__ == "__main__":
    from _utils import (
        load_data,
        get_most_active_monkeys,
        multiply_activity,
        play,
    )

    n_rounds = 20
    filename = "input.dat"

    monkeys = load_data(filename, Monkey)

    play(monkeys, n_rounds)
    most_active_monkeys = get_most_active_monkeys(monkeys)

    answer = multiply_activity(most_active_monkeys)
    question = f"What is the level of monkey business after {n_rounds} rounds of stuff-slinging simian shenanigans?"

    print(f"{question} {answer}")
