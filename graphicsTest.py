import pygame
from pygame.locals import *

gBoard = 	[[ 4, 1, 0, 0, 0, 0,11,14],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 3, 1, 2, 3, 4, 5,11,13],
			 [ 5, 1,15,14,13,12,11,15],
			 [ 6, 1, 0, 0, 0, 0,11,16],
			 [ 3, 1, 0, 0, 0, 0,11,13],
			 [ 2, 1, 0, 0, 0, 0,11,12],
			 [ 4, 1, 0, 0, 0, 0,11,14]]
pygame.init
pygame.font.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Chess")
screen.fill((50,150,100))
background = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\chessBackground.png')
screen.blit(background,(0,0))

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
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False



r'''for f in range(8):
	for r in range(8):
		surf = pygame.Surface((100,100))
		if (f + r) % 2 == 0:
			surf.fill((200,150,100))
		else:
			surf.fill((150,100,0))
		screen.blit(surf,(100 * f + 100,100 * r + 100))
for i in range(9):
	pygame.draw.line(screen,(0,0,0),(100,100 * i + 100),(900,100 * i + 100),5)
for i in range(9):
	pygame.draw.line(screen,(0,0,0),(100 * i + 100,100),(100 * i + 100,900),5)
for i in range(8):
	screen.blit(pygame.font.SysFont('Montserrat', 30).render(chr(i + 49), False, (0, 100, 0)),pygame.font.SysFont('Montserrat', 30).render(chr(i + 49), False, (0, 100, 0)).get_rect(center=(50, -100 * i + 850)))
	screen.blit(pygame.font.SysFont('Montserrat', 30).render(chr(i + 49), False, (0, 100, 0)),pygame.font.SysFont('Montserrat', 30).render(chr(i + 49), False, (0, 100, 0)).get_rect(center=(950, -100 * i + 850)))
for i in range(8):
	screen.blit(pygame.font.SysFont('Montserrat', 30).render(chr(i + 97), False, (0, 100, 0)),pygame.font.SysFont('Montserrat', 30).render(chr(i + 97), False, (0, 100, 0)).get_rect(center=(100 * i + 150,50)))
	screen.blit(pygame.font.SysFont('Montserrat', 30).render(chr(i + 97), False, (0, 100, 0)),pygame.font.SysFont('Montserrat', 30).render(chr(i + 97), False, (0, 100, 0)).get_rect(center=(100 * i + 150,950)))
pygame.display.flip()
running = True
while running:
	for f in range(8):
		for r in range(8):
			if gBoard[f][r] == 1:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whitePawn.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 11:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackPawn.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 2:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whiteKnight.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 12:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackKnight.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 3:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whiteBishop.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 13:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackBishop.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 4:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whiteRook.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 14:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackRook.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 5:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whiteQueen.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 15:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackQueen.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 6:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\whiteKing.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
			if gBoard[f][r] == 16:
				surf = pygame.image.load(r'C:\Users\garre\OneDrive\Desktop\Projects\chess\images\blackKing.png')
				screen.blit(surf,surf.get_rect(center=(100 * f + 150,-100 * r + 850)))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False'''