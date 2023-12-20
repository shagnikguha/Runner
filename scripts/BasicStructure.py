import pygame
from sys import exit

pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))           # creating a display surface
pygame.display.set_caption('Basic')

test_surface1 = pygame.Surface((100, 200))                  # creating a regular surface to place on the display
test_surface1.fill('Red')                                   # making that surface red

sky_surface = pygame.image.load('graphics/Sky.png').convert()         # importing image to show on display
ground_surface = pygame.image.load('graphics/ground.png').convert()             # convert makes the imaage easier to manage in pygame

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                      # setting up font for game
test_surface2 = test_font.render("Testing", False, 'Black')   # False/True for anti-aliasing

clock = pygame.time.Clock()                                 # allowing us to set a proper frame rate to ensure that game will run properly

running = True

while running:                                              # drawing all elements and updating in for loop
    for event in pygame.event.get():                        # a for-loop which loops through all user inputs
        if event.type == pygame.QUIT:                       # checking for the closing condition, i.e. the red cross
            running = False                                 # exit the loop if the user closes the window
    
    screen.blit(sky_surface, (0,0))                         # block image transfer, that is placing a surface on another
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface2, (300, 50))
    pygame.display.update()                                 # updating code with every iteration
    clock.tick(60)                                          # making the while loop run every 60 seconds
   
pygame.quit()
exit()
