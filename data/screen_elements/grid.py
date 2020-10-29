import pygame
import data.constants as c
from data.screen_elements.app_element import AppElement
from data.graph import Graph


class Grid(AppElement):

    def __init__(self):
        super().__init__(c.CANVAS_WIDTH, c.CANVAS_HEIGHT, c.CANVAS_CENTER)
        self.bg_color = c.CANVAS_COLOR
        self.init_pygame_stuff()
        self.graph = Graph(c.DEFAULT_ROWS, c.DEFAULT_COLS)
        # TODO: find a way to clean up node_length (find somewhere else for it?)
        self.node_len = int((c.CANVAS_WIDTH + c.NODE_PADDING) / self.graph.cols - c.NODE_PADDING)

    def process_event(self, event):
        pass

    def process_mouse_event(self, event, adj_mouse_pos, mouse):
        node_pos = self.screen_pos_to_grid_pos(adj_mouse_pos)
        node = self.graph.get_node(node_pos)
        if node:
            if mouse.cur_setting == c.M_BLOCK:
                node.state = c.N_BLOCKED
            if mouse.cur_setting == c.M_CLEAR:
                node.weight = 0
                node.state = c.N_BLANK
            if mouse.cur_setting == c.M_START:
                self.graph.set_start(node_pos)
            if mouse.cur_setting == c.M_GOAL:
                self.graph.set_goal(node_pos)
            if mouse.cur_setting == c.M_INC_WEIGHT:
                if node.state == c.N_BLANK:
                    node.weight += 1
            if mouse.cur_setting == c.M_DEC_WEIGHT:
                if node.state == c.N_BLANK:
                    node.weight -= 1
                    if node.weight < 0:
                        node.weight = 0


    def draw_rest(self):
        """
        draws the remaining pieces of the screen elements
        and routes it back into the parent class's draw
        method
        """
        for row in self.graph.node_list:
            for node in row:
                node_x, node_y = self.grid_pos_to_screen_pos(node.pos)
                node_color = r, g, b = c.NODE_COLORS[node.state]
                if node.state in [c.N_BLANK, c.N_OPEN_SET, c.N_CLOSED_SET]:
                    r -= node.weight*10
                    g -= node.weight*10
                    b -= node.weight*10
                    if r <= 0: r = 0
                    if g <= 0: g = 0
                    if b <= 0: b = 0
                    node_color = (r, g, b)
                pygame.draw.rect(self.surf, node_color, [node_x, node_y, self.node_len, self.node_len])

    def grid_pos_to_screen_pos(self, pos: tuple) -> tuple:
        """
        converts the (row, col) pos to the canvas xy
        coordinates of the center of the respective
        node
        """
        row, col = pos
        node_center_x = (self.node_len + c.NODE_PADDING)*col  # + node_len/2
        node_center_y = (self.node_len + c.NODE_PADDING)*row  # + node_len/2
        return (node_center_x, node_center_y)

    def screen_pos_to_grid_pos(self, pos: tuple) -> tuple:
        """
        converts the (x, y) pos to the (row, col)
        of the grid, i.e. the node indices
        """
        x, y = pos
        row = int(y / (float(c.CANVAS_HEIGHT) / self.graph.rows))
        col = int(x / (float(c.CANVAS_WIDTH) / self.graph.cols))
        if row < 0:
            row = 0
        if col < 0:
            col = 0
        return (row, col)
