def load_data(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split() for line in file]

    return data


HAND_SHAPES = ["rock", "paper", "scissors"]
POINTS = {shape_type: pt for shape_type, pt in zip(HAND_SHAPES, (1, 2, 3))}

WINS_AGAINTS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",

}

OPPONENT_CODE = {letter: shape_type for letter, shape_type in zip("ABC", HAND_SHAPES)}

VICTORY = 6
DRAW = 3


class HandShape:

    def __init__(self, shape_type):
        self.shape_type = shape_type

    @property
    def points(self):
        return POINTS[self.shape_type]

    def play(self, other):
        if self.shape_type == other.shape_type:
            return 0

        if other.shape_type in WINS_AGAINTS[self.shape_type]:
            return 1

        return -1

    def loses_against(self):
        shape_type, = set(WINS_AGAINTS.keys()).difference(
            set([self.shape_type, WINS_AGAINTS[self.shape_type]])
        )
        return HandShape(shape_type)

    def wins_against(self):
        return HandShape(WINS_AGAINTS[self.shape_type])


def get_total_score(rounds, get_round_score):
    my_score = 0
    for round_ in rounds:
        my_score += get_round_score(round_)

    return my_score
