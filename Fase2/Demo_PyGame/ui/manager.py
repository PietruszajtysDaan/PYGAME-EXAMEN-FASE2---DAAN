import pygame
from data.json_manager import JSONManager


class UIManager:
    def __init__(self):
        self.state = 'menu'
        self.font = pygame.font.SysFont(None, 40)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == 'menu' and event.key == pygame.K_RETURN:
                self.state = 'playing'
            elif self.state == 'playing' and event.key == pygame.K_ESCAPE:
                self.state = 'menu'
                return 'end_game' 
            elif self.state == 'scoreboard' and event.key == pygame.K_ESCAPE:
                self.state = 'menu'
            elif self.state == 'menu' and event.key == pygame.K_s:
                self.state = 'settings'
            elif self.state == 'settings' and event.key == pygame.K_ESCAPE:
                self.state = 'menu'
            if event.key == pygame.K_ESCAPE:
                return 'quit' 

    def show_menu(self, surface):
        text = self.font.render('Press ENTER to Start', True, (255, 255, 255))
        surface.blit(text, (200, 250))
        txt2 = self.font.render('S for Settings', True, (255, 255, 255))
        surface.blit(txt2, (200, 300))

    def show_score(self, surface, score):
        txt = self.font.render(f'Score: {score}', True, (255, 255, 0))
        surface.blit(txt, (10, 10))

    def show_scoreboard(self, surface, scores):
        y = 100
        surface.fill((0, 0, 0))
        for entry in sorted(scores, key=lambda e: e['score'], reverse=True)[:5]:
            txt = self.font.render(f"{entry['name']}: {entry['score']}", True, (0, 255, 0))
            surface.blit(txt, (100, y))
            y += 50

    def show_settings(self, surface):
        settings = JSONManager.load_data('data/settings.json') or {'volume': 0.5, 'difficulty': 'normal'}
        surface.fill((10, 10, 10))
        txt1 = self.font.render(f"Volume: {settings['volume']}", True, (255, 255, 255))
        txt2 = self.font.render(f"Difficulty: {settings['difficulty']}", True, (255, 255, 255))
        surface.blit(txt1, (200, 200))
        surface.blit(txt2, (200, 260))