import pygame as pg

# pygame uses (r, g, b) tuples for color
red = (255, 0, 0)
white = (255, 255, 255)

screen = pg.display.set_mode((500, 500))
pg.display.set_caption("click the mouse on the window ...")

# create a little red square
red_square = pg.Surface((30, 30))
red_square.fill(red)

# starting position
xy_position = (100, 100)

# set up the event loop
running = True
while running:
    event = pg.event.poll()
    keyinput = pg.key.get_pressed()
    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE]:
        raise SystemExit
    elif event.type == pg.QUIT:
        running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        #print(event.pos)  # test
        xy_position = event.pos

    # this erases the old sreen
    screen.fill(white)
    # put the image on the screen at given position
    screen.blit(red_square, xy_position)
    # update screen
    pg.display.flip()