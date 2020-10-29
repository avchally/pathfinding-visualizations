import pygame


class AppElement:

    def __init__(self, width: int, height: int, center: tuple):
        self.width = width
        self.height = height
        self.center = center
        self.bg_color = None
        self.init_pygame_stuff()

    def init_pygame_stuff(self):
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect(center=self.center)

    def draw(self, screen):
        self.surf.fill(self.bg_color)
        self.draw_rest()
        screen.blit(self.surf, self.rect)

    def update(self):
        """
        !!must be fully defined within child classes!!
        updates the rest of the screen element and its features
        """
        pass

    def draw_rest(self):
        """
        !!must be fully defined within child classes!!
        draws the rest of the screen element and its features
        """
        pass
