import os, time as chronic_tacos
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('KingdomDark')

for this in ['Structure/', 'Gamefiles/']:
    for that in os.listdir(this):
        if that[-3:] == '.py': exec('from ' + this[:-1] + '.' + that[:-3] + ' import *')

jsondata = json_obj()
input = input_object(jsondata)

text = text_box()
hatlor = hatlor_obj(['lordhatlor.png'])
box=boxtext(screen, x=1000, y=900, w=900, h=100)

origin_taco = chronic_tacos.time()
while True:
    current_taco = chronic_tacos.time() - origin_taco
    input.update(jsondata, screen)
    if process_return(input):
        break
    hatlor.blit(screen, 'lordhatlor', (0, -15))
    text.RnD(screen, input, "im mr worldwide star thats so cool", 500, 400, 200, current_taco)
    box.render(screen)
    pg.time.wait(1); pg.display.flip(); screen.fill((55, 0, 75))
