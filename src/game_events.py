import sys

import pygame


class GameEventHandler:
    """Responsável apenas por ler e tratar eventos do teclado/janela."""

    def __init__(self, ship, bullet_manager):
        self.ship = ship
        self.bullet_manager = bullet_manager

    def check_events(self):
        """Responde a eventos de pressionamento de teclas e mouse."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

            elif event.type == pygame.KEYUP:
                self.handle_keyup(event)

    def handle_keydown(self, event):
        """Responde a eventos de pressionamento de teclas."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            self.bullet_manager.fire_bullet()

    def handle_keyup(self, event):
        """Responde a eventos de liberação de teclas."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False