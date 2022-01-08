import numpy as np
import sqlite3 as sql

board = np.array(
	[
		[ 4, 1, 0, 0, 0, 0,11,14],
		[ 2, 1, 0, 0, 0, 0,11,12],
		[ 3, 1, 0, 0, 0, 0,11,13],
		[ 5, 1, 0, 0, 0, 0,11,15],
		[ 6, 1, 0, 0, 0, 0,11,16],
		[ 3, 1, 0, 0, 0, 0,11,13],
		[ 2, 1, 0, 0, 0, 0,11,12],
		[ 4, 1, 0, 0, 0, 0,11,14]
	],dtype = np.int8)

wControl = np.array(
	[
		[False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True]
	],dtype = np.bool_)
bControl = np.array(
	[
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[ True, True, True, True, True, True, True, True],
		[False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False],
		[False,False,False,False,False,False,False,False]
	],dtype = np.bool_)
control = [wControl,bControl]

global gameMove; gameMove = 0
global drawCounter; drawCounter = 0

sCastleRight = [True,True]
lCastleRight = [True,True]

con = sql.connect('positions.db')

'''
con.execute('CREATE TABLE positions (a1 INT, a2 INT, a3 INT, a4 INT, a5 INT, a6 INT, a7 INT, a8 INT, b1 INT, b2 INT, b3 INT, b4 INT, b5 INT, b6 INT, b7 INT, b8 INT, c1 INT, c2 INT, c3 INT, c4 INT, c5 INT, c6 INT, c7 INT, c8 INT, d1 INT, d2 INT, d3 INT, d4 INT, d5 INT, d6 INT, d7 INT, d8 INT, e1 INT, e2 INT, e3 INT, e4 INT, e5 INT, e6 INT, e7 INT, e8 INT, f1 INT, f2 INT, f3 INT, f4 INT, f5 INT, f6 INT, f7 INT, f8 INT, g1 INT, g2 INT, g3 INT, g4 INT, g5 INT, g6 INT, g7 INT, g8 INT, h1 INT, h2 INT, h3 INT, h4 INT, h5 INT, h6 INT, h7 INT, h8 INT)')
'''

def possibleMoves(player):
	moves = []
	if sCastleRight[player] and board[4:8,player * 7] == [player * 10 + 6, 0, 0, player * 10 + 4] and control[(player + 1) % 2][4:7,player * 7] == [False,False,False]:
		moves.append("O-O")
	if lCastleRight[player] and board[0:5,player * 7] == [player * 10 + 4, 0, 0, 0, player * 10 + 6] and control[(player + 1) % 2][2:5, player * 7] == [False,False,False]:
		moves.append("O-O-O")
	for f in range(8):
		for r in range(8):
			if control[player][f,r] == False:
				pinCheck(player,f,r)
			pos = board[f,r]
			if pos == 1:
				print(1)

