import pygame
import time


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

pygame.display.set_caption('***caption text***')
font = pygame.font.SysFont("comicsansms", 36)


timer_text = font.render("timer", True, (0, 128, 0))
current_category_text = font.render("current category", True, (0, 128, 0))
score_text = font.render("score text", True, (0, 128, 0))

time = 0
category = ""
score = 0

in_game = False





#to add:
#input box
#start button





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))

    timer_text = 

    screen.blit(timer_text,
        (320 - timer_text.get_width() // 2, 100 - timer_text.get_height() // 2))
    
    screen.blit(current_category_text,
        (320 - current_category_text.get_width() // 2, 200 - current_category_text.get_height() // 2))

    screen.blit(score_text,
        (320 - score_text.get_width() // 2, 300 - score_text.get_height() // 2))




    pygame.display.flip()
    clock.tick(60)