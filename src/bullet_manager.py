import pygame

from bullet import Bullet


class BulletManager:
    """Responsável apenas por criar, atualizar e desenhar os projéteis."""

    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = pygame.sprite.Group()

    def fire_bullet(self):
        """Dispara um projétil se o limite não tiver sido atingido."""

        if len(self.bullets) < self.settings.bullet_allowed:

            new_bullet = Bullet(
                self.screen,
                self.settings,
                self.ship
            )

            self.bullets.add(new_bullet)

    def update_bullets(self, aliens):
        """Atualiza os projéteis e verifica colisões."""

        self.bullets.update()

        self.remove_offscreen_bullets()

        self.check_bullet_alien_collisions(aliens)

    def remove_offscreen_bullets(self):
        """Remove os projéteis que desapareceram da tela."""

        for bullet in self.bullets.copy():

            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def check_bullet_alien_collisions(self, aliens):
        """Verifica colisões entre projéteis e alienígenas."""

        pygame.sprite.groupcollide(
            self.bullets,
            aliens,
            True,
            True
        )