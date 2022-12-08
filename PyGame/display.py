import pygame as pg

pg.display.init()
pg.display.set_mode((500,500))

running = True

while(running):
    for event in pg.event.get():
          
        if event.type == pg.QUIT:
            running = False