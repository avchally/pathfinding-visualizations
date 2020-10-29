"""


Sparseness: Sparse Mazes are produced by choosing to not grow the Maze in 
areas that would violate the rule of sparseness. A consistent way to implement 
this is to, whenever considering a new cell to carve into, to first check 
all cells within a semicircle of chosen cell radius located forward in the 
current direction. If any of those cells is already part of the Maze, don't 
allow the cell being considered, since doing to would be too close to an 
existing cell and hence make the Maze not sparse.

"""
import random
from data.algorithms.algorithm import Algorithm
import data.constants as c


class MazeGenerator(Algorithm):

    def start_algorithm(self, allow_diagonal=False):
        super().start_algorithm()
        self.graph.block_all()
        self.path_stack = [self.graph.get_node((1, 1))]

    def increment_algorithm(self):
        if self.running:
            while len(self.path_stack) > 0:
                current_node = self.path_stack.pop()
                current_node.state = c.N_BLANK
                valid_neighbors = []
                # print()
                # print(current_node.pos)
                for neighbor in self.graph.get_neighbors(current_node, allow_diagonal=False, ignore_blocked=False):
                    if neighbor and neighbor not in self.path_stack and neighbor.state != c.N_BLANK:
                        # print(neighbor.pos)
                        direction = (neighbor.row - current_node.row, neighbor.col - current_node.col)
                        if self.is_direction_valid(current_node, direction):
                            valid_neighbors.append(neighbor)
                if len(valid_neighbors) > 0:
                    next_node = random.choice(valid_neighbors)
                    next_node.state = c.N_BLANK
                    self.path_stack.append(current_node)
                    self.path_stack.append(next_node)
                if self.path_stack != []:
                    self.path_stack[-1].state = c.N_CLOSED_SET
            # else:
            self.running = False
            print('done')

    def is_direction_valid(self, current_node, direction):
        # print()
        # print(direction)
        # print(current_node.pos)
        try:
            for i in [1, 2]:
                for y in [-1, 0, 1]:
                    dir_y, dir_x = direction
                    node_y, node_x = current_node.pos
                    if dir_y == 0:
                        dir_y = y
                        dir_x *= i
                    elif dir_x == 0:
                        dir_x = y
                        dir_y *= i
                    # print(dir_y, dir_x, f'i:{i}, y:{y}')
                    if self.graph.get_node((node_y + dir_y, node_x + dir_x)).state == c.N_BLANK:
                        return False
        except AttributeError:
            return False
        return True
