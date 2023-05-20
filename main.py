import pygame
import math
from game import Game
pygame.init()

clock = pygame.time.Clock()
FPS = 60

#Fenetre
pygame.display.set_caption("TreeShooter")
screen = pygame.display.set_mode((1080, 720))
running = True
background = pygame.image.load('assets/bg.jpg')
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
play_button = pygame.image.load("assets/button.png")
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

pygame.mixer.music.load('assets/sounds/Skeleton.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#charger le jeu
game = Game()

while running:

    #appliquer arriere plan
    screen.blit(background, (0, -200))

    #verifier si le jeux a lancer
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner, (banner_rect.x,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.start()
                    game.sound_manager.play("click")
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    if running:
        pygame.display.flip()
    clock.tick(FPS)