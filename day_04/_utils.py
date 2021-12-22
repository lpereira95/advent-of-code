

def load_data(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

    drawn_numbers = [int(number.strip()) for number in lines[0].split(',')]
    boards = []
    board = []
    for line in lines[2:]:
        if line.strip() == '':
            boards.append(board)
            board = []
            continue

        board.append([int(number.strip()) for number in line.strip().split()])
    boards.append(board)

    return drawn_numbers, boards


def compute_board_score(board, drawn_numbers, board_size=5):
    # returns also at which drawn it finishes
    board_state = [[0 for _ in range(board_size)] for _ in range(board_size)]

    for i, draw_number in enumerate(drawn_numbers):
        pos = check_number_in_board(board, draw_number)
        if pos is None:
            continue

        board_state[pos[0]][pos[1]] = 1
        if is_finished(board_state):
            return i, compute_finished_board_score(board, board_state, draw_number)

    return None, 0


def compute_finished_board_score(board, board_state, last_drawn_number):
    non_marked_sum = 0
    for board_row, state_row in zip(board, board_state):
        for value, state_value in zip(board_row, state_row):
            if state_value == 0:
                non_marked_sum += value

    return non_marked_sum * last_drawn_number


def check_number_in_board(board, number):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == number:
                return i, j

    return None


def is_finished(board_state):
    board_size = len(board_state)
    # check rows
    for row in board_state:
        if sum(row) == board_size:
            return True

    # check columns
    for j in range(board_size):
        s = sum(board_state[i][j] for i in range(board_size))
        if s == board_size:
            return True

    return False