def inCheck(player,file,rank):
	inCheck = False
	checkType = ""
	checkPiecePos = (-1,-1)
	for f in range(file - 1,file + 2):
		for r in range(rank - 1,rank + 2):
			if f in range(8) and r in range(8) and board[f,r] == (player + 1) % 2 * 10 + 6:
				if inCheck == False:
					inCheck = True
					checkType = "king"
					checkPiecePos = (f,r)
				else:
					return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank + 1 in range(8) and board[file + 1,rank + 1] == 11 and player == 0:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file + 1,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank + 1 in range(8) and board[file - 1,rank + 1] == 11 and player == 0:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file - 1,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank - 1 in range(8) and board[file + 1,rank - 1] == 1 and player == 1:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file + 1,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank - 1 in range(8) and board[file - 1,rank - 1] == 1 and player == 1:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file - 1,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file + 2 in range(8) and rank + 1 in range(8) and board[file + 2,rank + 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 2,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file + 2 in range(8) and rank - 1 in range(8) and board[file + 2,rank - 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 2,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank + 2 in range(8) and board[file + 1,rank + 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 1,rank + 2)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank - 2 in range(8) and board[file + 1,rank - 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 1,rank - 2)
		else:
			return (True,"double",(-1,-1))
	if file - 2 in range(8) and rank + 1 in range(8) and board[file - 2,rank + 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 2,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file - 2 in range(8) and rank - 1 in range(8) and board[file - 2,rank - 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 2,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank + 2 in range(8) and board[file - 1,rank + 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 1,rank + 2)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank - 2 in range(8) and board[file - 1,rank - 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 1,rank - 2)
		else:
			return (True,"double",(-1,-1))
	for f in range(file - 1,-1,-1):
		if board[f,rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[f,rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "file"
				checkPiecePos = (f,rank)
			else:
				return (True,"double",(-1,-1))
	for f in range(file + 1,8,1):
		if board[f,rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[f,rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "file"
				checkPiecePos = (f,rank)
			else:
				return (True,"double",(-1,-1))
	for r in range(rank - 1,-1,-1):
		if board[file,r] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[file,r] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "rank"
				checkPiecePos = (file,r)
			else:
				return (True,"double",(-1,-1))
	for r in range(rank + 1,8,1):
		if board[file,r] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[file,r] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "rank"
				checkPiecePos = (file,r)
			else:
				return (True,"double",(-1,-1))
	for i in range(1,8):
		if file + i not in range(8) or rank + i not in range(8):
			break
		if board[file + i,rank + i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file + i,rank + i)
			else:
				return (True,"double",(-1,-1))
		if board[file + i,rank + i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file + i not in range(8) or rank - i not in range(8):
			break
		if board[file + i,rank - i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file + i,rank - i)
			else:
				return (True,"double",(-1,-1))
		if board[file + i,rank - i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file - i not in range(8) or rank + i not in range(8):
			break
		if board[file - i,rank + i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file - i,rank + i)
			else:
				return (True,"double",(-1,-1))
		if board[file - i,rank + i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file - i not in range(8) or rank - i not in range(8):
			break
		if board[file - i,rank - i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file - i,rank - i)
			else:
				return (True,"double",(-1,-1))
		if board[file - i,rank - i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	return (inCheck,checkType,checkPiecePos)

def pinCheck(player,file,rank):
	kFile = 0
	kRank = 0
	for f in range(8):
		for r in range(8):
			if board[f,r] == player * 10 + 6:
				kFile = f
				kRank = r
				break
	if file == kFile and rank == kRank:
		return ("no pin","0")
	if abs(file - kFile) == abs(rank - kRank):
		fdir = int(abs(file - kFile) / (file - kFile))
		rdir = int(abs(rank - kRank) / (rank - kRank))
		for i in range(1,abs(file - kFile) + 1):
				if not board[file - fdir * i,rank - rdir * i] in (0,7,17):
					return ("no pin","0")
		for i in range(1,8):
			if not file - fdir * i in range(8) or not rank - rdir * i in range(8):
				break
			if board[file - fdir * i,rank - rdir * i] in (1,11,2,12,player * 10 + 3,4,14,player * 10 + 5):
				break
			if board[file - fdir * i,rank - rdir * i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
				if file - kFile == rank - kRank:
					return ("diag pin","+")
				else:
					return ("diag pin","-")
		return ("no pin","0")
	elif file == kFile:
		dir = int(abs(rank - kRank) / (rank - kRank))
		for i in range(rank + 1,kRank):
			if not board[file,i] in (0,7,17):
				return ("no pin","0")
		for i in range(rank + dir,int(dir * 4.5 + 3.5),dir):
			if board[file,i] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5):
				break
			if board[file,i] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				return ("file pin","+")
		return ("no pin","0")
	elif rank == kRank:
		dir = int(abs(file - kFile) / (file - kFile))
		for i in range(file + 1,kFile):
			if not board[i,rank] in (0,7,17):
				return ("no pin","0")
		for i in range(file + dir,int(dir * 4.5 + 3.5),dir):
			if board[i,rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5):
				break
			if board[i,rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				return ("rank pin","-")
		return ("no pin","0")
	return ("no pin","0")

def updateControl(player):
	for f in range(8):
		for r in range(8):
			if inCheck(player,f,r)[0]:
				control[player][f,r] == False
			else:
				control[player][f,r] == True

def move(m):
	global gameMove
	global drawCounter
	if m == "O-O":
		board[4,gameMove % 2 * 7] = 0
		board[5,gameMove % 2 * 7] = gameMove % 2 * 10 + 4
		board[6,gameMove % 2 * 7] = gameMove % 2 * 10 + 6
		board[7,gameMove % 2 * 7] = 0
		gameMove += 1
		drawCounter += 1
	if m == "O-O-O":
		board[4,gameMove % 2 * 7] = 0
		board[3,gameMove % 2 * 7] = gameMove % 2 * 10 + 4
		board[2,gameMove % 2 * 7] = gameMove % 2 * 10 + 6
		board[0,gameMove % 2 * 7] = 0
		gameMove += 1
		drawCounter += 1
	if m[0:2] == "pd":
		print("pd")
	if m[0:2] == "pp":
		print("pp")
	if m[0:2] == "ep":
		pos1 = board[ord(m[2]) - 97,ord(m[3] - 49)]
		pos2 = board[ord(m[4]) - 97,ord(m[5] - 49)]
		posEP = board[ord(m[4]) - 97,ord(m[3]) - 49]
		board[ord(m[4]) - 97,ord(m[5] - 49)] = pos1
		board[ord(m[2]) - 97,ord(m[3] - 49)] = 0
		board[ord(m[4]) - 97,ord(m[3]) - 49] = 0
		gameMove += 1
		drawCounter = 0
	else:
		pos1 = board[ord(m[0]) - 97,ord(m[1] - 49)]
		pos2 = board[ord(m[2]) - 97,ord(m[3] - 49)]
		board[ord(m[2]) - 97,ord(m[3] - 49)] = pos1
		board[ord(m[0]) - 97,ord(m[1] - 49)] = 0
		gameMove += 1
		if pos1 in (1,11):
			drawCounter = 0
		if pos2 != 0:
			drawCounter = 0
		else:
			drawCounter += 1
	arrayToDatabase()
	updateControl(0)
	updateControl(1)
	

def arrayToDatabase():
	array = []
	for f in range(8):
		for r in range(8):
			array.append(int(board[f,r]))
	con.execute("INSERT INTO positions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(tuple(array)))
	con.commit
	con.close

def databaseToArray():
	array = []
	for item in con.execute("SELECT * from positions").fetchall()[-1]:
		array.append(item)
	nparray = np.array(array,dtype = np.int8).reshape(8,8)
	return nparray