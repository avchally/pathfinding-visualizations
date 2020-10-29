import sys
import pygame
import data.constants as c
from data.algorithms.dijkstra import Dijkstra
from data.algorithms.maze_generator import MazeGenerator
from data.screen_elements.grid import Grid
from data.screen_elements.menu import Menu
from data.screen_elements.mouse import Mouse


class App:

    def __init__(self):
        self.settings = self.init_settings()
        self.load_pygame()
        self.grid = Grid()
        self.menu = Menu()
        self.cursor = Mouse(self)
        self.algorithm = Dijkstra(self.grid.graph)
        self.maze_generator = MazeGenerator(self.grid.graph)
        self.main_loop()

    def main_loop(self):
        while True:
            if not self.algorithm.running:
                for event in pygame.event.get():
                    self.process_event(event)
            self.update()
            self.draw()

            pygame.event.pump()
            pygame.display.update()
            # self.clock.tick(10)

    def process_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.algorithm.start_algorithm(self.allow_diagonal)
            if event.key == pygame.K_m:
                self.maze_generator.start_algorithm()
            if event.key == pygame.K_c:
                self.grid.graph.clear_all()
            if event.key == pygame.K_b:
                self.grid.graph.block_all()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            self.cursor.process_event(event, self.xy_to_element(self.cursor.pos))

    def update(self):
        self.algorithm.increment_algorithm()
        self.maze_generator.increment_algorithm()
        self.menu.update()
        self.grid.update()
        self.cursor.update()

    def draw(self):
        self.screen.fill(c.BG_COLOR)
        self.menu.draw(self.screen)
        self.grid.draw(self.screen)
        self.cursor.draw(self.screen)

    def xy_to_element(self, pos: tuple) -> tuple:
        """
        takes a screen coordinate and returns
        the screen element and its corresponding
        screen element coordinate as a tuple
        (element, coord_on_element)
        """
        element_pos_x = pos[0] - c.SCREEN_PADDING
        if pos[1] < c.CANVAS_START_Y:
            screen_element = self.menu
            element_pos_y = pos[1] - c.SCREEN_PADDING
        else:
            screen_element = self.grid
            element_pos_y = pos[1] - (c.CANVAS_START_Y)
        return (screen_element, (element_pos_x, element_pos_y))

    def init_settings(self):
        self.allow_diagonal = False

    def load_pygame(self):
        pygame.init()
        pygame.display.set_caption(c.WINDOW_CAPTIONS)
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
