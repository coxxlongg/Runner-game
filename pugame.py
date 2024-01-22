import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect =  score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('run master')
clock = pygame.time.Clock()
test_font = pygame.font.Font('/Users/coxlong/Desktop/pp/graph/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('/Users/coxlong/Desktop/pp/graph/Sky.png').convert()
ground_surface = pygame.image.load('/Users/coxlong/Desktop/pp/graph/ground.png').convert()

#score_surf = test_font.render('Mini Runner', False, 'Black')


snail_surf = pygame.image.load('/Users/coxlong/Desktop/pp/graph/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('/Users/coxlong/Desktop/pp/graph/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#intro
player_stand = pygame.image.load('/Users/coxlong/Desktop/pp/graph/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand,(200,400))
player_stand_rect = player_stand_scaled.get_rect(center = (400,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #screen.blit(score_surf,(300,50))
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #coll
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('White')
        screen.blit(player_stand_scaled,)



    pygame.display.update()
    clock.tick(60)



