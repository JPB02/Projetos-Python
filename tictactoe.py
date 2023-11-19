'''
#############################
#TIC-TAC-TOE				#
#Author: João Barbosa(JPB02)#
#############################
'''

import random as rd

# Global Variables
player_turn = rd.randint(1,2)
possible_coordinates = ['(0,0)','(1,1)','(2,2)','(0,1)','(0,2)','(1,0)','(1,2)','(2,0)','(2,1)']
play_matrix = [['~' for _ in range(3)] for _ in range(3)]

# Auxiliar Game Functions
def player_symbol():
	global player_turn
	if player_turn==1:
		return ('X')
	elif player_turn==2:
		return('O')

def next_turn():
	global player_turn
	if player_turn==1:
		player_turn=2
	else:
		player_turn=1

def draw_matrix():
    global play_matrix
    for row in play_matrix:
        formatted_row = ' | '.join(map(str, row))
        print(formatted_row)
        print('-' * (len(formatted_row) + 2))


def valid_move():
	global play_matrix
	for i in range(0,3):
		for j in range(0,3):
			if play_matrix[i][j] == '~':
				return True
	return False

def game_won():
	global play_matrix
	# Won by vertical line
	for i in range(0,3):
		if play_matrix[0][i] == play_matrix[1][i] == play_matrix[2][i] != '~' :
			return True

	# Won by horizontal line
	for j in range(0,3):
		if play_matrix[j][0] == play_matrix[j][1] == play_matrix[j][2] != '~' :
			return True

	# Won by diagonal line
	if play_matrix[0][0] == play_matrix[1][1] == play_matrix[2][2] != '~':
		return True
	if play_matrix[0][2] == play_matrix[1][1] == play_matrix[2][0] != '~':
		return True

	return False

# Start Game Function
def start_game():
	global play_matrix
	global player_turn
	global possible_coordinates
	print(f"Flipping a coin...\nPlayer {player_turn} starts first!")
	while valid_move():
		draw_matrix()
		i = input(f">> It's player {player_turn}'s turn. Select the coordinate of your play:\n")
		if i in possible_coordinates:
			play_matrix[int(i[1])][int(i[3])] = player_symbol()
			possible_coordinates.remove(i)
			if game_won():
				print(f"Player {player_turn} has won!")
				draw_matrix()
				break
			else:
				next_turn()
		else:
			print("That position has already been played, or isn't a valid move. Try again!")
			continue

start_game()
