import sys

import pygame

from alien import Alien


class FleetManager:
    """Responsável apenas por criar e atualizar a frota de alienígenas."""

    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.aliens = pygame.sprite.Group()

    def create_fleet(self):
        """Cria uma frota de alienígenas."""

        alien = Alien(self.screen, self.settings)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = (
            self.settings.screen_width
            - (2 * alien_width)
        )

        number_aliens_x = (
            available_space_x // (2 * alien_width)
        )

        ship_height = self.ship.rect.height

        available_space_y = (
            self.settings.screen_height
            - (3 * alien_height)
            - ship_height
        )

        number_rows = (
            available_space_y // (2 * alien_height)
        )

        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):

                alien = Alien(
                    self.screen,
                    self.settings
                )

                alien.x = (
                    alien_width
                    + 2 * alien_width * alien_number
                )

                alien.rect.x = alien.x

                alien.y = (
                    alien_height
                    + 2 * alien_height * row_number
                )

                alien.rect.y = alien.y

                self.aliens.add(alien)

    def update_aliens(self):
        """Atualiza a posição dos alienígenas."""

        self.check_fleet_edges()

        self.aliens.update()

        self.check_ship_collision()

    def check_fleet_edges(self):
        """Verifica se algum alienígena atingiu uma borda."""

        for alien in self.aliens.sprites():

            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Move a frota para baixo e inverte sua direção."""

        for alien in self.aliens.sprites():

            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def check_ship_collision(self):
        """Verifica se a nave colidiu com algum alienígena."""

        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens
        ):
            print("A nave foi atingida!")
            sys.exit()