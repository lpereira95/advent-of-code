

OPEN_SYMBOLS = ['(', '[', '{', '<']

CLOSED_SYMBOLS = [')', ']', '}', '>']


def load_data(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    return lines


def get_pair(char):
    try:
        index = OPEN_SYMBOLS.index(char)
        return CLOSED_SYMBOLS[index]
    except ValueError:
        index = CLOSED_SYMBOLS.index(char)
        return OPEN_SYMBOLS[index]


def is_open_char(char):
    try:
        OPEN_SYMBOLS.index(char)
        return True
    except ValueError:
        return False


def get_opened_closed_chars(line):
    opened = []
    closed = []
    for char in line:
        if is_open_char(char):
            opened.append(char)
        else:
            pair = get_pair(char)
            if opened and opened[-1] == pair:
                opened.pop()
            else:
                closed.append(char)

    return opened, closed
