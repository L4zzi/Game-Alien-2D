import pygame

from src.desconto import Pedido
from src.fleet_manager import FleetManager
from src.game_events import GameEventHandler
from src.settings import Settings
from tests.doubles import StubAlienNaBorda, StubSemDesconto


def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100


def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock()  # Criar mock do desconto
    mock_desconto.calcular.return_value = 10  # Definir comportamento do mock

    pedido = Pedido(mock_desconto)  # Injetar mock no Pedido
    resultado = pedido.total(100)  # Executar método

    assert resultado == 90  # Verificar resultado final

    mock_desconto.calcular.assert_called()  # verifica se o método calcular foi chamado
    mock_desconto.calcular.assert_called_once_with(100)  # chamado uma única vez com o valor 100
    assert mock_desconto.calcular.call_count == 1  # chamado exatamente uma vez


# ---------------- Jogo Game2D_Alien ----------------


def test_frota_muda_direcao_com_stub_alien():
    """Stub: alien falso que sempre está na borda -> a frota desce e inverte a direção."""
    settings = Settings()
    fleet_manager = FleetManager(None, settings, None)

    alien = StubAlienNaBorda()
    fleet_manager.aliens.add(alien)

    fleet_manager.check_fleet_edges()

    assert settings.fleet_direction == -1
    assert alien.rect.y == settings.fleet_drop_speed


def test_espaco_dispara_projetil_com_mock(mocker):
    """Mock: verifica se apertar ESPAÇO chama fire_bullet do BulletManager uma única vez."""
    mock_ship = mocker.Mock()
    mock_bullet_manager = mocker.Mock()

    event_handler = GameEventHandler(mock_ship, mock_bullet_manager)

    evento = mocker.Mock(key=pygame.K_SPACE)
    event_handler.handle_keydown(evento)

    mock_bullet_manager.fire_bullet.assert_called_once()


def test_seta_direita_move_nave_com_mock(mocker):
    """Mock: apertar a seta para a direita liga o movimento da nave e não dispara."""
    mock_ship = mocker.Mock()
    mock_bullet_manager = mocker.Mock()

    event_handler = GameEventHandler(mock_ship, mock_bullet_manager)

    evento = mocker.Mock(key=pygame.K_RIGHT)
    event_handler.handle_keydown(evento)

    assert mock_ship.moving_right is True
    mock_bullet_manager.fire_bullet.assert_not_called()
