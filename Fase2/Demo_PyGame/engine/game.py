import pygame, time
from ui.manager import UIManager
from data.json_manager import JSONManager
from entities.player import Player, Powerup
from entities.enemy import Enemy


class GameEngine:
    def __init__(self):
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Voorbeeld Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ui = UIManager()
        self.players = []
        self.enemies = []
        self.scores = JSONManager.load_data("data/highscores.json")
        print("Scores loaded:", self.scores)
        self.current_score = 0
        # Toegevoegde attributen voor Examen
        self.powerup = Powerup(self.screen)
        self.endtime = 0
        self.loop = False
        self.playerspeed = 2
        # IMPLEMENTATIE FASE2
        self.DP = False
        self.TP = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle window close
                    self.running = False
                else:
                    action = self.ui.handle_input(event)
                if action == "quit":  # Handle ESC key to quit
                    self.running = False
                elif action == "end_game":  # Handle end game signal
                    self.end_game(
                        "Player1"
                    )  # Replace "Player1" with actual player name input
            if self.ui.state == "playing":
                self.update()
                print(round(self.endtime))
            self.render()
            self.clock.tick(60)

    def update(self):
        if not self.players:
            self.players.append(Player(100, 100, self.playerspeed))
        if not self.enemies:
            self.enemies.append(Enemy(400, 100))
            
        for p in self.players:
            
            # IMPLEMENTATIE FASE2
            # Als je LSHFT indrukt dan zal je ergens random geplaatst worden
            if p.activateTP == True:
                p.x = self.powerup.Teleport(p.x,p.y)[0]
                p.y = self.powerup.Teleport(p.x,p.y)[1]
                self.TP = True
            else:
                self.TP = False
                
            # IMPLEMENTATIE FASE2
            # Als je LCTRL indrukt dan zal je punten gedubbled worden
            if p.activateDP == True:
                p.color = self.powerup.DoublePoints(self.playerspeed)[1]
                self.DP = True
            else:
                p.color = self.powerup.Deactivate(self.playerspeed, (0,0,255), "DP")[1]
                self.DP = False
            
            if round(self.endtime) == 0 and self.loop:
                p.activateSB = False
                self.loop = False
                p.speed = self.powerup.Deactivate(self.playerspeed,0,"SB")
            if p.activateSB == True and round(self.endtime) == 0:
                self.endtime = 5
                self.loop = True
                p.speed *= self.powerup.Speedboost(2)
            elif round(self.endtime) > 0:
                self.endtime -= 0.016
            
            p.update(p.speed)
        for e in self.enemies:
            e.update()
        distx = abs(self.players[0].x - self.enemies[0].x)
        disty = abs(self.players[0].y - self.enemies[0].y)
        distc = abs((distx ** 2 + disty ** 2) ** 0.5)
        self.current_score = round(max(0, 1000 - distc))
        
        # IMPLEMENTATIE FASE2
        if self.DP:
            self.current_score *= 2


    def render(self):
        self.font = pygame.font.SysFont(None, 40)
        self.screen.fill((30, 30, 30))
        if self.ui.state == "menu":
            self.ui.show_menu(self.screen)
        elif self.ui.state == "playing":
            for p in self.players:
                
                # IMPLEMENTATIE FASE2
                if p.activateDP == True:
                    txt = self.font.render(f'DOUBLEPOINTS', True, (255, 255, 0))
                    self.screen.blit(txt, (10, 40))   
                if p.activateTP == True:
                    txt = self.font.render(f'TELEPORTING...', True, (255, 255, 0))
                    self.screen.blit(txt, (10, 70))
                    
                # Door dit komt "Speedboost" op het scherm.
                if p.activateSB == True:
                    self.powerup.Speedboost(1)
                p.draw(self.screen)
            for e in self.enemies:
                e.draw(self.screen)
            self.ui.show_score(self.screen, self.current_score)
        elif self.ui.state == "scoreboard":
            self.ui.show_scoreboard(self.screen, self.scores)
        elif self.ui.state == "settings":
            self.ui.show_settings(self.screen)
        pygame.display.flip()

    def end_game(self, name):
        entry = {
            "name": name,
            "score": self.current_score,
            "date": pygame.time.get_ticks(),
        }
        self.scores.append(entry)
        JSONManager.save_data("data/highscores.json", self.scores)
        print("Scores saved:", self.scores)
        self.ui.state = "scoreboard"
