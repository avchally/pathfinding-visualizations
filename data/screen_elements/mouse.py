import pygame
import data.constants as c


class Mouse:

    def __init__(self, app):
        self.cur_setting = c.M_BLOCK
        self.clicking = False
        self.pos = None
        self.app = app

    def process_event(self, event, screen_info):
        """
        directs the mouse event to the proper screen
        element (either the grid or the menu)
        """
        screen_element_obj, adj_mouse_pos = screen_info
        if event:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.clicking = False
        screen_element_obj.process_mouse_event(event, adj_mouse_pos, self)

    def draw(self, screen):
        if self.mouse_in_bounds(screen):
            c_surf = pygame.Surface((7, 7))
            c_surf.fill(c.CURSOR_COLOR[self.cur_setting])
            c_rect = c_surf.get_rect(center=self.pos)
            screen.blit(c_surf, c_rect)

    def update(self):
        self.pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.mouse_in_bounds(self.app.screen):
            self.process_event(None, self.app.xy_to_element(self.pos))

    def mouse_in_bounds(self, screen):
        """
        determines whether the mouse is within the bounds
        of the window
        """
        w, h = screen.get_size()
        p = pygame.mouse.get_pos()
        return p[0] > 0 and p[0] < w and p[1] > 0 and p[1] < h
