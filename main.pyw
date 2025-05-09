import colors as c
import pygame as pg
import number as n
import letter as l

running = True
init_width, init_height = (96, 64)
sizeFactor = 4

pg.init()
display = pg.display.set_mode((init_width * sizeFactor, init_height * sizeFactor), pg.FULLSCREEN | pg.SCALED)

while running:
    x, y = pg.mouse.get_pos()

    l.LETR_P(display, 4, 4)
    l.LETR_R(display, 10, 4)
    l.LETR_E(display, 16, 4)
    l.LETR_S(display, 22, 4)
    l.LETR_S(display, 28, 4)
    l.LETR_S(display, 40, 4)
    l.LETR_P(display, 46, 4)
    l.LETR_A(display, 52, 4)
    l.LETR_C(display, 58, 4)
    l.LETR_E(display, 64, 4)
    l.LETR_T(display, 76, 4)
    l.LETR_O(display, 83, 4)
    l.LETR_R(display, 96, 4)
    l.LETR_E(display, 102, 4)
    l.LETR_M(display, 108, 4)
    l.LETR_O(display, 115, 4)
    l.LETR_V(display, 121, 4)
    l.LETR_E(display, 128, 4)
    l.LETR_A(display, 140, 4)
    l.LETR_L(display, 146, 4)
    l.LETR_L(display, 152, 4)
    l.LETR_D(display, 164, 4)
    l.LETR_O(display, 170, 4)
    l.LETR_T(display, 176, 4)
    l.LETR_S(display, 182, 4)

    l.LETR_P(display, 4, 16)
    l.LETR_R(display, 10, 16)
    l.LETR_E(display, 16, 16)
    l.LETR_S(display, 22, 16)
    l.LETR_S(display, 28, 16)
    l.LETR_E(display, 40, 16)
    l.LETR_C(display, 46, 16)
    l.LETR_A(display, 52, 16)
    l.LETR_P(display, 58, 16)
    l.LETR_E(display, 64, 16)
    l.LETR_T(display, 76, 16)
    l.LETR_O(display, 83, 16)
    l.LETR_C(display, 96, 16)
    l.LETR_L(display, 102, 16)
    l.LETR_O(display, 108, 16)
    l.LETR_S(display, 115, 16)
    l.LETR_E(display, 121, 16)


    for event in pg.event.get():
        if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_F11:
            pg.display.toggle_fullscreen()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
            pg.draw.rect(display, c.white, ((x, y), (2, 2)))
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            display.fill(c.black)


    pg.display.flip()
pg.quit()