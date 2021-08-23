import pygame
import Coordinates
import numpy as np

BLACK = (0, 0, 0)
LINE_BOARD_WIDTH = 8
FIG_LINE_WIDTH = 4
LENGTH = 16
BACKGROUND = (255, 255, 255)


def draw_board(screen):
    CENTER = Coordinates.center(screen.get_width(), screen.get_height())
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, BLACK, CENTER, 400, LINE_BOARD_WIDTH)
    pygame.draw.circle(screen, BLACK, CENTER, 300, LINE_BOARD_WIDTH)
    pygame.draw.circle(screen, BLACK, CENTER, 200, LINE_BOARD_WIDTH)
    pygame.draw.circle(screen, BLACK, CENTER, 100, LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (100, 500), (900, 500), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (500, 100), (500, 900), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (500 - 283, 500 - 283), (500 + 283, 500 + 283), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (500 - 283, 500 + 283), (500 + 283, 500 - 283), LINE_BOARD_WIDTH)


def draw_x_from_center_point(screen, center):
    x0, y0 = center
    x, y = LENGTH / 2 / np.sqrt(2), LENGTH / 2 / np.sqrt(2)
    start_1 = (x0 - x, y0 - y)
    end_1 = (x0 + x, y0 + y)
    start_2 = (x0 - x, y0 + y)
    end_2 = (x0 + x, y0 - y)

    pygame.draw.line(screen, BLACK, start_1, end_1, FIG_LINE_WIDTH)
    pygame.draw.line(screen, BLACK, start_2, end_2, FIG_LINE_WIDTH)


def draw_o_from_center_point(screen, center):
    pygame.draw.circle(screen, BLACK, center, LENGTH, FIG_LINE_WIDTH)


def draw_mark(mark, screen, center):
    if mark == "X":
        draw_x_from_center_point(screen, center)
    elif mark == "O":
        draw_o_from_center_point(screen, center)



