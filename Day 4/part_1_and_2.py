#!/usr/bin/env python

from board import Board

sequence = [93,18,74,26,98,52,94,23,15,2,34,75,13,31,39,76,96,16,84,12,38,27,8,85,86,43,4,79,57,19,40,59,14,21,35,0,90,11,32,17,78,83,54,42,66,82,99,45,55,63,24,5,89,46,80,49,3,48,67,47,50,60,81,51,71,33,72,6,9,30,56,20,77,29,28,69,25,36,91,92,65,22,62,58,64,88,10,7,87,41,44,37,73,70,68,97,61,95,53,1]

boards = []

def play_board(board):
    for current_number in sequence:
        board.plot_number(current_number)

        if board.has_won():
            board.calculate_score()
            break

# Gets the boards from data.txt and plays
with open('data.txt', 'r') as file:
    board_numbers = []

    for line in file.readlines():
        if line.strip() != '':
            # Creates the numbers for the board
            for number in line.replace('\n', '').split():
                board_numbers.append(number)
        else:
            board = Board(board_numbers)
            boards.append(board)

            board_numbers.clear()

            play_board(board)

# Sorts the board with the least moves 
boards = sorted(boards, key=lambda board: board.moves)

# Output
print('-------------------- Least Moves --------------------')
print('Moves: {} \nScore: {}'.format(boards[0].moves, boards[0].score))
boards[0].display()

print('-------------------- Most Moves --------------------')
print('Moves: {} \nScore: {}'.format(boards[-1].moves, boards[-1].score))
boards[-1].display()