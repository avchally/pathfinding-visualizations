import random
import data.constants as c


class Node:

    def __init__(self, pos):
        self.pos = pos
        self.row, self.col = pos
        self.state = c.N_BLANK
        self.screen_pos = None
        self.color = c.NODE_COLORS[self.state]
        self.weight = 0

    def update(self):
        self.color = c.NODE_COLORS[self.state]

    def __str__(self):
        return str(self.pos)

    def __lt__(self, other):
        return random.randrange(2) == 1

    def __le__(self, other):
        return random.randrange(2) == 1


class Graph:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.node_list = self.generate_nodes()
        self.start_node = None
        self.goal_node = None

    def generate_nodes(self):
        """in its own method to declutter __ini__"""
        return [[Node((row, col)) for col in range(self.cols)] for row in range(self.rows)]

    def get_node(self, pos):
        """returns the node at the (row, col) pos"""
        if pos[0] < self.rows and pos[0] >= 0 and pos[1] < self.cols and pos[1] >= 0:
            return self.node_list[pos[0]][pos[1]]

    def set_start(self, pos):
        """sets the node's state at (row, col) pos to be start"""
        if self.start_node:
            self.start_node.state = c.N_BLANK
        start_node = self.get_node(pos)
        start_node.state = c.N_START
        self.start_node = start_node

    def set_goal(self, pos):
        """sets the node's state at (row, col) pos to be start"""
        if self.goal_node:
            self.goal_node.state = c.N_BLANK
        goal_node = self.get_node(pos)
        goal_node.state = c.N_GOAL
        self.goal_node = goal_node

    def block_all(self):
        for row in self.node_list:
            for node in row:
                node.state = c.N_BLOCKED

    def clear_all(self):
        for row in self.node_list:
            for node in row:
                node.state = c.N_BLANK

    def get_neighbors(self, node, allow_diagonal=True, ignore_blocked=True):
        neighbor_list = []
        if allow_diagonal:
            possible_movements = [(-1, -1), (-1, 0), (-1, 1),
                                  (0, -1), (0, 1),
                                  (1, -1), (1, 0), (1, 1)]
        else:
            possible_movements = [(-1, 0),
                                  (0, -1), (0, 1),
                                  (1, 0)]
        for move in possible_movements:
            try:
                row_pos = node.pos[0] + move[0]
                col_pos = node.pos[1] + move[1]
                if row_pos == -1:
                    row_pos = 0
                if col_pos == -1:
                    col_pos = 0
                this_node = self.get_node((row_pos, col_pos))
                if ignore_blocked:
                    if this_node.state != c.N_BLOCKED:
                        neighbor_list.append(this_node)
                else:
                    neighbor_list.append(this_node)
            except Exception:
                pass
        return neighbor_list
