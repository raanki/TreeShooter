import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 75
        self.max_health = 75
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(100, 400)
        self.rect.y = 540 - offset
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = 1 + random.randint(1, 3)

    def update_health_bar(self, surface):
        bar_color = (111, 240, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 25, self.rect.y - 10, self.health, 5]
        back_bar_position = [self.rect.x + 25, self.rect.y - 10, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def update_animation(self):
        self.animate(loop=True)

    def forward(self):
        if not self.game.check_collison(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = 1000 + random.randint(100, 400)
            self.health = self.max_health
            self.velocity = 1 + random.uniform(1, self.default_speed)
            self.game.score += 20

        if self.game.comet_event.is_full_loaded():
            self.game.all_monsters.remove(self)

            self.game.comet_event.attempt_fall()

class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)


class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8

