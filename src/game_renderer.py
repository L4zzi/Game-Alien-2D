import pygame


class GameRenderer:
    """Responsável apenas por desenhar os elementos do jogo na tela."""

    def __init__(
        self,
        screen,
        bg_color,
        ship,
        bullets,
        aliens
    ):
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def render_screen(self):
        """Redesenha a tela a cada passagem pelo laço."""

        self.screen.fill(self.bg_color)

        self.ship.blitme()

        self.aliens.draw(self.screen)

        self.draw_bullets()

        pygame.display.flip()

    def draw_bullets(self):
        """Desenha os projéteis na tela."""

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()