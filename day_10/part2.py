
from _utils import load_data
from _utils import get_opened_closed_chars
from _utils import get_pair

MAP_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def compute_incomplete_line_score(line):
    opened, closed = get_opened_closed_chars(line)
    if closed:
        return None

    score = 0
    for char in reversed(opened):
        score *= 5
        score += MAP_SCORE[get_pair(char)]

    return score


def compute_incomplete_scores(lines):
    scores = []
    for line in lines:
        score = compute_incomplete_line_score(line)
        if score:
            scores.append(score)

    return scores


filename = 'input.dat'
data = load_data(filename)

scores = compute_incomplete_scores(data)
sorted_scores = sorted(scores)

middle_score = sorted_scores[len(scores) // 2]
print(f'What is the middle score? {middle_score}')
