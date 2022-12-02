
from _utils import load_data
from _utils import compute_board_score


filename = 'input.dat'
drawn_numbers, boards = load_data(filename)


board_scores = [compute_board_score(board, drawn_numbers) for board in boards]
finishing_orders = [value[0] for value in board_scores]
index_first = finishing_orders.index(min(finishing_orders))
score_first = board_scores[index_first][1]


print(f'What will your final score be if you choose that board? {score_first}')
