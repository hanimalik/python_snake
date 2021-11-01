"""
Classic snake game in python. Code was generated following the
tutorial at: https://www.edureka.co/blog/snake-game-with-pygame/
"""

# import required packages
import pygame

# initialize the game
pygame.init()

# set the screen size
dis = pygame.display.set_mode((400, 300))

# draw the screen
pygame.display.update()

#set caption on screen
pygame.display.set_caption("Snake Game by Edureka")
#variable for when game is over
game_over = False

#main game loop, will run infinitely until value 
#of game_over changes from 'False to 'True'
while not game_over:
    #loops over all of the events (keypresses, mouse moves,
    # button clicks) that happen in one game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True




# quit the game
pygame.quit()
quit()

