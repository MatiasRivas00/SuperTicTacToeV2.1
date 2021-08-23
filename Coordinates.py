import pygame
import math
import cmath


def center(width, height):
    return width/2, height/2


def plane(x, y, center):
    center_x = center[0]
    center_y = center[1]
    if x < center_x and y < center_y:
        return x - center_x, center_y - y
    if x > center_x and y < center_y:
        return x - center_x, center_y - y
    if x < center_x and y > center_y:
        return x - center_x, center_y - y
    if x > center_x and y > center_y:
        return x - center_x, center_y - y


def polar(x, y):
    r, phi = cmath.polar(complex(x, y))
    if phi < 0:
        return r, 360 + math.degrees(phi)
    else:
        return r, math.degrees(phi)


def new_cord(x, y, center):
    plx, ply = plane(x, y, center)
    r, phi = polar(plx, ply)
    j = r//100
    i = phi//45
    return int(i), int(j)


def fig_center(i, j, center):
    theta = i*45 + 45/2
    r = j*100 + 50
    print(theta, r)
    x, y = (r*math.cos(math.radians(theta)), r*math.sin(math.radians(theta)))
    print((center[0] + x, center[1] - y))
    return center[0] + x, center[1] - y

