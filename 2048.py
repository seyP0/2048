# 2048 project

import random

# create a 4x4 game grid too store the surrent
# state of the game board. All values start 
# 0 then generate a single 2

board =[[0,2,2,2]
	   ,[2,2,0,2]
	   ,[4,0,0,4]
	   ,[2,2,0,0]]

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
def MergeRight (BoardNow):
	#Pre: go through the numbers in the board to merge to the left.
	#Post: reverse the merged numbers to the left to make them go to the right.
	for i in range (Board_size):
		BoardNow[i] = Reverse(BoardNow[i])
		BoardNow[i] = MergeRowLeft(BoardNow[i])
		BoardNow[i] = Reverse(BoardNow[i])
	return BoardNow


def Transpose (BoardNow):
	#Pre: 
	#Post:
	for i in range(Board_size):
		for j in range(i, Board_size):
			if not i == j:
				trans = BoardNow[i][j]
				BoardNow[i][j] = BoardNow[j][i]
				BoardNow[j][i] = trans
			
	return BoardNow
	

def MergeUp (BoardNow):
	#Pre:
	#Post:
	BoardNow = Transpose(BoardNow)
	BoardNow = WholeLeft(BoardNow)
	BoardNow = Transpose(BoardNow)
	
	return BoardNow

	
def MergeDown (BoardNow):
	#Pre:
	#Post:
	BoardNow = Transpose(BoardNow)
	BoardNow = WholeReverse(BoardNow)
	BoardNow = WholeLeft(BoardNow)
	BoardNow = WholeReverse(BoardNow)
	BoardNow = Transpose(BoardNow)

	
	return BoardNow

def NewValue():
	#Pre:
	#Post:
	if random.randint(1,8) == 1:
		return 4
	else:
		return 2

def MoreValues():
	#Pre:
	#Post:
	RowNum = 
	ColNum = 
	while board[RowNum][ColNum] != 0:
		
# A blank board
board = []
for i in range (Board_size):
	row = []
	for n in range (Board_size):
		row.append(0)
	board.append(row)

NeededSpots = 2
while NeededSpots > 0:
	RowNum = random.randint(0,Board_size-1)
	ColNum = random.randint(0,Board_size-1)
	if board[RowNum][ColNum] == 0:
		board[RowNum][ColNum] = NewValue()
		NeededSpots -= 1
Display(board)

while True:
	Movement = input("Direction you would like to move: ")

	if Movement == 'u':
		board = MergeUp(board)
		Display(board)
	elif Movement == 'd':
		board = MergeDown(board)
		Display(board)
	elif Movement == 'r':
		board = MergeRight(board)
		Display(board)
	elif Movement == 'l':
		board = WholeLeft(board)
		Display(board)
