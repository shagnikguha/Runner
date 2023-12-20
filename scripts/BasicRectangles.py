import pygame
from sys import exit

pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))           
pygame.display.set_caption('Basic')

clock = pygame.time.Clock()                                 

sky_surface = pygame.image.load('graphics/Sky.png').convert()         
ground_surface = pygame.image.load('graphics/ground.png').convert()                 # convert makes the imaage easier to manage in pygame

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                      
score_surface = test_font.render("Testing", False, 'Black')   
score_rect = score_surface.get_rect(midtop = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()      # excludes the alpha values to remove empty space 
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))                            # takes image and draws rectangle around it

running = True

while running:                                             
    for event in pygame.event.get():                        
        if event.type == pygame.QUIT:                       
            running = False    
        # if event.type == pygame.MOUSEMOTION:
        #   if player_rect.collidepoint(event.pos):
        #       print('collision)   
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         print("clicked")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            print('keyup')                             
    
    screen.blit(sky_surface, (0,0))                        
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', (score_rect.x - 5, score_rect.y - 5, score_rect.width + 5, score_rect.height + 5), width=6,border_radius=5)
    screen.blit(score_surface, score_rect)

    # pygame.draw.line(screen, 'Red', (0,0), pygame.mouse.get_pos(), 5)
    # pygame.draw.ellipse(screen, 'Gold', pygame.Rect(500, 200, 100, 100))    

    player_rect.left += 1
    snail_rect.right -= 4                                                           # making snail move left
    if snail_rect.right <= 0:
        snail_rect.right = 800        
    
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)                                           # taking image and placing it at the rectangle position
    
    # if player_rect.colliderect(snail_rect):                                         # returns 1 when collision occurs
    #     print('collision')                                                          # if we have a health-bar, then we should add invincibilty frames.

    # keys = pygame.key.get_pressed()                                                 # creating a dictionary of all keyboard inputs
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):                                         #checks if the point is in the rectangle
        print(pygame.mouse.get_pressed())

    pygame.display.update()                                
    clock.tick(60)                                         
   
pygame.quit()
exit()
