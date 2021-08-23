import pygame
import sys
import Draw
import Controller

pygame.init()

WIDTH = 1000
HEIGHT = 1000
BACKGROUND = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)
pygame.display.set_caption("Super TicTacToeV2")

Draw.draw_board(screen)
controller = Controller.Controller(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            controller.controller(event.pos)

    pygame.display.update()
