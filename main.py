#!/usr/bin/python3
import pygame_textinput
import pygame
from button import Button

pygame.init()

#colors
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)
BUTTON_STYLE = {"hover_color" : BLUE,
"clicked_color" : GREEN,
"clicked_font_color" : BLACK,
"hover_font_color" : ORANGE,
}

#fonts
title_font = pygame.font.SysFont("arial", 60)                
font = pygame.font.SysFont("arial", 35)

curr_score = 0
curr_category = "animals"

title = title_font.render("Trivia", True, BLUE)
timer = font.render("Timer: ", True, BLACK)
category = font.render("Category: " + curr_category, True, BLACK)
input_start = font.render("Input: ______________", True, BLACK)
text_input = pygame_textinput.TextInput()
score = font.render("Score: " + str(curr_score), True, BLACK)
button = Button((200,450,200,50),RED, GREEN,text="start", **BUTTON_STYLE)

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
done = False

while not done:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

    # Feed it with events every frame
    if text_input.update(events):
        curr_category=text_input.get_text()
        category = font.render("Category: " + curr_category, True, BLACK)
    # Blit its surface onto the screen
    screen.blit(title,(200,25))
    screen.blit(timer,(175,150))
    screen.blit(category,(150,225))
    screen.blit(input_start,(100,290))
    screen.blit(text_input.get_surface(), (200, 300))
    screen.blit(score,(250,375))
    button.update(screen)

    pygame.display.update()
    #pygame.display.flip()
    clock.tick(30)