import pygame
import data.constants as c
from data.screen_elements.app_element import AppElement


class Menu(AppElement):

    def __init__(self):
        super().__init__(c.MENU_WIDTH, c.MENU_HEIGHT, c.MENU_CENTER)
        self.bg_color = c.MENU_COLOR
        self.init_pygame_stuff()
        self.set_buttons()

    def process_event(self, event):
        pass

    def process_mouse_event(self, event, adj_mouse_pos, mouse):
        if event and event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.button_list:
                if button.rect.collidepoint(adj_mouse_pos):
                    button.on_press(mouse)

    def draw_rest(self):
        for button in self.button_list:
            button.draw(self.surf)

    def set_buttons(self):
        # self.button_list = [ClearSelector(c.M_CLEAR), CursorSelectorButton(c.M_BLOCK, (70, 30), (55, 20), (25, 25, 25), 'Block'),
        #                     StartSelector(c.M_START), GoalSelector(c.M_GOAL)]
        self.button_list = [CursorSelectorButton((70, 30), (55, 20), (25, 25, 25), 'Block', c.M_BLOCK),
                            CursorSelectorButton((70, 30), (135, 20), (125, 125, 125), 'Clear', c.M_CLEAR),
                            CursorSelectorButton((70, 30), (55, 60), (0, 0, 125), 'Start', c.M_START),
                            CursorSelectorButton((70, 30), (215, 20), (60, 60, 60), '+Weight', c.M_INC_WEIGHT),
                            CursorSelectorButton((70, 30), (135, 60), (125, 0, 0), 'Goal', c.M_GOAL),
                            CursorSelectorButton((70, 30), (215, 60), (225, 225, 225), '-Weight', c.M_DEC_WEIGHT)]


class Button:

    def __init__(self, size, pos, color, text):
        self.size = size
        self.pos = pos
        self.color = color
        self.text = text
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=pos)

    def draw(self, screen):
        self.surf.fill(self.color)
        screen.blit(self.surf, self.rect)


class CursorSelectorButton(Button):
    # TODO: compress cursor buttons to just the parent button

    def __init__(self, size, pos, color, text, cursor_setting):
        super().__init__(size, pos, color, text)
        self.cursor_setting = cursor_setting
        self.size = size
        self.pos = pos
        self.color = color
        self.text = text
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=pos)

    def on_press(self, cursor):
        cursor.cur_setting = self.cursor_setting


# class BlockSelector(CursorSelectorButton):

#     def __init__(self, cursor_setting):
#         super().__init__(cursor_setting)
#         self.surf = pygame.Surface((70, 30))
#         self.rect = self.surf.get_rect(center=(55, 20))
#         self.color = (25, 25, 25)


# class ClearSelector(CursorSelectorButton):

#     def __init__(self, cursor_setting):
#         super().__init__(cursor_setting)
#         self.surf = pygame.Surface((70, 30))
#         self.rect = self.surf.get_rect(center=(135, 20))
#         self.color = (125, 125, 125)


# class StartSelector(CursorSelectorButton):

#     def __init__(self, cursor_setting):
#         super().__init__(cursor_setting)
#         self.surf = pygame.Surface((70, 30))
#         self.rect = self.surf.get_rect(center=(55, 60))
#         self.color = (0, 0, 125)


# class GoalSelector(CursorSelectorButton):

#     def __init__(self, cursor_setting):
#         super().__init__(cursor_setting)
#         self.surf = pygame.Surface((70, 30))
#         self.rect = self.surf.get_rect(center=(135, 60))
#         self.color = (125, 0, 0)
