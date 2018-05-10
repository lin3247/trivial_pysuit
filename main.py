#!/usr/bin/python3
import pygame_textinput
import pygame
from button import Button

import random




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



curr_score = 0					#store game status variables
curr_category = ""		#store current game category
curr_category_index = 0

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

categories = ["countries", "colors", "fruits", "animals"]
category = font.render("Category: " + curr_category, True, BLACK)





done = False
in_game = False

def update_game_status():
    global in_game
    global start_time
    global button
    global remaining_time
    global category
    global categories
    global curr_category
    global curr_category_index
    global curr_score
    global score

    in_game = not in_game

    if(in_game):
        start_time = pygame.time.get_ticks()
        temp_index = random.randint(0,len(categories)-1)
        while(temp_index == curr_category_index):
            temp_index = random.randint(0,len(categories)-1)
        curr_category_index = temp_index
        curr_category = categories[curr_category_index]
        category = font.render("Category: " + curr_category, True, BLACK)
        curr_score = 0
        score = font.render("Score: " + str(curr_score), True, BLACK)


    else:
        remaining_time = 0

countries = {"congo":3, "china":2, "usa":1}
colors = {"red":1,"gold":3}
fruits = {"apple":1, "orange":2}
animals = {"cat":1, "dog":2}

def get_word_value(word):
    global curr_category


    if curr_category == "countries":
        if word in countries:
            return countries.get(word)

    if curr_category == "colors":
        if word in colors:
            return colors.get(word)

    if curr_category == "fruits":
        if word in fruits:
            return fruits.get(word)

    if curr_category == "animals":
        if word in animals:
            return animals.get(word)

    return 0




title = title_font.render("Trivia", True, BLUE)
timer = font.render("Timer: ", True, BLACK)

input_start = font.render("Input: ______________", True, BLACK)
text_input = pygame_textinput.TextInput()
score = font.render("Score: " + str(curr_score), True, BLACK)
button = Button((200,450,200,50),RED, update_game_status, text="start/stop", **BUTTON_STYLE)

screen = pygame.display.set_mode((600, 600))




while not done:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:				#check for exit conditions
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        button.check_event(event)
    if(done):
        break

    if(in_game):
        #display remaining_time
        remaining_time = (9999 - (pygame.time.get_ticks() - start_time))
        timer = font.render("Timer: " + str(remaining_time//1000) + "." + str((remaining_time%1000)//100), True, BLACK)   

        #check if close enough to 0 time left
        if(remaining_time <= 10):
            remaining_time = 0
            in_game = False
            timer = font.render("Timer: " + str(remaining_time//1000) + "." + str((remaining_time%1000)//100), True, BLACK)


    #Feed text_input with events every frame so it can grab user input.
    #Also, only returns true only when user presses ENTER/RETURN key
    if text_input.update(events):
    	if(in_game):
            #get current word
            word = text_input.get_text().lower()
            
            #get word value
            value = get_word_value(word)

            #update points
            curr_score = curr_score + value

            #set a new category
            temp_index = random.randint(0,len(categories)-1)
            while(temp_index == curr_category_index):
                temp_index = random.randint(0,len(categories)-1)
            curr_category_index = temp_index
            curr_category = categories[curr_category_index]
            category = font.render("Category: " + curr_category, True, BLACK)
            score = font.render("Score: " + str(curr_score), True, BLACK)
            text_input.clear_text()
            

    button.update(screen)


    # Blit its surface onto the screen
    screen.blit(title,(200,25))
    screen.blit(timer,(175,150))
    screen.blit(category,(150,225))
    screen.blit(input_start,(100,290))
    screen.blit(text_input.get_surface(), (200, 300))
    screen.blit(score,(250,375))
    

    pygame.display.update()
    #pygame.display.flip()
    clock.tick(30)