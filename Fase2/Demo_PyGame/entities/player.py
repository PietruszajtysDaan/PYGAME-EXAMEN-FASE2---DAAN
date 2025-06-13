import pygame, random
from entities.entity import Entity

class Player(Entity):
    def __init__(self, x, y, speed):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.speed = speed
        self.color = (0, 0, 255)  # Blue
        # IMPLEMENTATIE FASE2
        self.activateSB = False
        self.activateDP = False
        self.activateTP = False

    # Dit checked welke knop je hebt getoetst
    def update(self, playerboost):
        keys = pygame.key.get_pressed()
        # IMPLEMENTATIE FASE2
        if keys[pygame.K_SPACE]:
            self.activateSB = True
        if keys[pygame.K_LCTRL]:
            self.activateDP = True
        else:
            self.activateDP = False
        if keys[pygame.K_LSHIFT]:
            self.activateTP = True
        else:
            self.activateTP = False
            
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * playerboost
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * playerboost
        if keys[pygame.K_UP]:
            self.y -= self.speed * playerboost
        if keys[pygame.K_DOWN]:
            self.y += self.speed * playerboost

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

class Powerup:
    def __init__(self, surface):
        self.screen = surface
        self.font = pygame.font.SysFont(None, 40)
    
    # Wanneer Speedboost wordt opgestart zal het iets op het scherm schrijven en daarna zal het boostamount returnen
    def Speedboost(self, boostamount: float):
        text = self.font.render('SPEEDBOOST', True, (0, 255, 255))
        self.screen.blit(text, self.screen.get_rect().center)
        return boostamount
    
    # Wanneer Deactivate wordt opgestart zal de character zijn normale snelheid weer krijgen.
    def Deactivate(self, normalspeed,normalcolor, txt):
        if txt == "SB":
            return normalspeed
        if txt == "DP":
            return [normalspeed, normalcolor]
    
    # IMPLEMENTATIE FASE2
    def DoublePoints(self, speed):
        newspeed = speed / 2
        newcolor = (255,255,0)
        return [newspeed, newcolor]
    def Teleport(self, x, y):
        x = random.randint(0,800)
        y = random.randint(0,600)
        return [x,y]
                
    
    