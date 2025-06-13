import pygame  # Import pygame to use its drawing functions
from entities.entity import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)  # Red
        self.direction = 1

    def update(self):
        # Move back and forth
        self.x += 2 * self.direction
        if self.x < 0 or self.x > 750:
            self.direction *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))