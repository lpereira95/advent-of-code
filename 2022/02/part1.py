
from _utils import (
    HandShape,
    HAND_SHAPES,
    OPPONENT_CODE,
    VICTORY,
    DRAW,
)


MY_CODE = {letter: shape_type for letter, shape_type in zip("XYZ", HAND_SHAPES)}


def get_round_score(round_):
    opp, me = round_
    opp_hand, me_hand = HandShape(OPPONENT_CODE[opp]), HandShape(MY_CODE[me])

    my_score = me_hand.points

    round_res = me_hand.play(opp_hand)
    if round_res > 0:
        my_score += VICTORY

    elif round_res == 0:
        my_score += DRAW

    return my_score


if __name__ == '__main__':
    from _utils import (
        load_data,
        get_total_score,
    )

    filename = "input.dat"

    rounds = load_data(filename)
    answer = get_total_score(rounds, get_round_score)

    question = (
        "What would your total score be if everything goes exactly according "
        "to your strategy guide?"
    )
    print(f"{question} {answer}")
