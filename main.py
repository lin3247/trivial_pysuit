import pygame

pygame.init()

#INITIALIZE DATABASE








pygame.display.set_caption('***CAPTION GOES HERE***')

screen = pygame.display.set_mode((400, 300))





done = False
while not done:		#main control loop that switches between activities
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True






        
        pygame.display.flip()		#Update the full display Surface to the screen