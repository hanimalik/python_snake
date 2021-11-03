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

#colors
blue = (0,0,255)
red = (255,0,0)
yellow = (255, 255, 0)
white = (255, 255, 255)

#variable for when game is over
game_over = False

#variables 
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0


clock = pygame.time.Clock()



#main game loop, will run infinitely until value 
#of game_over changes from 'False to 'True'
while not game_over:
    #loops over all of the events (keypresses, mouse moves,
    # button clicks) that happen in one game loop
    for event in pygame.event.get():
        #if someone wants to exit the game
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #left arrow key
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT: #right arrow key
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        
    #draws yellow rectangle to be head of snake
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    
    
    #command updates the display with any changes
    pygame.display.update()


clock.tick(30)


# quit the game
pygame.quit()
quit()

