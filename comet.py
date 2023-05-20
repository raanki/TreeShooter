import pygame
import random
from monster import Monster, Mummy, Alien

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(4, 7)
        self.rect.x = random. randint(20, 800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play("meteorite")
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            self.remove()
        if self.comet_event.game.check_collison(self, self.comet_event.game.all_players):
            self.comet_event.game.player.health -= 35
            self.remove()
            if self.comet_event.game.player.health <= 0:
                self.comet_event.game.game_over()

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False