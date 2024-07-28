# 2048 project
# Se Yeon Bark

import random
import copy

# create a 4x4 game grid too store the surrent
# state of the game board. All values start 
# 0 then generate a single 2

board =[[0,0,0,0]
	   ,[0,0,0,0]
	   ,[0,0,0,0]
	   ,[0,0,0,0]]

Board_size = 4

def Display(board):
	#Pre: go through the list of board
	#Post: print the board with the '|' in front of the number 
	#		and number 0 will the replaced with a space.
	space = len(str(board[0][0]))
	for i in board:
		for n in i:
			if len(str(n)) > space:
				space = len(str(n))
				
	for index in board:
		Barrier = '|'
		for num in index:
			if num == 0:
				Barrier += ' '*space + '|'
			else: 
				Barrier += (' '*(space-len(str(num))))+str(num) + '|'
				
		print(Barrier)


#Display(board)
print()
def MergeRowLeft(row):
	#Pre: row will equal one row of our game board
	#Post: return row with everything moved <--
	
	# go through the row and move items to left
	# if there is a blank space. 
	
	for repeat in range(3):
		for item in range(3, 0, -1):
			if (row[item-1] == 0):
				row[item-1] = row[item]
				row[item] = 0
				
	# go through values and double if two adjacent
	# values are the same making the right value = 0
	for item in range(3):
		if row[item] == row[item+1]:
			row[item] *= 2
			row[item+1] = 0 
			
	# move left again to remove blanks again.
	for repeat in range(3):
		for item in range(3, 0, -1):
			if (row[item-1] == 0):
				row[item-1] = row[item]
				row[item] = 0
	return(row)
	
def WholeLeft (board):
# Move all of numbers in four rows to the left 
	for item in range(Board_size):
		board[item] = MergeRowLeft(board[item])
	return board

def Reverse (row):
	#Pre: go through the number in reverse so that the last # in the list
	#	 can be appended to an empty list
	#Post: append numbers in multi-dimensional list into an empty list.
	reverse = []
	for ele in range (Board_size-1, -1, -1):
		reverse.append(row[ele])

	return reverse

def WholeReverse (BoardNow):
	for item in range(Board_size):
		board[item] = Reverse(board[item])
	return board
def MergeRight (board):
	#Pre: go through the numbers in the board to merge to the left.
	#Post: reverse the merged numbers to the left to make them go to the right.
	for i in range (Board_size):
		board[i] = Reverse(board[i])
		board[i] = MergeRowLeft(board[i])
		board[i] = Reverse(board[i])
	return board


def Transpose (board):
	#Pre: 
	#Post:
	for i in range(Board_size):
		for j in range(i, Board_size):
			if i != j:
				trans = board[i][j]
				board[i][j] = board[j][i]
				board[j][i] = trans
			
	return board
	

def MergeUp (board):
	#Pre:
	#Post:
	board = Transpose(board)
	board = WholeLeft(board)
	board = Transpose(board)

	
	
	return board

	
def MergeDown (board):
	#Pre:
	#Post:
	
	board = Transpose(board)
	board = MergeRight(board)
	board = Transpose(board)

	
	return board

def NewValue():
	#Pre:
	#Post:
	if random.randint(1,8) == 1:
		return 4
	else:
		return 2

def AddNewValue(board):
	empty_spot = []
	for r in range(Board_size):
		for c in range(Board_size):
			if board[r][c] == 0:
				empty_spot.append((r,c))
	if empty_spot:
		r,c = random.choice(empty_spot)
		board[r][c] = NewValue()

def CanMove(board):
	# check if any empty spots are available
	for row in board:
		if 0 in row:
			return True
		
	
	# check for possible horizontal spots are available
	for row in board:
		for i in range(Board_size-1):
			if row[i] == row[i+1]:
				return True
			
	# check for possible vertical spots are available
	transposed = Transpose(board)
	for row in transposed:
		for j in range(Board_size-1):
			if row[j] == row[j+1]:
				return True
			
	return False

# Display two numbers randomly on the board
AddNewValue(board)
AddNewValue(board)
		
# Main game loop
game_won = False


while True:
	Display(board)

	if not CanMove(board):
		print("Game Over!")
		break
	
	if game_won:
		print("You win!")
		break
	
	Movement = input("Direction you would like to move: ")
	new_board = None

	# copy.deepcopy(board) = row[:] for row in board

	if Movement == 'w':
		new_board = MergeUp(copy.deepcopy(board))
		# [row[:] for row in board] => creates deep copy of the board when making a move
		# Deep copy keeps the original board unchanged during the move process 
	elif Movement == 's':
		new_board = MergeDown([row[:] for row in board])
	elif Movement == 'a':
		new_board = WholeLeft([row[:] for row in board])
	elif Movement == 'd':
		new_board = MergeRight([row[:] for row in board])

	if new_board != board:
		board = new_board
		AddNewValue(board)


	else:
		# Invalid move shows up when numbers can't add up although there is spaces left
		print()
		print("Invalid move")
	
	for a in range(Board_size):
		for b in range(Board_size):
			if board[a][b] == 2048:
				game_won = True
				break
		if game_won:
			break
		
	
		
