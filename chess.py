import pygame
from pygame.locals import *
import numpy
import random
from copy import copy, deepcopy

global gBoard
gBoard = 	[[ 4, 1, 0, 0, 0, 0,11,14],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 3, 1, 0, 0, 0, 0,11,13],
			 [ 5, 1, 0, 0, 0, 0,11,15],
			 [ 6, 1, 0, 0, 0, 0,11,16],
			 [ 3, 1, 0, 0, 0, 0,11,13],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 4, 1, 0, 0, 0, 0,11,14]]
global gPositions
gPositions =[[[ 4, 1, 0, 0, 0, 0,11,14],
			  [ 2, 1, 0, 0, 0, 0,11,12],
			  [ 3, 1, 0, 0, 0, 0,11,13],
			  [ 5, 1, 0, 0, 0, 0,11,15],
			  [ 6, 1, 0, 0, 0, 0,11,16],
			  [ 3, 1, 0, 0, 0, 0,11,13],
			  [ 2, 1, 0, 0, 0, 0,11,12],
			  [ 4, 1, 0, 0, 0, 0,11,14]]]
empty = 	[[ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0],
			 [ 0, 0, 0, 0, 0, 0, 0, 0]]
global gSCastleRight; gSCastleRight = [True,True]
global gLCastleRight; gLCastleRight = [True,True]
getPieceNumber = {
	"P" : 1,
	"N" : 2,
	"B" : 3,
	"R" : 4,
	"Q" : 5,
	"K" : 6,
	"p" : 1,
	"n" : 2,
	"b" : 3,
	"r" : 4,
	"q" : 5,
	"k" : 6,
	"#" : 8
}
getPiece = {
	0 : "#",
	1 : "P",
	2 : "N",
	3 : "B",
	4 : "R",
	5 : "Q",
	6 : "K",
	11 : "P",
	12 : "N",
	13 : "B",
	14 : "R",
	15 : "Q",
	16 : "K",
}
global gTurn; gTurn = [0]

pygame.init
pygame.font.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Chess")

wP = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whitePawn.png')
bP = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackPawn.png')
wN = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whiteKnight.png')
bN = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackKnight.png')
wB = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whiteBishop.png')
bB = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackBishop.png')
wR = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whiteRook.png')
bR = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackRook.png')
wQ = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whiteQueen.png')
bQ = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackQueen.png')
wK = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\whiteKing.png')
bK = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\blackKing.png')
background = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\chessBackground.png')
wPromo = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\wPromoUI.png')
bPromo = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Coding\chess\images\bPromoUI.png')

def printBoard():
	print("   ",end ="")
	for letter in range(97,105):
		print("\033[91m" + "  " + chr(letter) + " " + "\033[0m",end = "")
	print("")
	for i in range(7,-1,-1):
		print("\033[91m" + " " + str(i + 1) + " " + "\033[0m",end = "")
		for j in range(8):
			if gBoard[j][i] in (7,17):
				print("  0 ",end = "")
			elif len(str(gBoard[j][i])) == 1:
				print("  " + str(gBoard[j][i]) + " ",end = "")
			else:
				print(" " + str(gBoard[j][i]) + " ",end = "")
		print("\033[91m" + " " + str(i + 1) + "\033[0m",end = "")
		print("")
	print("   ",end ="")
	for letter in range(97,105):
		print("\033[91m" + "  " + chr(letter) + " " + "\033[0m",end = "")
	print("")

