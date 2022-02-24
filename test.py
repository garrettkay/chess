import numpy as np
import sqlite3 as sql

board = np.array([[ 4, 1, 0, 0, 0, 0,11,14],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 3, 1, 0, 0, 0, 0,11,13],
			 [ 5, 1, 0, 0, 0, 0,11,15],
			 [ 6, 1, 0, 0, 0, 0,11,16],
			 [ 3, 1, 0, 0, 0, 0,11,13],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 4, 1, 0, 0, 0, 0,11,14]], dtype = np.int8)

con = sql.connect('positions.db')
cur = con.cursor()

'''
cur.execute('CREATE TABLE positions (a1 INT, a2 INT, a3 INT, a4 INT, a5 INT, a6 INT, a7 INT, a8 INT, b1 INT, b2 INT, b3 INT, b4 INT, b5 INT, b6 INT, b7 INT, b8 INT, c1 INT, c2 INT, c3 INT, c4 INT, c5 INT, c6 INT, c7 INT, c8 INT, d1 INT, d2 INT, d3 INT, d4 INT, d5 INT, d6 INT, d7 INT, d8 INT, e1 INT, e2 INT, e3 INT, e4 INT, e5 INT, e6 INT, e7 INT, e8 INT, f1 INT, f2 INT, f3 INT, f4 INT, f5 INT, f6 INT, f7 INT, f8 INT, g1 INT, g2 INT, g3 INT, g4 INT, g5 INT, g6 INT, g7 INT, g8 INT, h1 INT, h2 INT, h3 INT, h4 INT, h5 INT, h6 INT, h7 INT, h8 INT)')
'''

def arrayToDatabase():
	array = []
	for f in range(8):
		for r in range(8):
			array.append(int(board[f,r]))
	cur.execute("INSERT INTO positions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(tuple(array)))
	con.commit
	con.close

def databaseToArray(n):
	array = []
	for item in cur.execute("SELECT * from positions").fetchall()[-n]:
		array.append(item)
	nparray = np.array(array,dtype = np.int8).reshape(8,8)
	return nparray

arrayToDatabase()

board = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0]], dtype = np.int8)

arrayToDatabase()

print(databaseToArray(1))
print(databaseToArray(0))