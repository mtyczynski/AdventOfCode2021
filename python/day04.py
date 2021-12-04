from aoc import read_input, mapl
import numpy as np

def IsBingo(card):
    for i in range(5):
        row_zeros=np.count_nonzero(card[i,:])
        col_zeros=np.count_nonzero(card[:,i])
        if not row_zeros or not col_zeros:
            return True
    return False

numbers = read_input(4)
input_numbers = np.array(mapl(int, numbers[0].split(",")))
input_numbers[input_numbers == 0] = -1

boards_raw = list(filter(lambda x: x != "", numbers))[1:]
board = [x.split() for x in boards_raw]

board = np.array(board).reshape((-1,5,5)).astype(int)
board = np.where(board == 0, -1, board)
stop = False
first_found = False

for num in input_numbers:
    if stop: break
    board = np.where(board == num, 0, board)
    for i in range(board.shape[0]):
        if i >= board.shape[0]: break
        bingo_found = IsBingo(board[i,:,:])
        if bingo_found:
            if not first_found:
                print(f"part1: {board[i,:,:].sum()*num}")
                first_found = True
            if board.shape[0] > 1:
                board = np.delete(board, i, 0)
            else:
                marked_sum = board[i,:,:].sum()
                print(f"part2: {marked_sum*num}")
                stop = True
                break