def drawBoard():
	screen.blit(background,(0,0))
	for f in range(8):
		for r in range(8):
			if gBoard[f][r] == 1:
				screen.blit(wP,wP.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 11:
				screen.blit(bP,bP.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 2:
				screen.blit(wN,wN.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 12:
				screen.blit(bN,bN.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 3:
				screen.blit(wB,wB.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 13:
				screen.blit(bB,bB.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 4:
				screen.blit(wR,wR.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 14:
				screen.blit(bR,bR.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 5:
				screen.blit(wQ,wQ.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 15:
				screen.blit(bQ,bQ.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 6:
				screen.blit(wK,wK.get_rect(center=(100 * f + 150,-100 * r + 850)))
			elif gBoard[f][r] == 16:
				screen.blit(bK,bK.get_rect(center=(100 * f + 150,-100 * r + 850)))
	pygame.display.flip()

def move(m, check = ""):
	global gBoard
	global gPositions
	global gSCastleRight
	global gLCastleRight
	global gTurn
	board = []
	positions = []
	sCastleRight = []
	lCastleRight = []
	turn = []
	if check == "":
		board = gBoard
		positions = gPositions
		sCastleRight = gSCastleRight
		lCastleRight = gLCastleRight
		turn = gTurn
	else:
		board = deepcopy(gBoard)
		positions = deepcopy(gPositions)
		sCastleRight = deepcopy(gSCastleRight)
		lCastleRight = deepcopy(gLCastleRight)
		turn = deepcopy(gTurn)
	deactivateBishop = False
	if turn[0] == 0:
		for f in range(8):
			for r in range(8):
				if board[f][r] == 7:
					board[f][r] = 0
	if turn[0] == 1:
		for f in range(8):
			for r in range(8):
				if board[f][r] == 17:
					board[f][r] = 0
	if board[0][0] != 4:
		lCastleRight[0] = False
	if board[7][0] != 4:
		sCastleRight[0] = False
	if board[0][7] != 14:
		lCastleRight[1] = False
	if board[7][7] != 14:
		sCastleRight[1] = False
	if board[4][0] != 6:
		lCastleRight[0] = False
		sCastleRight[0] = False
	if board[4][7] != 16:
		lCastleRight[1] = False
		sCastleRight[1] = False
	moveType = ""
	PorC = 0
	if m in ("0-0","o-o","O-O"):
		if sCastleRight[turn[0]] and not inCheck(turn[0],4,turn[0] * 7,board)[0] and not inCheck(turn[0],5,turn[0] * 7,board)[0] and not inCheck(turn[0],6,turn[0] * 7,board)[0] and board[4][turn[0] * 7] == turn[0] * 10 + 6 and board[5][turn[0] * 7] == 0 and board[6][turn[0] * 7] == 0 and board[7][turn[0] * 7] == turn[0] * 10 + 4:
			board[4][turn[0] * 7] = 0
			board[5][turn[0] * 7] = turn[0] * 10 + 4
			board[6][turn[0] * 7] = turn[0] * 10 + 6
			board[7][turn[0] * 7] = 0
			sCastleRight[turn[0]] = False
			positions.append(deepcopy(board))
			moveType = "short castle"
			PorC = 1
	if m in ("0-0-0","o-o-o","O-O-O"):
		if lCastleRight[turn[0]] and not inCheck(turn[0],2,turn[0] * 7,board)[0] and not inCheck(turn[0],3,turn[0] * 7,board)[0] and not inCheck(turn[0],4,turn[0] * 7,board)[0] and board[0][turn[0] * 7] == turn[0] * 10 + 4 and board[1][turn[0] * 7] == 0 and board[2][turn[0] * 7] == 0 and board[3][turn[0] * 7] == 0 and board[4][turn[0] * 7] == turn[0] * 10 + 6:
			board[4][turn[0] * 7] = 0
			board[3][turn[0] * 7] = turn[0] * 10 + 4
			board[2][turn[0] * 7] = turn[0] * 10 + 6
			board[0][turn[0] * 7] = 0
			lCastleRight[turn[0]] = False
			positions.append(deepcopy(board))
			moveType = "long castle"
			PorC = 1
	if len(m) == 2 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] == "4" and board[ord(m[0]) - 97][1] == 1:
		if board[ord(m[0]) - 97][3] == 0 and board[ord(m[0]) - 97][2] == 0 and board[ord(m[0]) - 97][1] == 1:
			board[ord(m[0]) - 97][3] = 1
			board[ord(m[0]) - 97][2] = 7
			board[ord(m[0]) - 97][1] = 0
			positions.append(deepcopy(board))
			moveType = "p double"
			PorC = 2
	if len(m) == 2 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] == "5" and board[ord(m[0]) - 97][6] == 11:
		if board[ord(m[0]) - 97][4] == 0 and board[ord(m[0]) - 97][5] == 0 and board[ord(m[0]) - 97][6] == 11:
			board[ord(m[0]) - 97][4] = 11
			board[ord(m[0]) - 97][5] = 17
			board[ord(m[0]) - 97][6] = 0
			positions.append(deepcopy(board))
			moveType = "p double"
			PorC = 2
	if len(m) == 2 and turn[0] == 0 and ord(m[0]) in range(97,105) and ord(m[1]) in range(51,56):
		if board[ord(m[0]) - 97][ord(m[1]) - 49] == 0 and board[ord(m[0]) - 97][ord(m[1]) - 49 - 1] == 1:
			board[ord(m[0]) - 97][ord(m[1]) - 49] = 1
			board[ord(m[0]) - 97][ord(m[1]) - 49 - 1] = 0
			positions.append(deepcopy(board))
			moveType = "p single"
			PorC = 2
	if len(m) == 2 and turn[0] == 1 and ord(m[0]) in range(97,105) and ord(m[1]) in range(50,55):
		if board[ord(m[0]) - 97][ord(m[1]) - 49] == 0 and board[ord(m[0]) - 97][ord(m[1]) - 49 + 1] == 11:
			board[ord(m[0]) - 97][ord(m[1]) - 49] = 11
			board[ord(m[0]) - 97][ord(m[1]) - 49 + 1] = 0
			positions.append(deepcopy(board))
			moveType = "p single"
			PorC = 2
	if len(m) == 2 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] == "8":
		if board[ord(m[0]) - 97][7] == 0 and board[ord(m[0]) - 97][6] == 1:
			board[ord(m[0]) - 97][7] = 5
			board[ord(m[0]) - 97][6] = 0
			positions.append(deepcopy(board))
			moveType = "p single def promo"
			PorC = 2
	if len(m) == 2 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] == "1":
		if board[ord(m[0]) - 97][0] == 0 and board[ord(m[0]) - 97][1] == 1:
			board[ord(m[0]) - 97][0] = 15
			board[ord(m[0]) - 97][1] = 0
			positions.append(deepcopy(board))
			moveType = "p single def promo"
			PorC = 2
	if len(m) == 4 and turn[0] == 0 and m[2] == "=" and ord(m[0]) in range(97,105) and m[1] == "8" and m[3] in ("N","B","R","Q","n","b","r","q") and board[ord(m[0]) - 97][7] == 0 and board[ord(m[0]) - 97][6] == 1:
		board[ord(m[0]) - 97][7] = getPieceNumber.get(m[3])
		board[ord(m[0]) - 97][6] = 0
		positions.append(deepcopy(board))
		moveType = "p single promo"
		PorC = 2
	if len(m) == 4 and turn[0] == 1 and m[2] == "=" and ord(m[0]) in range(97,105) and m[1] == "1" and m[3] in ("N","B","R","Q","n","b","r","q") and board[ord(m[0]) - 97][0] == 0 and board[ord(m[0]) - 97][1] == 11:
		board[ord(m[0]) - 97][0] = 10 + getPieceNumber.get(m[3])
		board[ord(m[0]) - 97][1] = 0
		positions.append(deepcopy(board))
		moveType = "p single promo"
		PorC = 2
	if len(m) == 4 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(51,56) and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[2]) - 97][ord(m[3]) - 49] in (11,12,13,14,15):
		if board[ord(m[0]) - 97][ord(m[3]) - 49 - 1] == 1:
			if m[0:1] in ("bX","bx","BX","Bx"):
				deactivateBishop = True
			board[ord(m[0]) - 97][ord(m[3]) - 49 - 1] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = 1
			positions.append(deepcopy(board))
			moveType = "p cap"
			PorC = 2
	if len(m) == 4 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(50,55) and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[2]) - 97][ord(m[3]) - 49] in (1,2,3,4,5):
		if board[ord(m[0]) - 97][ord(m[3]) - 49 + 1] == 11:
			if m[0:1] in ("bX","bx","BX","Bx"):
				deactivateBishop = True
			board[ord(m[0]) - 97][ord(m[3]) - 49 + 1] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = 11
			positions.append(deepcopy(board))
			moveType = "p cap"
			PorC = 2
	if len(m) == 4 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "8" and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[2]) - 97][ord(m[3]) - 49] in (11,12,13,14,15):
		if board[ord(m[0]) - 97][6] == 1:
			if m[0:1] in ("bX","bx","BX","Bx"):
				deactivateBishop = True
			board[ord(m[0]) - 97][6] = 0
			board[ord(m[2]) - 97][7] = 5
			positions.append(deepcopy(board))
			moveType = "p cap def promo"
			PorC = 2
	if len(m) == 4 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "1" and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[2]) - 97][ord(m[3]) - 49] in (1,2,3,4,5):
		if board[ord(m[0]) - 97][1] == 11:
			if m[0:1] in ("bX","bx","BX","Bx"):
				deactivateBishop = True
			board[ord(m[0]) - 97][1] = 0
			board[ord(m[2]) - 97][0] = 15
			positions.append(deepcopy(board))
			moveType = "p cap def promo"
			PorC = 2
	if len(m) == 6 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "8" and m[4] == "=" and m[5] in ("N","B","R","Q","n","b","r","q") and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[0]) - 97][6] == 1 and board[ord(m[2]) - 97][7] in (11,12,13,14,15):
			board[ord(m[2]) - 97][7] = getPieceNumber.get(m[5])
			board[ord(m[0]) - 97][6] = 0
			positions.append(deepcopy(board))
			moveType = "p cap promo"
			PorC = 2
	if len(m) == 6 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "1" and m[4] == "=" and m[5] in ("N","B","R","Q","n","b","r","q") and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[0]) - 97][1] == 11 and board[ord(m[2]) - 97][0] in (1,2,3,4,5):
			board[ord(m[2]) - 97][0] = 10 + getPieceNumber.get(m[5])
			board[ord(m[0]) - 97][1] = 0
			positions.append(deepcopy(board))
			moveType = "p cap promo"
			PorC = 2
	if len(m) == 4 and turn[0] == 0 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "6" and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[0]) - 97][4] == 1 and board[ord(m[2]) - 97][4] == 11 and board[ord(m[2]) - 97][5] == 17:
		board[ord(m[0]) - 97][4] = 0
		board[ord(m[2]) - 97][4] = 0
		board[ord(m[2]) - 97][5] = 1
		positions.append(deepcopy(board))
		moveType = "en passant"
		PorC = 2
	if len(m) == 4 and turn[0] == 1 and ord(m[0]) in range(97,105) and m[1] in ("X","x") and ord(m[2]) in range(97,105) and m[3] == "3" and abs(ord(m[2]) - ord(m[0])) == 1 and board[ord(m[0]) - 97][3] == 11 and board[ord(m[2]) - 97][3] == 1 and board[ord(m[2]) - 97][2] == 7:
		board[ord(m[0]) - 97][3] = 0
		board[ord(m[2]) - 97][3] = 0
		board[ord(m[2]) - 97][2] = 11
		positions.append(deepcopy(board))
		moveType = "en passant"
		PorC = 2
	if len(m) == 3 and m[0] in ("N","n") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and not board[ord(m[1]) - 97][ord(m[2]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		if ord(m[1]) - 97 + 2 in range(8) and ord(m[2]) - 49 + 1 in range(8) and board[ord(m[1]) - 97 + 2][ord(m[2]) - 49 + 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 + 2,ord(m[2]) - 49 + 1))
		if ord(m[1]) - 97 + 2 in range(8) and ord(m[2]) - 49 - 1 in range(8) and board[ord(m[1]) - 97 + 2][ord(m[2]) - 49 - 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 + 2,ord(m[2]) - 49 - 1))
		if ord(m[1]) - 97 + 1 in range(8) and ord(m[2]) - 49 + 2 in range(8) and board[ord(m[1]) - 97 + 1][ord(m[2]) - 49 + 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 + 1,ord(m[2]) - 49 + 2))
		if ord(m[1]) - 97 + 1 in range(8) and ord(m[2]) - 49 - 2 in range(8) and board[ord(m[1]) - 97 + 1][ord(m[2]) - 49 - 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 + 1,ord(m[2]) - 49 - 2))
		if ord(m[1]) - 97 - 2 in range(8) and ord(m[2]) - 49 + 1 in range(8) and board[ord(m[1]) - 97 - 2][ord(m[2]) - 49 + 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 - 2,ord(m[2]) - 49 + 1))
		if ord(m[1]) - 97 - 2 in range(8) and ord(m[2]) - 49 - 1 in range(8) and board[ord(m[1]) - 97 - 2][ord(m[2]) - 49 - 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 - 2,ord(m[2]) - 49 - 1))
		if ord(m[1]) - 97 - 1 in range(8) and ord(m[2]) - 49 + 2 in range(8) and board[ord(m[1]) - 97 - 1][ord(m[2]) - 49 + 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 - 1,ord(m[2]) - 49 + 2))
		if ord(m[1]) - 97 - 1 in range(8) and ord(m[2]) - 49 - 2 in range(8) and board[ord(m[1]) - 97 - 1][ord(m[2]) - 49 - 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[1]) - 97 - 1,ord(m[2]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[1]) - 97][ord(m[2]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("N","n") and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and board[ord(m[2]) - 97][ord(m[3]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 - 2))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("N","n") and ord(m[1]) in range(97,105) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[2]) - 97 + 2 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[2]) - 97 + 2 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[2]) - 97 + 1 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[2]) - 97 + 1 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 - 2))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[2]) - 97 - 2 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[2]) - 97 - 2 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[2]) - 97 - 1 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[2]) - 97 - 1 == ord(m[1]) - 97:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n f dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("N","n") and ord(m[1]) in range(97,105) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		if ord(m[3]) - 97 + 2 in range(8) and ord(m[4]) - 49 + 1 in range(8) and board[ord(m[3]) - 97 + 2][ord(m[4]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[3]) - 97 + 2 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 + 2,ord(m[4]) - 49 + 1))
		if ord(m[3]) - 97 + 2 in range(8) and ord(m[4]) - 49 - 1 in range(8) and board[ord(m[3]) - 97 + 2][ord(m[4]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[3]) - 97 + 2 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 + 2,ord(m[4]) - 49 - 1))
		if ord(m[3]) - 97 + 1 in range(8) and ord(m[4]) - 49 + 2 in range(8) and board[ord(m[3]) - 97 + 1][ord(m[4]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[3]) - 97 + 1 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 + 1,ord(m[4]) - 49 + 2))
		if ord(m[3]) - 97 + 1 in range(8) and ord(m[4]) - 49 - 2 in range(8) and board[ord(m[3]) - 97 + 1][ord(m[4]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[3]) - 97 + 1 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 + 1,ord(m[4]) - 49 - 2))
		if ord(m[3]) - 97 - 2 in range(8) and ord(m[4]) - 49 + 1 in range(8) and board[ord(m[3]) - 97 - 2][ord(m[4]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[3]) - 97 - 2 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 - 2,ord(m[4]) - 49 + 1))
		if ord(m[3]) - 97 - 2 in range(8) and ord(m[4]) - 49 - 1 in range(8) and board[ord(m[3]) - 97 - 2][ord(m[4]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[3]) - 97 - 2 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 - 2,ord(m[4]) - 49 - 1))
		if ord(m[3]) - 97 - 1 in range(8) and ord(m[4]) - 49 + 2 in range(8) and board[ord(m[3]) - 97 - 1][ord(m[4]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[3]) - 97 - 1 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 - 1,ord(m[4]) - 49 + 2))
		if ord(m[3]) - 97 - 1 in range(8) and ord(m[4]) - 49 - 2 in range(8) and board[ord(m[3]) - 97 - 1][ord(m[4]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[3]) - 97 - 1 == ord(m[1]) - 97:
			pCand.append((ord(m[3]) - 97 - 1,ord(m[4]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n f dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("N","n") and ord(m[1]) in range(49,57) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[3]) - 49 + 1 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 + 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 + 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[3]) - 49 - 1 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 + 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[3]) - 49 + 2 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 + 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 + 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[3]) - 49 - 2 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 + 1,ord(m[3]) - 49 - 2))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 + 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[3]) - 49 + 1 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 + 1))
		if ord(m[2]) - 97 - 2 in range(8) and ord(m[3]) - 49 - 1 in range(8) and board[ord(m[2]) - 97 - 2][ord(m[3]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[3]) - 49 - 1 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 - 2,ord(m[3]) - 49 - 1))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 + 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[3]) - 49 + 2 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 + 2))
		if ord(m[2]) - 97 - 1 in range(8) and ord(m[3]) - 49 - 2 in range(8) and board[ord(m[2]) - 97 - 1][ord(m[3]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[3]) - 49 - 2 == ord(m[1]) - 49:
			pCand.append((ord(m[2]) - 97 - 1,ord(m[3]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n r dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("N","n") and ord(m[1]) in range(49,57) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		if ord(m[3]) - 97 + 2 in range(8) and ord(m[4]) - 49 + 1 in range(8) and board[ord(m[3]) - 97 + 2][ord(m[4]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[4]) - 49 + 1 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 + 2,ord(m[4]) - 49 + 1))
		if ord(m[3]) - 97 + 2 in range(8) and ord(m[4]) - 49 - 1 in range(8) and board[ord(m[3]) - 97 + 2][ord(m[4]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[4]) - 49 - 1 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 + 2,ord(m[4]) - 49 - 1))
		if ord(m[3]) - 97 + 1 in range(8) and ord(m[4]) - 49 + 2 in range(8) and board[ord(m[3]) - 97 + 1][ord(m[4]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[4]) - 49 + 2 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 + 1,ord(m[4]) - 49 + 2))
		if ord(m[3]) - 97 + 1 in range(8) and ord(m[4]) - 49 - 2 in range(8) and board[ord(m[3]) - 97 + 1][ord(m[4]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[4]) - 49 - 2 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 + 1,ord(m[4]) - 49 - 2))
		if ord(m[3]) - 97 - 2 in range(8) and ord(m[4]) - 49 + 1 in range(8) and board[ord(m[3]) - 97 - 2][ord(m[4]) - 49 + 1] == turn[0] * 10 + 2 and ord(m[4]) - 49 + 1 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 - 2,ord(m[4]) - 49 + 1))
		if ord(m[3]) - 97 - 2 in range(8) and ord(m[4]) - 49 - 1 in range(8) and board[ord(m[3]) - 97 - 2][ord(m[4]) - 49 - 1] == turn[0] * 10 + 2 and ord(m[4]) - 49 - 1 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 - 2,ord(m[4]) - 49 - 1))
		if ord(m[3]) - 97 - 1 in range(8) and ord(m[4]) - 49 + 2 in range(8) and board[ord(m[3]) - 97 - 1][ord(m[4]) - 49 + 2] == turn[0] * 10 + 2 and ord(m[4]) - 49 + 2 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 - 1,ord(m[4]) - 49 + 2))
		if ord(m[3]) - 97 - 1 in range(8) and ord(m[4]) - 49 - 2 in range(8) and board[ord(m[3]) - 97 - 1][ord(m[4]) - 49 - 2] == turn[0] * 10 + 2 and ord(m[4]) - 49 - 2 == ord(m[1]) - 49:
			pCand.append((ord(m[3]) - 97 - 1,ord(m[4]) - 49 - 2))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n r dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("N","n") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 2 and not board[ord(m[3]) - 97][ord(m[4]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		if (abs(ord(m[4]) - ord(m[2])) == 2 and abs(ord(m[3]) - ord(m[1])) == 1) or (abs(ord(m[4]) - ord(m[2])) == 1 and abs(ord(m[3]) - ord(m[1])) == 2) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 2:
			board[ord(m[1]) - 97][ord(m[2]) - 49] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n f r dis"
			PorC = 1
	if len(m) == 6 and m[0] in ("N","n") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and m[3] in ("X","x") and ord(m[4]) in range(97,105) and ord(m[5]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 2 and board[ord(m[4]) - 97][ord(m[5]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		if (abs(ord(m[5]) - ord(m[2])) == 2 and abs(ord(m[4]) - ord(m[1])) == 1) or (abs(ord(m[5]) - ord(m[2])) == 1 and abs(ord(m[4]) - ord(m[1])) == 2) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 2:
			board[ord(m[1]) - 97][ord(m[2]) - 49] = 0
			board[ord(m[4]) - 97][ord(m[5]) - 49] = turn[0] * 10 + 2
			positions.append(deepcopy(board))
			moveType = "n f r dis cap"
			PorC = 2
	if len(m) == 3 and m[0] in ("B","b") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and not board[ord(m[1]) - 97][ord(m[2]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6) and not deactivateBishop:
		pCand = []
		for i in range(1,8):
			if ord(m[1]) - 97 + i not in range(8) or ord(m[2]) - 49 + i not in range(8):
				break
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 + i] == turn[0] * 10 + 3:
				pCand.append((ord(m[1]) - 97 + i,ord(m[2]) - 49 + i))
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 + i not in range(8) or ord(m[2]) - 49 - i not in range(8):
				break
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 - i] == turn[0] * 10 + 3:
				pCand.append((ord(m[1]) - 97 + i,ord(m[2]) - 49 - i))
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 - i not in range(8) or ord(m[2]) - 49 + i not in range(8):
				break
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 + i] == turn[0] * 10 + 3:
				pCand.append((ord(m[1]) - 97 - i,ord(m[2]) - 49 + i))
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 - i not in range(8) or ord(m[2]) - 49 - i not in range(8):
				break
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 - i] == turn[0] * 10 + 3:
				pCand.append((ord(m[1]) - 97 - i,ord(m[2]) - 49 - i))
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[1]) - 97][ord(m[2]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("B","b") and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and board[ord(m[2]) - 97][ord(m[3]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5) and not deactivateBishop:
		pCand = []
		for i in range(1,8):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("B","b") and ord(m[1]) in range(97,105) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[2]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[2]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[2]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[2]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[2]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[2]) - 97 - i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[2]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[2]) - 97 - i != ord(m[1]) - 97):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b f dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("B","b") and ord(m[1]) in range(97,105) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i != ord(m[1]) - 97):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b f dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("B","b") and ord(m[1]) in range(49,57) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 49 - i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 49 - i != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b r dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("B","b") and ord(m[1]) in range(49,57) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[4]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[4]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[4]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[4]) - 49 - i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[4]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[4]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[4]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[4]) - 49 - i != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b r dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("B","b") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 3 and not board[ord(m[3]) - 97][ord(m[4]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i == ord(m[1]) - 97 and ord(m[4]) - 49 + i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[3]) - 97 + i != ord(m[1]) - 97 or ord(m[4]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 97 + i == ord(m[1]) - 97 and ord(m[4]) - 49 - i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[3]) - 97 + i != ord(m[1]) - 97 or ord(m[4]) - 49 - i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i == ord(m[1]) - 97 and ord(m[4]) - 49 + i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[3]) - 97 - i != ord(m[1]) - 97 or ord(m[4]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and ord(m[3]) - 97 - i == ord(m[1]) - 97 and ord(m[4]) - 49 - i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[3]) - 97 - i != ord(m[1]) - 97 or ord(m[4]) - 49 - i != ord(m[2]) - 49)):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b f r dis"
			PorC = 1
	if len(m) == 6 and m[0] in ("B","b") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and m[3] in ("X","x") and ord(m[4]) in range(97,105) and ord(m[5]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 3 and board[ord(m[4]) - 97][ord(m[5]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5) and not deactivateBishop:
		pCand = []
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[4]) - 97 + i not in range(8) or ord(m[5]) - 49 + i not in range(8):
				break
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 + i == ord(m[1]) - 97 and ord(m[5]) - 49 + i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 + i,ord(m[5]) - 49 + i))
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 + i != ord(m[1]) - 97 or ord(m[5]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[4]) - 97 + i not in range(8) or ord(m[5]) - 49 - i not in range(8):
				break
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 + i == ord(m[1]) - 97 and ord(m[5]) - 49 - i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 + i,ord(m[5]) - 49 - i))
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 + i != ord(m[1]) - 97 or ord(m[5]) - 49 - i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[4]) - 97 - i not in range(8) or ord(m[5]) - 49 + i not in range(8):
				break
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 - i == ord(m[1]) - 97 and ord(m[5]) - 49 + i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 - i,ord(m[5]) - 49 + i))
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 - i != ord(m[1]) - 97 or ord(m[5]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[4]) - 97 - i not in range(8) or ord(m[5]) - 49 - i not in range(8):
				break
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 - i == ord(m[1]) - 97 and ord(m[5]) - 49 - i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 - i,ord(m[5]) - 49 - i))
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] in (1,11,2,12,4,14,5,15,6,16,(turn[0] + 1) % 2 * 10 + 3) or (board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] == turn[0] * 10 + 3 and (ord(m[4]) - 97 - i != ord(m[1]) - 97 or ord(m[5]) - 49 - i != ord(m[2]) - 49)):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[4]) - 97][ord(m[5]) - 49] = turn[0] * 10 + 3
			positions.append(deepcopy(board))
			moveType = "b f r dis cap"
			PorC = 2
	if len(m) == 3 and m[0] in ("R","r") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and not board[ord(m[1]) - 97][ord(m[2]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for f in range(ord(m[1]) - 97 - 1,-1,-1):
			if board[f][ord(m[2]) - 49] == turn[0] * 10 + 4:
				pCand.append((f,ord(m[2]) - 49))
			if board[f][ord(m[2]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for f in range(ord(m[1]) - 97 + 1,8,1):
			if board[f][ord(m[2]) - 49] == turn[0] * 10 + 4:
				pCand.append((f,ord(m[2]) - 49))
			if board[f][ord(m[2]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for r in range(ord(m[2]) - 49 - 1,-1,-1):
			if board[ord(m[1]) - 97][r] == turn[0] * 10 + 4:
				pCand.append((ord(m[1]) - 97,r))
			if board[ord(m[1]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for r in range(ord(m[2]) - 49 + 1,8,1):
			if board[ord(m[1]) - 97][r] == turn[0] * 10 + 4:
				pCand.append((ord(m[1]) - 97,r))
			if board[ord(m[1]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[1]) - 97][ord(m[2]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("R","r") and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and board[ord(m[2]) - 97][ord(m[3]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for f in range(ord(m[2]) - 97 - 1,-1,-1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 4:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for f in range(ord(m[2]) - 97 + 1,8,1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 4:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for r in range(ord(m[3]) - 49 - 1,-1,-1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 4:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		for r in range(ord(m[3]) - 49 + 1,8,1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 4:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("R","r") and ord(m[1]) in range(97,105) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for f in range(ord(m[2]) - 97 - 1,-1,-1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 4 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[f][ord(m[3]) - 49] == turn[0] * 10 + 4 and f != ord(m[1]) - 97):
				break
		for f in range(ord(m[2]) - 97 + 1,8,1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 4 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[f][ord(m[3]) - 49] == turn[0] * 10 + 4 and f != ord(m[1]) - 97):
				break
		if m[1] == m[2]:
			return "disambiguation required"
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r f dis"
			PorC = 1
	if len(m) == 5 and m[0] in ("R","r") and ord(m[1]) in range(97,105) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for f in range(ord(m[3]) - 97 - 1,-1,-1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 4 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 4 and f != ord(m[1]) - 97):
				break
		for f in range(ord(m[3]) - 97 + 1,8,1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 4 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 4 and f != ord(m[1]) - 97):
				break
		if m[1] == m[3]:
			return "disambiguation required"
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r f dis cap"
			PorC = 2
	if len(m) == 4 and m[0] in ("R","r") and ord(m[1]) in range(49,57) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for r in range(ord(m[3]) - 49 - 1,-1,-1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 4 and r == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[ord(m[2]) - 97][r] == turn[0] * 10 + 4 and r != ord(m[1]) - 49):
				break
		for r in range(ord(m[3]) - 49 + 1,8,1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 4 and r == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[ord(m[2]) - 97][r] == turn[0] * 10 + 4 and r != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r r dis"
			PorC = 1
	if len(m) == 5 and m[0] in ("R","r") and ord(m[1]) in range(49,57) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for r in range(ord(m[4]) - 49 - 1,-1,-1):
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 4 and r == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 4 and r != ord(m[1]) - 49):
				break
		for r in range(ord(m[4]) - 49 + 1,8,1):
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 4 and r == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,5,15,6,16,(turn[0] + 1) % 2 * 10 + 4) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 4 and r != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 4
			positions.append(deepcopy(board))
			moveType = "r r dis cap"
			PorC = 2
	if len(m) == 3 and m[0] in ("Q","q") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and not board[ord(m[1]) - 97][ord(m[2]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for i in range(1,8):
			if ord(m[1]) - 97 + i not in range(8) or ord(m[2]) - 49 + i not in range(8):
				break
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 + i] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97 + i,ord(m[2]) - 49 + i))
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 + i not in range(8) or ord(m[2]) - 49 - i not in range(8):
				break
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 - i] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97 + i,ord(m[2]) - 49 - i))
			if board[ord(m[1]) - 97 + i][ord(m[2]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 - i not in range(8) or ord(m[2]) - 49 + i not in range(8):
				break
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 + i] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97 - i,ord(m[2]) - 49 + i))
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[1]) - 97 - i not in range(8) or ord(m[2]) - 49 - i not in range(8):
				break
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 - i] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97 - i,ord(m[2]) - 49 - i))
			if board[ord(m[1]) - 97 - i][ord(m[2]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for f in range(ord(m[1]) - 97 - 1,-1,-1):
			if board[f][ord(m[2]) - 49] == turn[0] * 10 + 5:
				pCand.append((f,ord(m[2]) - 49))
			if board[f][ord(m[2]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for f in range(ord(m[1]) - 97 + 1,8,1):
			if board[f][ord(m[2]) - 49] == turn[0] * 10 + 5:
				pCand.append((f,ord(m[2]) - 49))
			if board[f][ord(m[2]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for r in range(ord(m[2]) - 49 - 1,-1,-1):
			if board[ord(m[1]) - 97][r] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97,r))
			if board[ord(m[1]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for r in range(ord(m[2]) - 49 + 1,8,1):
			if board[ord(m[1]) - 97][r] == turn[0] * 10 + 5:
				pCand.append((ord(m[1]) - 97,r))
			if board[ord(m[1]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[1]) - 97][ord(m[2]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("Q","q") and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and board[ord(m[2]) - 97][ord(m[3]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for i in range(1,8):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for i in range(1,8):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for f in range(ord(m[2]) - 97 - 1,-1,-1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 5:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for f in range(ord(m[2]) - 97 + 1,8,1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 5:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for r in range(ord(m[3]) - 49 - 1,-1,-1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		for r in range(ord(m[3]) - 49 + 1,8,1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 5:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("Q","q") and ord(m[1]) in range(97,105) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[2]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[2]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[2]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[2]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[2]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[2]) - 97 - i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[2]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[2]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[2]) - 97 - i != ord(m[1]) - 97):
				break
		for f in range(ord(m[2]) - 97 - 1,-1,-1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 5 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[3]) - 49] == turn[0] * 10 + 5 and f != ord(m[1]) - 97):
				break
		for f in range(ord(m[2]) - 97 + 1,8,1):
			if board[f][ord(m[3]) - 49] == turn[0] * 10 + 5 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[3]) - 49))
			if board[f][ord(m[3]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[3]) - 49] == turn[0] * 10 + 5 and f != ord(m[1]) - 97):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q f dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("Q","q") and ord(m[1]) in range(97,105) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i != ord(m[1]) - 97):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i == ord(m[1]) - 97:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i != ord(m[1]) - 97):
				break
		for f in range(ord(m[3]) - 97 - 1,-1,-1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and f != ord(m[1]) - 97):
				break
		for f in range(ord(m[3]) - 97 + 1,8,1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and f == ord(m[1]) - 97:
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and f != ord(m[1]) - 97):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q f dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 4 and m[0] in ("Q","q") and ord(m[1]) in range(49,57) and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and not board[ord(m[2]) - 97][ord(m[3]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 + i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 + i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 + i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 49 - i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 + i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 + i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[3]) - ord(m[1])) + 1):
			if ord(m[2]) - 97 - i not in range(8) or ord(m[3]) - 49 - i not in range(8):
				break
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97 - i,ord(m[3]) - 49 - i))
			if board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97 - i][ord(m[3]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 49 - i != ord(m[1]) - 49):
				break
		for r in range(ord(m[3]) - 49 - 1,-1,-1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 5 and r == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97][r] == turn[0] * 10 + 5 and r != ord(m[1]) - 49):
				break
		for r in range(ord(m[3]) - 49 + 1,8,1):
			if board[ord(m[2]) - 97][r] == turn[0] * 10 + 5 and r == ord(m[1]) - 49:
				pCand.append((ord(m[2]) - 97,r))
			if board[ord(m[2]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[2]) - 97][r] == turn[0] * 10 + 5 and r != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q r dis"
			PorC = 1
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("Q","q") and ord(m[1]) in range(49,57) and m[2] in ("X","x") and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[3]) - 97][ord(m[4]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[4]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[4]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[4]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[4]) - 49 - i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[4]) - 49 + i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[4]) - 49 + i != ord(m[1]) - 49):
				break
		for i in range(1,abs(ord(m[4]) - ord(m[1])) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[4]) - 49 - i == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[4]) - 49 - i != ord(m[1]) - 49):
				break
		for r in range(ord(m[4]) - 49 - 1,-1,-1):
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and r == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and r != ord(m[1]) - 49):
				break
		for r in range(ord(m[4]) - 49 + 1,8,1):
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and r == ord(m[1]) - 49:
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and r != ord(m[1]) - 49):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q r dis cap"
			PorC = 2
		if len(pCand) > 1:
			return "disambiguation required"
	if len(m) == 5 and m[0] in ("Q","q") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and ord(m[3]) in range(97,105) and ord(m[4]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 5 and not board[ord(m[3]) - 97][ord(m[4]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for i in range(1,min(abs(ord(m[4]) - ord(m[2])),abs(ord(m[3]) - ord(m[1]))) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i == ord(m[1]) - 97 and ord(m[4]) - 49 + i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[3]) - 97 + i != ord(m[1]) - 97 or ord(m[4]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[4]) - ord(m[2])),abs(ord(m[3]) - ord(m[1]))) + 1):
			if ord(m[3]) - 97 + i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 97 + i == ord(m[1]) - 97 and ord(m[4]) - 49 - i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 + i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 + i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[3]) - 97 + i != ord(m[1]) - 97 or ord(m[4]) - 49 - i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[4]) - ord(m[2])),abs(ord(m[3]) - ord(m[1]))) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 + i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i == ord(m[1]) - 97 and ord(m[4]) - 49 + i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 + i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[3]) - 97 - i != ord(m[1]) - 97 or ord(m[4]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[4]) - ord(m[2])),abs(ord(m[3]) - ord(m[1]))) + 1):
			if ord(m[3]) - 97 - i not in range(8) or ord(m[4]) - 49 - i not in range(8):
				break
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and ord(m[3]) - 97 - i == ord(m[1]) - 97 and ord(m[4]) - 49 - i == ord(m[2]) - 49:
				pCand.append((ord(m[3]) - 97 - i,ord(m[4]) - 49 - i))
			if board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97 - i][ord(m[4]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[3]) - 97 - i != ord(m[1]) - 97 or ord(m[4]) - 49 - i != ord(m[2]) - 49)):
				break
		for f in range(ord(m[3]) - 97 - 1,-1,-1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and (f == ord(m[1]) - 97 and ord(m[4]) - 49 == ord(m[2]) - 49):
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and (f != ord(m[1]) - 49 or ord(m[4]) - 49 != ord(m[2]) - 49)):
				break
		for f in range(ord(m[3]) - 97 + 1,8,1):
			if board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and (f == ord(m[1]) - 97 and ord(m[4]) - 49 == ord(m[2]) - 49):
				pCand.append((f,ord(m[4]) - 49))
			if board[f][ord(m[4]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[4]) - 49] == turn[0] * 10 + 5 and (f != ord(m[1]) - 49 or ord(m[4]) - 49 != ord(m[2]) - 49)):
				break
		for r in range(ord(m[4]) - 49 - 1,-1,-1):
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and (ord(m[3]) - 97 == ord(m[1]) - 97 and r == ord(m[2]) - 49):
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and (ord(m[3]) - 97 != ord(m[1]) - 97 or r != ord(m[2]) - 49)):
				break
		for r in range(ord(m[4]) - 49 + 1,8,1):
			print(r)
			if board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and (ord(m[3]) - 97 == ord(m[1]) - 97 and r == ord(m[2]) - 49):
				pCand.append((ord(m[3]) - 97,r))
			if board[ord(m[3]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[3]) - 97][r] == turn[0] * 10 + 5 and (ord(m[3]) - 97 != ord(m[1]) - 97 or r != ord(m[2]) - 49)):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[3]) - 97][ord(m[4]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q f r dis"
			PorC = 1
	if len(m) == 6 and m[0] in ("Q","q") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and m[3] in ("X","x") and ord(m[4]) in range(97,105) and ord(m[5]) in range(49,57) and board[ord(m[1]) - 97][ord(m[2]) - 49] == turn[0] * 10 + 5 and board[ord(m[4]) - 97][ord(m[5]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for i in range(1,min(abs(ord(m[5]) - ord(m[2])),abs(ord(m[4]) - ord(m[1]))) + 1):
			if ord(m[4]) - 97 + i not in range(8) or ord(m[5]) - 49 + i not in range(8):
				break
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 + i == ord(m[1]) - 97 and ord(m[5]) - 49 + i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 + i,ord(m[5]) - 49 + i))
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97 + i][ord(m[5]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 + i != ord(m[1]) - 97 or ord(m[5]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[5]) - ord(m[2])),abs(ord(m[4]) - ord(m[1]))) + 1):
			if ord(m[4]) - 97 + i not in range(8) or ord(m[5]) - 49 - i not in range(8):
				break
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 + i == ord(m[1]) - 97 and ord(m[5]) - 49 - i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 + i,ord(m[5]) - 49 - i))
			if board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97 + i][ord(m[5]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 + i != ord(m[1]) - 97 or ord(m[5]) - 49 - i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[5]) - ord(m[2])),abs(ord(m[4]) - ord(m[1]))) + 1):
			if ord(m[4]) - 97 - i not in range(8) or ord(m[5]) - 49 + i not in range(8):
				break
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 - i == ord(m[1]) - 97 and ord(m[5]) - 49 + i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 - i,ord(m[5]) - 49 + i))
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97 - i][ord(m[5]) - 49 + i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 - i != ord(m[1]) - 97 or ord(m[5]) - 49 + i != ord(m[2]) - 49)):
				break
		for i in range(1,min(abs(ord(m[5]) - ord(m[2])),abs(ord(m[4]) - ord(m[1]))) + 1):
			if ord(m[4]) - 97 - i not in range(8) or ord(m[5]) - 49 - i not in range(8):
				break
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 - i == ord(m[1]) - 97 and ord(m[5]) - 49 - i == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97 - i,ord(m[5]) - 49 - i))
			if board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97 - i][ord(m[5]) - 49 - i] == turn[0] * 10 + 5 and (ord(m[4]) - 97 - i != ord(m[1]) - 97 or ord(m[5]) - 49 - i != ord(m[2]) - 49)):
				break
		for f in range(ord(m[4]) - 97 - 1,-1,-1):
			if board[f][ord(m[5]) - 49] == turn[0] * 10 + 5 and (f == ord(m[1]) - 97 and ord(m[5]) - 49 == ord(m[2]) - 49):
				pCand.append((f,ord(m[5]) - 49))
			if board[f][ord(m[5]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[5]) - 49] == turn[0] * 10 + 5 and (f != ord(m[1]) - 97 or ord(m[5]) - 49 != ord(m[2]) - 49)):
				break
		for f in range(ord(m[4]) - 97 + 1,8,1):
			if board[f][ord(m[5]) - 49] == turn[0] * 10 + 5 and (f == ord(m[1]) - 97 and ord(m[5]) - 49 == ord(m[2]) - 49):
				pCand.append((f,ord(m[5]) - 49))
			if board[f][ord(m[5]) - 49] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[f][ord(m[5]) - 49] == turn[0] * 10 + 5 and (f != ord(m[1]) - 97 or ord(m[5]) - 49 != ord(m[2]) - 49)):
				break
		for r in range(ord(m[5]) - 49 - 1,-1,-1):
			if board[ord(m[4]) - 97][r] == turn[0] * 10 + 5 and (ord(m[4]) - 97 == ord(m[1]) - 97 and r == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97,r))
			if board[ord(m[4]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97][r] == turn[0] * 10 + 5 and (ord(m[4]) - 97 != ord(m[1]) - 97 or r != ord(m[2]) - 49)):
				break
		for r in range(ord(m[5]) - 49 + 1,8,1):
			if board[ord(m[4]) - 97][r] == turn[0] * 10 + 5 and (ord(m[4]) - 97 == ord(m[1]) - 97 and r == ord(m[2]) - 49):
				pCand.append((ord(m[4]) - 97,r))
			if board[ord(m[4]) - 97][r] in (1,11,2,12,3,13,4,14,6,16,(turn[0] + 1) % 2 * 10 + 5) or (board[ord(m[4]) - 97][r] == turn[0] * 10 + 5 and (ord(m[4]) - 97 != ord(m[1]) - 97 or r != ord(m[2]) - 49)):
				break
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[4]) - 97][ord(m[5]) - 49] = turn[0] * 10 + 5
			positions.append(deepcopy(board))
			moveType = "q f r dis cap"
			PorC = 2
	if len(m) == 3 and m[0] in ("K","k") and ord(m[1]) in range(97,105) and ord(m[2]) in range(49,57) and not board[ord(m[1]) - 97][ord(m[2]) - 49] in (turn[0] * 10 + 1,turn[0] * 10 + 2,turn[0] * 10 + 3,turn[0] * 10 + 4,turn[0] * 10 + 5,turn[0] * 10 + 6):
		pCand = []
		for f in range(ord(m[1]) - 97 - 1, ord(m[1]) - 97 + 2):
			for r in range(ord(m[2]) - 49 - 1,ord(m[2]) - 49 + 2):
				if f in range(8) and r in range(8) and board[f][r] == turn[0] * 10 + 6:
					pCand.append((f,r))
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[1]) - 97][ord(m[2]) - 49] = turn[0] * 10 + 6
			positions.append(deepcopy(board))
			moveType = "k"
			PorC = 1
	if len(m) == 4 and m[0] in ("K","k") and m[1] in ("X","x") and ord(m[2]) in range(97,105) and ord(m[3]) in range(49,57) and board[ord(m[2]) - 97][ord(m[3]) - 49] in ((turn[0] + 1) % 2 * 10 + 1,(turn[0] + 1) % 2 * 10 + 2,(turn[0] + 1) % 2 * 10 + 3,(turn[0] + 1) % 2 * 10 + 4,(turn[0] + 1) % 2 * 10 + 5):
		pCand = []
		for f in range(ord(m[2]) - 97 - 1, ord(m[2]) - 97 + 2):
			for r in range(ord(m[3]) - 49 - 1,ord(m[3]) - 49 + 2):
				if f in range(8) and r in range(8) and board[f][r] == turn[0] * 10 + 6:
					pCand.append((f,r))		
		if len(pCand) == 1:
			board[pCand[0][0]][pCand[0][1]] = 0
			board[ord(m[2]) - 97][ord(m[3]) - 49] = turn[0] * 10 + 6
			positions.append(deepcopy(board))
			moveType = "k cap"
			PorC = 2
	if moveType == "":
		return "not possible"
	for f in range(8):
		for r in range(8):
			if board[f][r] == turn[0] * 10 + 6:
				if inCheck(turn[0],f,r,board)[0]:
					positions.pop(-1)
					board = deepcopy(positions[-1])
					if check == "":
						gBoard = deepcopy(positions[-1])
					return "illegal move"
				else:
					turn[0] = (turn[0] + 1) % 2
					return PorC

