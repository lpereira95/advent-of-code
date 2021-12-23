
from _utils import load_data
from _utils import get_opened_closed_chars

MAP_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def compute_corrupted_line_score(line):
    _, closed = get_opened_closed_chars(line)
    if closed:
        return MAP_SCORE[closed[0]]

    return 0


def compute_corrupted_score(lines):
    scores = [compute_corrupted_line_score(line) for line in lines]
    return sum(scores)


filename = 'input.dat'
data = load_data(filename)

score = compute_corrupted_score(data)

print(f'What is the total syntax error score for those errors? {score}')
