import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        bar_color = (111, 240, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 50, self.rect.y - 10, self.health, 10]
        back_bar_position = [self.rect.x + 50, self.rect.y - 10, self.max_health, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play("tir")

    def move_right(self):
        if not self.game.check_collison(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def damage(self, amount):
        if self.health - amount - 1 > amount:
            self.health -= amount
        else:
            self.game.game_over()