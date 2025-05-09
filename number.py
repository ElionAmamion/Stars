import pygame as pg
import colors as c

def NUM_2(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y), (x+3, y), (x+3, y+3), (x, y+3), (x, y+6), (x+3, y+6)], 1)