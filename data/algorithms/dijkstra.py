from queue import PriorityQueue
from data.algorithms.algorithm import Algorithm
import data.constants as c


class Dijkstra(Algorithm):

    def start_algorithm(self, allow_diagonal=True):
        super().start_algorithm()
        self.path = []
        self.drawing_path = False
        self.allow_diagonal = allow_diagonal
        self.open_set = PriorityQueue()
        self.open_set.put((0, self.graph.start_node))
        self.closed_set = {}
        self.cost_so_far = {}
        self.closed_set[self.graph.start_node] = None
        self.cost_so_far[self.graph.start_node] = 0

    def increment_algorithm(self):
        if self.running:
            if self.open_set.empty():
                # handles no path found
                self.running = False
                return
            else:
                current_node = self.open_set.get()[1]
                if current_node.state not in [c.N_START, c.N_GOAL]:
                    current_node.state = c.N_CLOSED_SET
                if current_node == self.graph.goal_node:
                    self.running = False
                    self.drawing_path = True
                    current_node.state = c.N_GOAL
                    self.path.append(current_node)
                    self.get_path()
                else:
                    for next_node in self.graph.get_neighbors(current_node, self.allow_diagonal):
                        prev_cost = self.cost_so_far[current_node]
                        new_cost = prev_cost + self.get_cost(current_node, next_node)
                        if next_node not in self.cost_so_far or new_cost < self.cost_so_far[next_node]:
                            self.cost_so_far[next_node] = new_cost
                            self.open_set.put((new_cost, next_node))
                            next_node.state = c.N_OPEN_SET
                            self.closed_set[next_node] = current_node
        if self.drawing_path:
            if len(self.path) != 0: #current_node != self.graph.goal_node:
                current_node = self.path.pop()
                if current_node.state not in [c.N_GOAL, c.N_START]:
                    current_node.state = c.N_PATH
            else:
                self.drawing_path = False

    def get_path(self):
        current_node = self.path[-1]
        while current_node != self.graph.start_node:
            current_node = self.closed_set[current_node]
            self.path.append(current_node)
        # self.path.reverse()

    def get_cost(self, start_node, dest_node):
        if self.allow_diagonal:
            dist_cost = self.calc_sl_dist(start_node, dest_node)
        else:
            dist_cost = self.calc_xy_dist(start_node, dest_node)

        node_weight = dest_node.weight
        return dist_cost + node_weight
