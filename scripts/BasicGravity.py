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

# font = pygame.font.Font(None, 50)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)                      

# score_surface = test_font.render("Testing", False, 'Black')   
# score_rect = score_surface.get_rect(midtop = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()      # excludes the alpha values to remove empty space 
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))                            # takes image and draws rectangle around it

player_gravity = 0

running = True

game_active = True

start_time = 0

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time                                          # gives time in millisecond from when pygame started
    score_surface = test_font.render(f'Score: {current_time}', False, 'Black')   
    score_rect = score_surface.get_rect(midtop = (400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', (score_rect.x - 5, score_rect.y - 5, score_rect.width + 5, score_rect.height + 5), width=6,border_radius=5)
    screen.blit(score_surface, score_rect)


while running:                                             
    for event in pygame.event.get():                        
        if event.type == pygame.QUIT:                       
             running = False    
        if game_active:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos ):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.x = 600
                    start_time = int(pygame.time.get_ticks()/1000)
                                
    if game_active:
        screen.blit(sky_surface, (0,0))                        
        screen.blit(ground_surface, (0, 300))

        display_score()
        
        # Snail
        snail_rect.right -= 5                                                           # making snail move left
        if snail_rect.right <= 0:
            snail_rect.right = 800        
        
        screen.blit(snail_surface, snail_rect)
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)                                           # taking image and placing it at the rectangle position
        
        # player snail collision
        if snail_rect.colliderect(player_rect):
            game_active = False 

    else:
        screen.fill('Yellow')

    pygame.display.update()                                
    clock.tick(60)                                     
   
pygame.quit()
exit()
