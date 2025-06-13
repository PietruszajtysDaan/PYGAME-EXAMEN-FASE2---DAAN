# ----- tests/test_player.py -----
import pygame
import pytest
from entities.player import Player

class DummyKeys:
    def __init__(self, pressed):
        self.pressed = pressed
    def __getitem__(self, key):
        return key in self.pressed

@pytest.fixture(autouse=True)
def init_pygame(monkeypatch):
    pygame.init()
    # Patche get_pressed om alleen de pijltjestoetsen te simuleren
    monkeypatch.setattr(pygame.key, 'get_pressed', lambda: DummyKeys({pygame.K_RIGHT}))

def test_player_moves_right():
    player = Player(0, 0)
    initial_x = player.x
    player.update()
    assert player.x == initial_x + player.speed

