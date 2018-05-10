import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

clock = pygame.time.Clock()

img_error_message = "Error loading image:"
begin_text = "Begin."

display_width = 720
display_height = 1080

# Basic display info #
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Trivial Pysuit")

# Cut display into quadrants #
status_rect = pygame.Rect(0, 0, display_width, display_height/4)            # top 1/4th of screen is status
q_rect = pygame.Rect(0, display_height/4, display_width, display_height/4)  # next 1/4th of screen is question
answer_rect = pygame.Rect(0, (display_width/4)*2, display_width, display_height/4)  # next 1/4th of screen is answer
info_rect = pygame.Rect(0, (display_width/4)*3, display_width, display_height/4)    # bottom 1/4th of screen is info


def load_image(img_name, colorkey=None):
    fullname = os.path.join('data', img_name)           # resources are in "data" directory
    try:
        image = pygame.image.load(fullname)         # load the image
    except pygame.error:
        print(img_error_message, img_name)              # return error
        raise SystemExit
    image = image.convert()                         # make new copy of Surface, matches display
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))         # use color of top left pixel
        image.set_colorkey(colorkey, RLEACCEL)      # RLEACCEL means quicker blitting
    return image, image.get_rect()                  # get rectangular area of surface


def load_sound(sound_name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()                      # return fake blank sound which returns no errors
    fullname = os.path.join('data', sound_name)
    try:
        sound = pygame.mixer.Sound(fullname)    # load the sound
    except pygame.error:
        print('Cannot load sound:', sound_name)
        raise SystemExit
    return sound


background = pygame.Surface(screen.get_size())      # background is same size as display window
background = background.convert()                   # background same format as display window
background.fill((250, 250, 250))                    # fill white

if pygame.font:
    font = pygame.font.Font(None, 24)                           # default font, size 24
    text = font.render(begin_text, 1, (10, 10, 10))             # grey text
    textpos = text.get_rect(centerx=screen.get_width()/2)       # display in middle
    screen.blit(text, textpos)                                  # paste text onto display

screen.blit(screen, (0, 0))                                     # paste everything
pygame.display.flip()                                           # swap display for double buffering

x = 0
y = 0
done = False

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        done = True

        '''
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        '''

        screen.fill((255, 255, 255))
        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 30)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()                   # update display
        clock.tick(60)                          # make sure doesn't run faster than 60 frames/sec
