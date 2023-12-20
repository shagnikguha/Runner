import pygame
from sys import exit
import random

pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))           
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()                                 

sky_surface = pygame.image.load('Runner/graphics/Sky.png').convert()         
ground_surface = pygame.image.load('Runner/graphics/ground.png').convert()                 # convert makes the imaage easier to manage in pygame

# font = pygame.font.Font(None, 50)
test_font = pygame.font.Font('Runner/font/Pixeltype.ttf', 50)                      
# score_surface = test_font.render("Testing", False, 'Black')   
# score_rect = score_surface.get_rect(midtop = (400, 50))

# Obstacles
snail_frame_1 = pygame.image.load('Runner/graphics/snail/snail1.png').convert_alpha()      # excludes the alpha values to remove empty space 
snail_frame_2 = pygame.image.load('Runner/graphics/snail/snail2.png').convert_alpha()      # excludes the alpha values to remove empty space 
snail_frame = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frame[snail_frame_index]
# snail_rect = snail_surface.get_rect(midbottom = (600, 300))

fly_frame_1 = pygame.image.load('Runner/graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('Runner/graphics/Fly/Fly2.png').convert_alpha()
fly_frame = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frame[fly_frame_index]

obstacle_rect_list = []

# Player
player_walk_1 = pygame.image.load('Runner/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Runner/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('Runner/graphics/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))                            # takes image and draws rectangle around it

player_stand = pygame.image.load('Runner/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
# player_stand = pygame.transform.rotozoom(player_stand, 0 ,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400, 330))

# Sounds
jump_sound = pygame.mixer.Sound('Runner/audio/jump.mp3')
jump_sound.set_volume(0.5)
game_music = pygame.mixer.Sound('Runner/audio/music.wav')
game_music.set_volume(0.35)
game_music.play(loops = -1) # loop forever
player_gravity = 0

running = True

game_active = False

start_time = 0

current_time = 0

# Timer  --> creaing custom user event
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks()/1000) - start_time                                          # gives time in millisecond from when pygame started
    score_surface = test_font.render(f'Score: {current_time}', False, 'Black')   
    score_rect = score_surface.get_rect(midtop = (400, 50))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', (score_rect.x - 5, score_rect.y - 5, score_rect.width + 5, score_rect.height + 5), width=6,border_radius=5)
    screen.blit(score_surface, score_rect)

def obstacle_movement(obstacle_list):
    if obstacle_list:                                                                                      # Checking if list is empty
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list

def collsion_chck(obstacle_list):
    global game_active
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.colliderect(obstacle_rect):
                game_active = False

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        # jumping animation when not on floor
        player_surf = player_jump
    else:
        # player walking animation when on floor
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]

while running:                                            
    for event in pygame.event.get():                        
        if event.type == pygame.QUIT:                       
             running = False    
        if game_active:    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
                    jump_sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos ):
                    player_gravity = -20
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    obstacle_rect_list = []
        if game_active:
            if event.type == obstacle_timer:
                if random.randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (random.randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (random.randint(900, 1100), 210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frame[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frame[fly_frame_index]

    if game_active:
        screen.blit(sky_surface, (0,0))                        
        screen.blit(ground_surface, (0, 300))

        display_score()
        
        # Obstacle movement
        obstavle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision check
        collsion_chck(obstacle_rect_list)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        player_animation()
        screen.blit(player_surf, player_rect)                                           # taking image and placing it at the rectangle position
    
    else:
        screen.fill((94,129,162))   
        screen.blit(game_name, game_name_rect) 
        screen.blit(player_stand, player_stand_rect)
        score_surface = test_font.render(f'Your score: {current_time}', False, (111,196,169))   
        score_rect = score_surface.get_rect(center = (400, 330))

        if current_time == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_surface, score_rect)

    pygame.display.update()                                
    clock.tick(60)                                     
   
pygame.quit()
exit()
