import pygame
from pygame.sprite import Sprite

from src.desconto import IDesconto


class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0


# Stub do jogo: um alienígena falso que sempre informa estar na borda da tela.
# Substitui o Alien real (que precisa de imagem e tela) com uma resposta controlada.
class StubAlienNaBorda(Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 10, 10)

    def check_edges(self):
        return True
