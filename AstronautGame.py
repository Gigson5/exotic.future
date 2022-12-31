from tkinter import BOTTOM
import pygame

import sys

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    test_font = pygame.font.Font(None, 50)
    score_surf = test_font.render(f"Score: {current_time}",False, 'Red')
    score_rect = score_surf.get_rect(center = (750, 100))
    screen.blit(score_surf, score_rect)
    return current_time

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 750:
        player_surf = player_jump
        player_surf = pygame.transform.scale(player_surf, (170, 210))
    else:
        player_index += 0.1
        if player_index > len(player_walk): player_index = 0 
        player_surf = player_walk[int(player_index)]
        player_surf = pygame.transform.scale(player_surf, (170, 210))

pygame.init()

score = 0

def update_screen():
    pygame.display.flip()


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("Moon Astronaunt")

clock = pygame.time.Clock()

game_active = False

##############
# Game score #
##############

start_time = 0

###################
# Moon Background #
###################

bg_surf = pygame.image.load('images/bg1.png').convert_alpha()
bg_surf = pygame.transform.scale(bg_surf, (1600, 700))
bg_rect = bg_surf.get_rect()

###############
# Moon Ground #
###############

ground_surf = pygame.image.load('images/moonland.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (4000, 200))
ground_rect = ground_surf.get_rect(center = (800, 800))

################
# Alien Flying #
################

alien_surf = pygame.image.load('images/ufo1.png').convert_alpha()
alien_surf = pygame.transform.scale(alien_surf, (150, 90))
alien_rect = alien_surf.get_rect(midbottom = (1400, 700))

#########################
# Player Moon Astronaut #
#########################

player_walk_1 = pygame.image.load('images/walk1.png').convert_alpha()
player_walk_2 = pygame.image.load('images/walk2.png').convert_alpha()
player_jump = pygame.image.load('images/jump.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]

player_index = 0 

player_surf = player_walk[player_index]

player_surf = pygame.transform.scale(player_surf, (170, 210))

player_rect = player_surf.get_rect(midbottom = (200, 750))
player_gravity = 0

##############
# Start game #
##############

text_font_start = pygame.font.Font(None, 120)
text_start = text_font_start.render('Moon Astronaunt!', False, 'Red')
text_start_rect = text_start.get_rect(center = (770, 200))

text2_font_start = pygame.font.Font(None, 80)
text2_start = text2_font_start.render('Press Space to play!', False, 'Red')
text2_start_rect = text2_start.get_rect(center = (770, 450))

#############
# Game over #
#############

bg_over = pygame.image.load('images/bggg.png').convert_alpha()
bg_over = pygame.transform.scale(bg_over, (1600, 900))
bg_over_rect = bg_over.get_rect()

text_font_over = pygame.font.Font(None, 150)
text_over = text_font_over.render('Game Over!', False, 'Red')
text_over_rect = text_over.get_rect(center = (770, 200))

while True:
    # check_events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE and player_rect.bottom >= 750:
                    player_gravity = -27
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                alien_rect.left = 1200
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # Background
        screen.blit(bg_surf, bg_rect)

        # Ground
        screen.blit(ground_surf, ground_rect)

        # Game score
        score = display_score() 

        # player
        player_animation()
        screen.blit(player_surf, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 750: player_rect.bottom = 750


        # alien
        if alien_rect.right <= 0: alien_rect.left = 1600
        screen.blit(alien_surf, alien_rect)
        alien_rect.x -= 10

        # collision
        if alien_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.blit(bg_over, bg_rect)

        score_font_start = pygame.font.Font(None, 80)
        score_start = score_font_start.render(f'Your Score: {score}', False, 'Red')
        score_start_rect = score_start.get_rect(center = (770, 450))

        if score == 0:
            screen.blit(text_start, text_start_rect)
            screen.blit(text2_start, text2_start_rect)
        else:
            screen.blit(text_over, text_over_rect)
            screen.blit(score_start, score_start_rect)



    
    
    

    clock.tick(60)
    update_screen()
    
    