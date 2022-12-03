
from _utils import (
    load_data,
    get_total_score,
    HandShape,
    OPPONENT_CODE,
    VICTORY,
    DRAW,
)


def get_round_score(round_):
    opp, me = round_
    opp_hand = HandShape(OPPONENT_CODE[opp])

    if me == "X":
        return opp_hand.wins_against().points

    if me == "Y":
        return opp_hand.points + DRAW

    return opp_hand.loses_against().points + VICTORY


filename = "input.dat"

rounds = load_data(filename)
answer = get_total_score(rounds, get_round_score)


question = (
    "What would your total score be if everything goes exactly according "
    "to your strategy guide?"
)
print(f"{question} {answer}")
