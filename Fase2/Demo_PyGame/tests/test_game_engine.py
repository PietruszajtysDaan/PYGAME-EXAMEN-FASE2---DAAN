# ----- tests/test_game_engine.py -----
import pytest
from engine.game import GameEngine

@pytest.fixture(autouse=True)
def chdir_tmp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

def test_game_engine_initial_state():
    engine = GameEngine()
    assert engine.running is True
    assert hasattr(engine, 'clock')
    assert hasattr(engine, 'ui')
    assert isinstance(engine.scores, list)

