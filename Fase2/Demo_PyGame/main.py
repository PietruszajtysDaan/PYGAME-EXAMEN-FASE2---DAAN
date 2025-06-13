# Voorbeeld Pygame Project
# Structuur:
#   main.py
#   engine/game.py
#   data/json_manager.py
#   data/highscores.json
#   data/settings.json
#   entities/entity.py
#   entities/player.py
#   entities/enemy.py
#   ui/manager.py

# File: main.py
import pygame
from engine.game import GameEngine

if __name__ == '__main__':
    pygame.init()
    engine = GameEngine()
    engine.run()
    pygame.quit()








# File: data/highscores.json
# []

# File: data/settings.json
# {
#   "volume": 0.5,
#   "difficulty": "normal"
# }











# Einde voorbeeldproject
# Uitleg: vul data/highscores.json en settings.json aan, speel met parameters,
# voeg nieuwe Entity-klassen toe of menu-items om de toetsvragen te beantwoorden.

