import sys

import pygame

from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos básicos."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )

        pygame.display.set_caption("Alien Invasion")

        # Cria a nave
        self.ship = Ship(self.screen, self.settings)

        # Cor do plano de fundo
        self.bg_color = self.settings.bg_color

        # Grupo de projéteis
        self.bullets = pygame.sprite.Group()

        # Grupo de alienígenas
        self.aliens = pygame.sprite.Group()

    def create_fleet(self):
        """Cria uma frota de alienígenas."""

        # Cria um alienígena para obter suas dimensões
        alien = Alien(self.screen, self.settings)

        alien_width = alien.rect.width
        alien_height = alien.rect.height

        # Calcula quantos aliens cabem horizontalmente
        available_space_x = (
            self.settings.screen_width - (2 * alien_width)
        )

        number_aliens_x = available_space_x // (2 * alien_width)

        # Calcula quantas linhas cabem verticalmente
        ship_height = self.ship.rect.height

        available_space_y = (
            self.settings.screen_height
            - (3 * alien_height)
            - ship_height
        )

        number_rows = available_space_y // (2 * alien_height)

        # Cria as linhas de alienígenas
        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):

                alien = Alien(self.screen, self.settings)

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

    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e mouse."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._handle_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._handle_keyup_events(event)

    def _handle_keydown_events(self, event):
        """Responde aos eventos de pressionamento de teclas."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _handle_keyup_events(self, event):
        """Responde aos eventos de liberação de teclas."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Dispara um projétil se o limite não tiver sido atingido."""

        if len(self.bullets) < self.settings.bullet_allowed:

            new_bullet = Bullet(
                self.screen,
                self.settings,
                self.ship
            )

            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualiza a posição dos projéteis e remove os antigos."""

        self.bullets.update()

        self._remove_offscreen_bullets()

        self._check_bullet_alien_collisions()

    def _remove_offscreen_bullets(self):
        """Remove os projéteis que desapareceram da tela."""

        for bullet in self.bullets.copy():

            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """Verifica colisões entre projéteis e alienígenas."""

        pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True
        )

    def _update_aliens(self):
        """Atualiza a posição dos alienígenas."""

        self._check_fleet_edges()

        self.aliens.update()

    def _check_fleet_edges(self):
        """Responde quando algum alienígena alcança a borda."""

        for alien in self.aliens.sprites():

            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move a frota para baixo e inverte sua direção."""

        for alien in self.aliens.sprites():

            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_ship_collision(self):
        """Verifica se a nave colidiu com algum alienígena."""

        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens
        ):

            print("A nave foi atingida!")

            sys.exit()

    def _update_game_state(self):
        """Atualiza o estado da nave, projéteis e alienígenas."""

        self.ship.update()

        self._update_bullets()

        self._update_aliens()

        self._check_ship_collision()

    def _draw_bullets(self):
        """Desenha os projéteis na tela."""

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _render_screen(self):
        """Redesenha todos os elementos da tela."""

        self.screen.fill(self.bg_color)

        self.ship.blitme()

        self.aliens.draw(self.screen)

        self._draw_bullets()

        pygame.display.flip()

    def run_game(self):
        """Executa o laço principal do jogo."""

        self.create_fleet()

        while True:

            self._check_events()

            self._update_game_state()

            self._render_screen()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()