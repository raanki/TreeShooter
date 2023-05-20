import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager

class Game:
    def __init__(self):
        #generer notre joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.is_playing = False
        self.comet_event = CometFallEvent(self)
        self.score = 0
        self.font = pygame.font.Font("assets/Poppins.ttf", 25)
        self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def check_collison(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self, screen):
        score_texte = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_texte, (20, 20))

        # appliquer limage de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # recuperer les projectiles du jeu
        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer ensemble projectile
        self.player.all_projectiles.draw(screen)
        self.all_monsters.draw(screen)
        self.player.update_health_bar(screen)
        self.player.update_animation()
        self.comet_event.all_comets.draw(screen)

        # moove joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


        self.comet_event.update_bar(screen)

        # si le joueur ferme la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            # touche le clavier
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    self.player.launch_projectile()


            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False