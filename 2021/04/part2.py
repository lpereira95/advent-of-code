
from _utils import load_data
from _utils import compute_board_score


filename = 'input.dat'
drawn_numbers, boards = load_data(filename)


board_scores = [compute_board_score(board, drawn_numbers) for board in boards]
finishing_orders = [value[0] for value in board_scores]
index_last = finishing_orders.index(max(finishing_orders))
score_last = board_scores[index_last][1]


print(f'Once it wins, what would its final score be? {score_last}')
