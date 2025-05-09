import pygame as pg
import colors as c

def LETR_A(display, x, y):
    pg.draw.rect(display, c.white, ((x, y), (4, 4)), 1)
    pg.draw.rect(display, c.white, ((x, y+4), (1, 3)), 1)
    pg.draw.rect(display, c.white, ((x+3, y+4), (1, 3)), 1)

def LETR_C(display, x, y):
    pg.draw.rect(display, c.white, ((x, y), (4, 7)), 1)
    pg.draw.line(display, c.black, (x+3, y+2), (x+3, y+4), 1)

def LETR_D(display, x, y):
    pg.draw.rect(display, c.white, ((x, y), (4, 7)), 1)
    pg.draw.rect(display, c.black, ((x+3, y), (1, 1)), 1)
    pg.draw.rect(display, c.black, ((x+3, y+6), (1, 1)), 1)

def LETR_E(display, x, y):
    pg.draw.lines(display, c.white, False, [(x+3, y), (x, y), (x, y+3), (x+2, y+3), (x, y+3), (x, y+6), (x+3, y+6)], 1)

def LETR_L(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y), (x, y+6), (x+3, y+6)], 1)

def LETR_M(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y+6), (x, y), (x+2, y+5), (x+4, y), (x+4, y+6)], 1)

def LETR_O(display, x, y):
    pg.draw.rect(display, c.white, ((x, y), (4, 7)), 1)

def LETR_P(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y), (x+3, y), (x+3, y+3), (x, y+3), (x, y), (x, y+6)], 1)

def LETR_R(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y+6), (x, y), (x+3, y), (x+3, y+2), (x+2, y+3), (x, y+3), (x+2, y+3), (x+3, y+4), (x+3, y+6)], 1)

def LETR_S(display, x, y):
    pg.draw.lines(display, c.white, False, [(x+3, y), (x, y), (x, y+3), (x+3, y+3), (x+3, y+6), (x, y+6)], 1)

def LETR_T(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y), (x+4, y), (x+2, y), (x+2, y+6)], 1)

def LETR_V(display, x, y):
    pg.draw.lines(display, c.white, False, [(x, y), (x+2, y+6), (x+4, y)], 1)