def possibleMoves(player):
	moves = []
	if not move("O-O","check") in ("not possible","illegal move"):
		moves.append("O-O")
	if not move("O-O-O","check") in ("not possible","illegal move"):
		moves.append("O-O-O")
	allN = []
	allB = []
	diagB = []
	allR = []
	fileR = []
	rankR = []
	allQ = []
	diagQ = []
	fileQ = []
	rankQ = []
	kFile = -1
	kRank = -1
	for f in range(8):
		for r in range(8):
			if gBoard[f][r] == 1 and player == 0:
				if not move(chr(f + 97) + chr(r + 49 + 1),"check") in ("not possible","illegal move"):
					if r + 1 == 7:
						moves.append(chr(f + 97) + chr(r + 49 + 1) + "=N")
						moves.append(chr(f + 97) + chr(r + 49 + 1) + "=B")
						moves.append(chr(f + 97) + chr(r + 49 + 1) + "=R")
						moves.append(chr(f + 97) + chr(r + 49 + 1) + "=Q")
					else:
						moves.append(chr(f + 97) + chr(r + 49 + 1))
				if not move(chr(f + 97) + chr(r + 49 + 2),"check") in ("not possible","illegal move"):
						moves.append(chr(f + 97) + chr(r + 49 + 2))
				if not move(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1),"check") in ("not possible","illegal move"):
					if r + 1 == 7:
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1) + "=N")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1) + "=B")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1) + "=R")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1) + "=Q")
					else:
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 + 1))
				if not move(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1),"check") in ("not possible","illegal move"):
					if r + 1 == 7:
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1) + "=N")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1) + "=B")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1) + "=R")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1) + "=Q")
					else:
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 + 1))
			elif gBoard[f][r] == 11 and player == 1:
				if not move(chr(f + 97) + chr(r + 49 - 1),"check") in ("not possible","illegal move"):
					if r - 1 == 0:
						moves.append(chr(f + 97) + chr(r + 49 - 1) + "=N")
						moves.append(chr(f + 97) + chr(r + 49 - 1) + "=B")
						moves.append(chr(f + 97) + chr(r + 49 - 1) + "=R")
						moves.append(chr(f + 97) + chr(r + 49 - 1) + "=Q")
					else:
						moves.append(chr(f + 97) + chr(r + 49 - 1))
				if not move(chr(f + 97) + chr(r + 49 - 2),"check") in ("not possible","illegal move"):
					moves.append(chr(f + 97) + chr(r + 49 - 2))
				if not move(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1),"check") in ("not possible","illegal move"):
					if r - 1 == 0:
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1) + "=N")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1) + "=B")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1) + "=R")
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1) + "=Q")
					else:
						moves.append(chr(f + 97) + "x" + chr(f + 97 + 1) + chr(r + 49 - 1))
				if not move(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1),"check") in ("not possible","illegal move"):
					if r - 1 == 0:
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1) + "=N")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1) + "=B")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1) + "=R")
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1) + "=Q")
					else:
						moves.append(chr(f + 97) + "x" + chr(f + 97 - 1) + chr(r + 49 - 1))
			elif gBoard[f][r] == player * 10 + 2:
				(pieceState,direction) = pinCheck(f,r,player)
				if pieceState == "no pin":
					allN.append((f,r))
			elif gBoard[f][r] == player * 10 + 3:
				(pieceState,direction) = pinCheck(f,r,player)
				if pieceState == "no pin":
					allB.append((f,r))
				if pieceState == "diag pin":
					diagB.append((f,r),direction)
			elif gBoard[f][r] == player * 10 + 4:
				(pieceState,direction) = pinCheck(f,r,player)
				if pieceState == "no pin":
					allR.append((f,r))
				if pieceState == "file pin":
					fileR.append((f,r))
				if pieceState == "rank pin":
					rankR.append((f,r))
			elif gBoard[f][r] == player * 10 + 5:
				(pieceState,direction) = pinCheck(f,r,player)
				if pieceState == "no pin":
					allQ.append((f,r))
				if pieceState == "diag pin":
					diagQ.append((f,r),direction)
				if pieceState == "file pin":
					fileQ.append((f,r))
				if pieceState == "rank pin":
					rankQ.append((f,r))
			elif gBoard[f][r] == player * 10 + 6:
				kFile = f
				kRank = r
				for file in range(f - 1,f + 2):
					for rank in range(r - 1,r + 2):
						if not file in range(8) or not rank in range(8):
							continue
						if move("K" + chr(file + 97) + chr(rank + 49),"check") == "not possible":
							continue
						if not move("K" + chr(file + 97) + chr(rank + 49),"check") == "illegal move":
							if gBoard[file][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
								moves.append("K" + "x" + chr(file + 97) + chr(rank + 49))
							else:
								moves.append("K" + chr(file + 97) + chr(rank + 49))
	nMoves = []
	bMoves = []
	rMoves = []
	qMoves = []
	for (f,r) in allN:
		if not f + 2 in range(8) or not r + 1 in range(8):
			pass
		elif gBoard[f + 2][r + 1] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f + 2][r + 1] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 2) + chr(r + 49 + 1) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 2) + chr(r + 49 + 1) + "o")
		if not f + 2 in range(8) or not r - 1 in range(8):
			pass
		elif gBoard[f + 2][r - 1] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f + 2][r - 1] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 2) + chr(r + 49 - 1) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 2) + chr(r + 49 - 1) + "o")
		if not f + 1 in range(8) or not r + 2 in range(8):
			pass
		elif gBoard[f + 1][r + 2] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f + 1][r + 2] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 1) + chr(r + 49 + 2) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 1) + chr(r + 49 + 2) + "o")
		if not f + 1 in range(8) or not r - 2 in range(8):
			pass
		elif gBoard[f + 1][r - 2] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f + 1][r - 2] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 1) + chr(r + 49 - 2) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 + 1) + chr(r + 49 - 2) + "o")
		if not f - 1 in range(8) or not r + 2 in range(8):
			pass
		elif gBoard[f - 1][r + 2] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f - 1][r + 2] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 1) + chr(r + 49 + 2) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 1) + chr(r + 49 + 2) + "o")
		if not f - 1 in range(8) or not r - 2 in range(8):
			pass
		elif gBoard[f - 1][r - 2] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f - 1][r - 2] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 1) + chr(r + 49 - 2) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 1) + chr(r + 49 - 2) + "o")
		if not f - 2 in range(8) or not r + 1 in range(8):
			pass
		elif gBoard[f - 2][r + 1] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f - 2][r + 1] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 2) + chr(r + 49 + 1) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 2) + chr(r + 49 + 1) + "o")
		if not f - 2 in range(8) or not r - 1 in range(8):
			pass
		elif gBoard[f - 2][r - 1] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
			pass
		elif gBoard[f - 2][r - 1] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 2) + chr(r + 49 - 1) + "x")
		else:
			nMoves.append("N" + chr(f + 97) + chr(r + 49) + chr(f + 97 - 2) + chr(r + 49 - 1) + "o")
	for (f,r) in allB:
		for i in range(1,8):
			if f + i not in range(8) or r + i not in range(8):
				break
			elif gBoard[f + i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f + i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "x")
				break
			else:
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "o")
		for i in range(1,8):
			if f + i not in range(8) or r - i not in range(8):
				break
			elif gBoard[f + i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f + i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "x")
				break
			else:
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "o")
		for i in range(1,8):
			if f - i not in range(8) or r + i not in range(8):
				break
			elif gBoard[f - i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f - i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "x")
				break
			else:
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "o")
		for i in range(1,8):
			if f - i not in range(8) or r - i not in range(8):
				break
			elif gBoard[f - i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f - i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "x")
				break
			else:
				bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "o")
	for ((f,r),direction) in diagB:
		if direction == "+":
			for i in range(1,8):
				if f + i not in range(8) or r + i not in range(8):
					break
				elif gBoard[f + i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f + i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "x")
					break
				else:
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "o")
			for i in range(1,8):
				if f - i not in range(8) or r - i not in range(8):
					break
				elif gBoard[f - i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f - i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "x")
					break
				else:
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "o")
		elif direction == "-":
			for i in range(1,8):
				if f + i not in range(8) or r - i not in range(8):
					break
				elif gBoard[f + i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f + i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "x")
					break
				else:
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "o")
			for i in range(1,8):
				if f - i not in range(8) or r + i not in range(8):
					break
				elif gBoard[f - i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f - i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "x")
					break
				else:
					bMoves.append("B" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "o")
	for (f,r) in allR:
		for file in range(f + 1,8,1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for file in range(f - 1,-1,-1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for rank in range(r + 1,8,1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
		for rank in range(r - 1,-1,-1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
	for (f,r) in fileR:
		for file in range(f + 1,8,1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for file in range(f - 1,-1,-1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
	for (f,r) in rankR:
		for rank in range(r + 1,8,1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
		for rank in range(r - 1,-1,-1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				rMoves.append("R" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
	for (f,r) in allQ:
		for i in range(1,8):
			if f + i not in range(8) or r + i not in range(8):
				break
			elif gBoard[f + i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f + i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "o")
		for i in range(1,8):
			if f + i not in range(8) or r - i not in range(8):
				break
			elif gBoard[f + i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f + i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "o")
		for i in range(1,8):
			if f - i not in range(8) or r + i not in range(8):
				break
			elif gBoard[f - i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f - i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "o")
		for i in range(1,8):
			if f - i not in range(8) or r - i not in range(8):
				break
			elif gBoard[f - i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f - i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "o")
		for file in range(f + 1,8,1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for file in range(f - 1,-1,-1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for rank in range(r + 1,8,1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
		for rank in range(r - 1,-1,-1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
	for ((f,r),direction) in diagQ:
		if direction == "+":
			for i in range(1,8):
				if f + i not in range(8) or r + i not in range(8):
					break
				elif gBoard[f + i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f + i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "x")
					break
				else:
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 + i) + "o")
			for i in range(1,8):
				if f - i not in range(8) or r - i not in range(8):
					break
				elif gBoard[f - i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f - i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "x")
					break
				else:
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 - i) + "o")
		elif direction == "-":
			for i in range(1,8):
				if f + i not in range(8) or r - i not in range(8):
					break
				elif gBoard[f + i][r - i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f + i][r - i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "x")
					break
				else:
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 + i) + chr(r + 49 - i) + "o")
			for i in range(1,8):
				if f - i not in range(8) or r + i not in range(8):
					break
				elif gBoard[f - i][r + i] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
					break
				elif gBoard[f - i][r + i] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "x")
					break
				else:
					qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97 - i) + chr(r + 49 + i) + "o")
	for (f,r) in fileQ:
		for file in range(f + 1,8,1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
		for file in range(f - 1,-1,-1):
			if gBoard[file][r] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[file][r] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(file + 97) + chr(r + 49) + "o")
	for (f,r) in rankQ:
		for rank in range(r + 1,8,1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
		for rank in range(r - 1,-1,-1):
			if gBoard[f][rank] in (player * 10 + 1,player * 10 + 2,player * 10 + 3,player * 10 + 4,player * 10 + 5,player * 10 + 6):
				break
			elif gBoard[f][rank] in ((player + 1) % 2 * 10 + 1,(player + 1) % 2 * 10 + 2,(player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "x")
				break
			else:
				qMoves.append("Q" + chr(f + 97) + chr(r + 49) + chr(f + 97) + chr(rank + 49) + "o")
	moveLists = [nMoves,bMoves,rMoves,qMoves]
	checkList = inCheck(player,kFile,kRank)
	if checkList[0] == True:
		inBetween = []
		if checkList[1] == "diag":
			fdir = int(abs(checkList[2][0] - kFile) / (checkList[2][0] - kFile))
			rdir = int(abs(checkList[2][1] - kRank) / (checkList[2][1] - kRank))
			for i in range(1,abs(checkList[2][0] - kFile) + 1):
				inBetween.append(chr(int(kFile + fdir * i + 97)) + chr(int(kRank + rdir * i + 49)))
		elif checkList[1] == "file":
			fdir = int(abs(checkList[2][0] - kFile) / (checkList[2][0] - kFile))
			for i in range(checkList[2][0],kFile,-fdir):
				inBetween.append(chr(i + 97) + chr(kRank + 49))
		elif checkList[1] == "rank":
			rdir = int(abs(checkList[2][1] - kRank) / (checkList[2][1] - kRank))
			for i in range(checkList[2][1],kRank,-rdir):
				inBetween.append(chr(kFile + 97) + chr(i + 49))
		elif checkList[1] in ("pawn","knight"):
			inBetween.append(chr(checkList[2][0] + 97) + chr(checkList[2][1] + 49))
		elif checkList[1] in ("double"):
			return moves
		for l in moveLists:
			for i in range(len(l) - 1,-1,-1):
				if not l[i][3:5] in inBetween:
					l.pop(i)
	print(checkList)
	while len(nMoves) > 0:
		tempN = []
		tempN.append(nMoves.pop(0))
		for i in range(len(nMoves) - 1,-1,-1):
			if tempN[0][3:5] == nMoves[i][3:5]:
				tempN.append(nMoves.pop(i))
		if len(tempN) == 1:
			if tempN[0][5] == "x":
				moves.append(tempN[0][0] + "x" + tempN[0][3:5])
			else:
				moves.append(tempN[0][0] + tempN[0][3:5])
		if len(tempN) > 1:
			for i in range(len(tempN)):
				fdis = True
				for j in range(len(tempN)):
					if tempN[i][1] == tempN[j][1] and i != j:
						fdis = False
						break
				if fdis == True:
					if tempN[i][5] == "x":
						moves.append(tempN[i][0:2] + "x" + tempN[i][3:5])
					else:
						moves.append(tempN[i][0:2] + tempN[i][3:5])
				if fdis == False:
					rdis = True
					for j in range(len(tempN)):
						if tempN[i][2] == tempN[j][2] and i != j:
							rdis = False
							break
					if rdis == True:
						if tempN[i][5] == "x":
							moves.append(tempN[i][0] + tempN[i][2] + "x" + tempN[i][3:5])
						else:
							moves.append(tempN[i][0] + tempN[i][2] + tempN[i][3:5])
					if rdis == False:
						if tempN[i][5] == "x":
							moves.append(tempN[i][0:3] + "x" + tempN[i][3:5])
						else:
							moves.append(tempN[i][0:5])
	while len(bMoves) > 0:
		tempB = []
		tempB.append(bMoves.pop(0))
		for i in range(len(bMoves) - 1,-1,-1):
			if tempB[0][3:5] == bMoves[i][3:5]:
				tempB.append(bMoves.pop(i))
		if len(tempB) == 1:
			if tempB[0][5] == "x":
				moves.append(tempB[0][0] + "x" + tempB[0][3:5])
			else:
				moves.append(tempB[0][0] + tempB[0][3:5])
		if len(tempB) > 1:
			for i in range(len(tempB)):
				fdis = True
				for j in range(len(tempB)):
					if tempB[i][1] == tempB[j][1] and i != j:
						fdis = False
						break
				if fdis == True:
					if tempB[i][5] == "x":
						moves.append(tempB[i][0:2] + "x" + tempB[i][3:5])
					else:
						moves.append(tempB[i][0:2] + tempB[i][3:5])
				if fdis == False:
					rdis = True
					for j in range(len(tempB)):
						if tempB[i][2] == tempB[j][2] and i != j:
							rdis = False
							break
					if rdis == True:
						if tempB[i][5] == "x":
							moves.append(tempB[i][0] + tempB[i][2] + "x" + tempB[i][3:5])
						else:
							moves.append(tempB[i][0] + tempB[i][2] + tempB[i][3:5])
					if rdis == False:
						if tempB[i][5] == "x":
							moves.append(tempB[i][0:3] + "x" + tempB[i][3:5])
						else:
							moves.append(tempB[i][0:5])
	while len(rMoves) > 0:
		tempR = []
		tempR.append(rMoves.pop(0))
		for i in range(len(rMoves) - 1,-1,-1):
			if tempR[0][3:5] == rMoves[i][3:5]:
				tempR.append(rMoves.pop(i))
		if len(tempR) == 1:
			if tempR[0][5] == "x":
				moves.append(tempR[0][0] + "x" + tempR[0][3:5])
			else:
				moves.append(tempR[0][0] + tempR[0][3:5])
		if len(tempR) > 1:
			for i in range(len(tempR)):
				fdis = True
				for j in range(len(tempR)):
					if tempR[i][1] == tempR[j][1] and i != j:
						fdis = False
						break
				if fdis == True:
					if tempR[i][5] == "x":
						moves.append(tempR[i][0:2] + "x" + tempR[i][3:5])
					else:
						moves.append(tempR[i][0:2] + tempR[i][3:5])
				if fdis == False:
					if tempR[i][5] == "x":
						moves.append(tempR[i][0] + tempR[i][2] + "x" + tempR[i][3:5])
					else:
						moves.append(tempR[i][0] + tempR[i][2] + tempR[i][3:5])
	while len(qMoves) > 0:
		tempQ = []
		tempQ.append(qMoves.pop(0))
		for i in range(len(qMoves) - 1,-1,-1):
			if tempQ[0][3:5] == qMoves[i][3:5]:
				tempQ.append(qMoves.pop(i))
		if len(tempQ) == 1:
			if tempQ[0][5] == "x":
				moves.append(tempQ[0][0] + "x" + tempQ[0][3:5])
			else:
				moves.append(tempQ[0][0] + tempQ[0][3:5])
		if len(tempQ) > 1:
			for i in range(len(tempQ)):
				fdis = True
				for j in range(len(tempQ)):
					if tempQ[i][1] == tempQ[j][1] and i != j:
						fdis = False
						break
				if fdis == True:
					if tempQ[i][5] == "x":
						moves.append(tempQ[i][0:2] + "x" + tempQ[i][3:5])
					else:
						moves.append(tempQ[i][0:2] + tempQ[i][3:5])
				if fdis == False:
					rdis = True
					for j in range(len(tempQ)):
						if tempQ[i][2] == tempQ[j][2] and i != j:
							rdis = False
							break
					if rdis == True:
						if tempQ[i][5] == "x":
							moves.append(tempQ[i][0] + tempQ[i][2] + "x" + tempQ[i][3:5])
						else:
							moves.append(tempQ[i][0] + tempQ[i][2] + tempQ[i][3:5])
					if rdis == False:
						if tempQ[i][5] == "x":
							moves.append(tempQ[i][0:3] + "x" + tempQ[i][3:5])
						else:
							moves.append(tempQ[i][0:5])
	return moves

def inCheck(player,file,rank,board = gBoard):
	inCheck = False
	checkType = ""
	checkPiecePos = (-1,-1)
	for f in range(file - 1,file + 2):
		for r in range(rank - 1,rank + 2):
			if f in range(8) and r in range(8) and board[f][r] == (player + 1) % 2 * 10 + 6:
				if inCheck == False:
					inCheck = True
					checkType = "king"
					checkPiecePos = (f,r)
				else:
					return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank + 1 in range(8) and board[file + 1][rank + 1] == 11 and player == 0:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file + 1,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank + 1 in range(8) and board[file - 1][rank + 1] == 11 and player == 0:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file - 1,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank - 1 in range(8) and board[file + 1][rank - 1] == 1 and player == 1:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file + 1,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank - 1 in range(8) and board[file - 1][rank - 1] == 1 and player == 1:
		if inCheck == False:
			inCheck = True
			checkType = "pawn"
			checkPiecePos = (file - 1,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file + 2 in range(8) and rank + 1 in range(8) and board[file + 2][rank + 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 2,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file + 2 in range(8) and rank - 1 in range(8) and board[file + 2][rank - 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 2,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank + 2 in range(8) and board[file + 1][rank + 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 1,rank + 2)
		else:
			return (True,"double",(-1,-1))
	if file + 1 in range(8) and rank - 2 in range(8) and board[file + 1][rank - 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file + 1,rank - 2)
		else:
			return (True,"double",(-1,-1))
	if file - 2 in range(8) and rank + 1 in range(8) and board[file - 2][rank + 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 2,rank + 1)
		else:
			return (True,"double",(-1,-1))
	if file - 2 in range(8) and rank - 1 in range(8) and board[file - 2][rank - 1] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 2,rank - 1)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank + 2 in range(8) and board[file - 1][rank + 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 1,rank + 2)
		else:
			return (True,"double",(-1,-1))
	if file - 1 in range(8) and rank - 2 in range(8) and board[file - 1][rank - 2] == (player + 1) % 2 * 10 + 2:
		if inCheck == False:
			inCheck = True
			checkType = "knight"
			checkPiecePos = (file - 1,rank - 2)
		else:
			return (True,"double",(-1,-1))
	for f in range(file - 1,-1,-1):
		if board[f][rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[f][rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "file"
				checkPiecePos = (f,rank)
			else:
				return (True,"double",(-1,-1))
	for f in range(file + 1,8,1):
		if board[f][rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[f][rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "file"
				checkPiecePos = (f,rank)
			else:
				return (True,"double",(-1,-1))
	for r in range(rank - 1,-1,-1):
		if board[file][r] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[file][r] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "rank"
				checkPiecePos = (file,r)
			else:
				return (True,"double",(-1,-1))
	for r in range(rank + 1,8,1):
		if board[file][r] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
		if board[file][r] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "rank"
				checkPiecePos = (file,r)
			else:
				return (True,"double",(-1,-1))
	for i in range(1,8):
		if file + i not in range(8) or rank + i not in range(8):
			break
		if board[file + i][rank + i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file + i,rank + i)
			else:
				return (True,"double",(-1,-1))
		if board[file + i][rank + i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file + i not in range(8) or rank - i not in range(8):
			break
		if board[file + i][rank - i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file + i,rank - i)
			else:
				return (True,"double",(-1,-1))
		if board[file + i][rank - i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file - i not in range(8) or rank + i not in range(8):
			break
		if board[file - i][rank + i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file - i,rank + i)
			else:
				return (True,"double",(-1,-1))
		if board[file - i][rank + i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	for i in range(1,8):
		if file - i not in range(8) or rank - i not in range(8):
			break
		if board[file - i][rank - i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
			if inCheck == False:
				inCheck = True
				checkType = "diag"
				checkPiecePos = (file - i,rank - i)
			else:
				return (True,"double",(-1,-1))
		if board[file - i][rank - i] in (1,11,2,12,4,14,player * 10 + 3,player * 10 + 5,(player + 1) % 2 * 10 + 6):
			break
	return (inCheck,checkType,checkPiecePos)

def pinCheck(player,file,rank):
	kFile = 0
	kRank = 0
	for f in range(8):
		for r in range(8):
			if gBoard[f][r] == player * 10 + 6:
				kFile = f
				kRank = r
				break
	if file == kFile and rank == kRank:
		return ("no pin","0")
	if abs(file - kFile) == abs(rank - kRank):
		fdir = int(abs(file - kFile) / (file - kFile))
		rdir = int(abs(rank - kRank) / (rank - kRank))
		for i in range(1,abs(file - kFile) + 1):
				if not gBoard[file - fdir * i][rank - rdir * i] in (0,7,17):
					return ("no pin","0")
		for i in range(1,8):
			if not file - fdir * i in range(8) or not rank - rdir * i in range(8):
				break
			if gBoard[file - fdir * i][rank - rdir * i] in (1,11,2,12,player * 10 + 3,4,14,player * 10 + 5):
				break
			if gBoard[file - fdir * i][rank - rdir * i] in ((player + 1) % 2 * 10 + 3,(player + 1) % 2 * 10 + 5):
				if file - kFile == rank - kRank:
					return ("diag pin","+")
				else:
					return ("diag pin","-")
		return ("no pin","0")
	elif file == kFile:
		dir = int(abs(rank - kRank) / (rank - kRank))
		for i in range(rank + 1,kRank):
			if not gBoard[file][i] in (0,7,17):
				return ("no pin","0")
		for i in range(rank + dir,int(dir * 4.5 + 3.5),dir):
			if gBoard[file][i] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5):
				break
			if gBoard[file][i] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				return ("file pin","+")
		return ("no pin","0")
	elif rank == kRank:
		dir = int(abs(file - kFile) / (file - kFile))
		for i in range(file + 1,kFile):
			if not gBoard[i][rank] in (0,7,17):
				return ("no pin","0")
		for i in range(file + dir,int(dir * 4.5 + 3.5),dir):
			if gBoard[i][rank] in (1,11,2,12,3,13,player * 10 + 4,player * 10 + 5):
				break
			if gBoard[i][rank] in ((player + 1) % 2 * 10 + 4,(player + 1) % 2 * 10 + 5):
				return ("rank pin","-")
		return ("no pin","0")
	return ("no pin","0")

drawBoard()

surf = pygame.Surface((400,100))
surf.fill((0,0,0))
surf.set_alpha(100)
screen.blit(surf,surf.get_rect(center=(260,510)))

surf = pygame.Surface((400,100))
surf.fill((100,100,200))
screen.blit(surf,surf.get_rect(center=(250,500)))

font = pygame.font.SysFont('Montserrat', 72).render("vs Computer", False, (0, 100, 0))
screen.blit(font,font.get_rect(center=(250,500)))

surf = pygame.Surface((400,100))
surf.fill((0,0,0))
surf.set_alpha(100)
screen.blit(surf,surf.get_rect(center=(760,510)))

surf = pygame.Surface((400,100))
surf.fill((100,100,200))
screen.blit(surf,surf.get_rect(center=(750,500)))

font = pygame.font.SysFont('Montserrat', 72).render("vs Friend", False, (0, 100, 0))
screen.blit(font,font.get_rect(center=(750,500)))

pygame.display.flip()

running = True
drawCounter = 0
gamemode = 0
while running:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			if event.pos[0] in range(50,450) and event.pos[1] in range(450,550):
				gamemode = 0
				running = False
			elif event.pos[0] in range(550,950) and event.pos[1] in range(450,550):
				gamemode = 1
				running = False
		if event.type == QUIT:
			gameState = "manual stop"
			running = False


drawBoard()
print("Player " + str(gTurn[0]) + "'s Move:")
pMoves = possibleMoves(gTurn[0])
print(pMoves)
m1State = 0
currentMove = ""
running = True
while running:
	for event in pygame.event.get():
		if gamemode == 0 and gTurn[0] == 1:
			currentMove = random.choice(pMoves)
			print(currentMove)
			moveType = move(currentMove)
			if moveType == 1:
				drawCounter += 1
			elif moveType == 2:
				drawCounter = 0
			currentMove = ""
			drawBoard()
			pMoves = possibleMoves(gTurn[0])
			if len(pMoves) == 0:
				for f in range(8):
					for r in range(8):
						if gBoard[f][r] == gTurn[0] * 10 + 6:
							kPos = (f,r)
				if inCheck(gTurn[0],kPos[0],kPos[1])[0]:
					gameState = "checkmate"
					running = False
				else:
					gameState = "stalemate"
					running = False
			if drawCounter >= 100:
				gameState = "50 move draw"
				running = False
			print("Player " + str(gTurn[0]) + "'s Move:")
			print(pMoves)
		if event.type == MOUSEBUTTONDOWN and m1State == 0 and event.pos[0] in range(100,900) and event.pos[1] in range(100,900):
			m1State = 1
			if int(event.pos[0] / 100) - 1 in range(8) and int(-event.pos[1] / 100) + 8 in range(8):
				currentMove += (getPiece.get(gBoard[int(event.pos[0] / 100) - 1][int(-event.pos[1] / 100) + 8]) + chr(int(event.pos[0] / 100) - 1 + 97) + chr(int(-event.pos[1] / 100) + 8 + 49))
		if event.type == MOUSEBUTTONUP and m1State == 1 and event.pos[0] in range(100,900) and event.pos[1] in range(100,900):
			m1State = 0
			if int(event.pos[0] / 100) - 1 in range(8) and int(-event.pos[1] / 100) + 8 in range(8):
				currentMove += (chr(int(event.pos[0] / 100) - 1 + 97) + chr(int(-event.pos[1] / 100) + 8 + 49))
				print(currentMove)
				if currentMove in ("Ke1g1","Ke1h1","Ke8g8","Ke8h8"):
					print("O-O")
					move("O-O")
					drawCounter += 1
				elif currentMove in ("Ke1a1","Ke1b1","Ke1c1","Ke8a8","Ke8b8","Ke8c8"):
					print("O-O-O")
					move("O-O-O")
					drawCounter += 1
				elif gBoard[ord(currentMove[1]) - 97][ord(currentMove[2]) - 49] == 10 * gTurn[0] + 1:
					if abs(ord(currentMove[3]) - ord(currentMove[1])) == 0:
						if ord(currentMove[4]) - 49 == (gTurn[0] + 1) % 2 * 7 and currentMove[3:5] + "=N" in pMoves:
							screen.blit(wPromo,((ord(currentMove[3]) - 97) * 100 + 125,125))
							pygame.display.flip()
							select = False
							while not select:
								mState = 0
								for event in pygame.event.get():
									if event.type == MOUSEBUTTONDOWN and mState == 0:
										mState = 1
										if int((event.pos[0] - 125) / 100) == ord(currentMove[3]) - 97 and int((event.pos[1] - 25) / 100) == 1:
											select = True
											print(currentMove[3:5] + "=Q")
											move(currentMove[3:5] + "=Q")
											drawCounter = 0
										elif int((event.pos[0] - 125) / 100) == ord(currentMove[3]) - 97 and int((event.pos[1] - 25) / 100) == 2:
											select = True
											print(currentMove[3:5] + "=R")
											move(currentMove[3:5] + "=R")
											drawCounter = 0
										elif int((event.pos[0] - 125) / 100) == ord(currentMove[3]) - 97 and int((event.pos[1] - 25) / 100) == 3:
											select = True
											print(currentMove[3:5] + "=B")
											move(currentMove[3:5] + "=B")
											drawCounter = 0
										elif int((event.pos[0] - 125) / 100) == ord(currentMove[3]) - 97 and int((event.pos[1] - 25) / 100) == 4:
											select = True
											print(currentMove[3:5] + "=N")
											move(currentMove[3:5] + "=N")
											drawCounter = 0
						else:
							print(currentMove[3:5])
							move(currentMove[3:5])
							drawCounter = 0
					if abs(ord(currentMove[3]) - ord(currentMove[1])) == 1:
						if ord(currentMove[4]) - 49 == (gTurn[0] + 1) % 2 * 7 and currentMove[1] + "x" + currentMove[3:5] + "=N" in pMoves:
							screen.blit(wPromo,((ord(currentMove[3]) - 97) * 100 + 125,125))
							pygame.display.flip()
							select = False
							while not select:
								mState = 0
								for event in pygame.event.get():
									if event.type == MOUSEBUTTONDOWN and mState == 0:
										mState = 1
										if int((event.pos[0] - 25) / 100) == ord(currentMove[3]) - 97 + 1 and int((event.pos[1] - 25) / 100) == 1:
											select = True
											print(currentMove[1] + "x" + currentMove[3:5] + "=Q")
											move(currentMove[1] + "x" + currentMove[3:5] + "=Q")
											drawCounter = 0
										elif int((event.pos[0] - 25) / 100) == ord(currentMove[3]) - 97 + 1 and int((event.pos[1] - 25) / 100) == 2:
											select = True
											print(currentMove[1] + "x" + currentMove[3:5] + "=R")
											move(currentMove[1] + "x" + currentMove[3:5] + "=R")
											drawCounter = 0
										elif int((event.pos[0] - 25) / 100) == ord(currentMove[3]) - 97 + 1 and int((event.pos[1] - 25) / 100) == 3:
											select = True
											print(currentMove[1] + "x" + currentMove[3:5] + "=B")
											move(currentMove[1] + "x" + currentMove[3:5] + "=B")
											drawCounter = 0
										elif int((event.pos[0] - 25) / 100) == ord(currentMove[3]) - 97 + 1 and int((event.pos[1] - 25) / 100) == 4:
											select = True
											print(currentMove[1] + "x" + currentMove[3:5] + "=N")
											move(currentMove[1] + "x" + currentMove[3:5] + "=N")
											drawCounter = 0
						else:
							print(currentMove[1] + "x" + currentMove[3:5])
							move(currentMove[1] + "x" + currentMove[3:5])
							drawCounter = 0
				elif gBoard[ord(currentMove[1]) - 97][ord(currentMove[2]) - 49] == 10 * gTurn[0] + getPieceNumber.get(currentMove[0]):
					print(currentMove[0] + currentMove[3:5])
					moveType = move(currentMove[0] + currentMove[3:5])
					if moveType == "disambiguation required":
						print(currentMove[0:2] + currentMove[3:5])
						moveType = move(currentMove[0:2] + currentMove[3:5])
						if moveType == "disambiguation required":
							print(currentMove[0] + currentMove[2:5])
							moveType = move(currentMove[0] + currentMove[2:5])
							if moveType == "disambiguation required":
								print(currentMove)
								moveType = move(currentMove)
								if moveType == 1:
									drawCounter += 1
								elif moveType == 2:
									drawCounter = 0
							else:
								if moveType == 1:
									drawCounter += 1
								elif moveType == 2:
									drawCounter = 0
						else:
							if moveType == 1:
								drawCounter += 1
							elif moveType == 2:
								drawCounter = 0
					else:
						if moveType == 1:
							drawCounter += 1
						elif moveType == 2:
							drawCounter = 0
				
				currentMove = ""
				drawBoard()
				pMoves = possibleMoves(gTurn[0])
				if len(pMoves) == 0:
					for f in range(8):
						for r in range(8):
							if gBoard[f][r] == gTurn[0] * 10 + 6:
								kPos = (f,r)
					if inCheck(gTurn[0],kPos[0],kPos[1])[0]:
						gameState = "checkmate"
						running = False
					else:
						gameState = "stalemate"
						running = False
				if drawCounter >= 100:
					gameState = "50 move draw"
					running = False
				print("Player " + str(gTurn[0]) + "'s Move:")
				print(pMoves)
		if event.type == QUIT:
			gameState = "manual stop"
			running = False

print(gameState)