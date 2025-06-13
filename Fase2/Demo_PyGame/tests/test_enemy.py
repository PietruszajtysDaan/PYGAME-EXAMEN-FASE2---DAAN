# ----- tests/test_enemy.py -----
from entities.enemy import Enemy

def test_enemy_bounces_at_edges():
    enemy = Enemy(0, 0)
    # Vijand beweegt 2 pixels per update
    initial_dir = enemy.direction
    enemy.update()
    assert enemy.x == 2 * initial_dir
    # Zet vijand buiten rand en update
    enemy.x = 800
    prev_dir = enemy.direction
    enemy.update()
    # Richting keert om
    assert enemy.direction == -prev_dir
