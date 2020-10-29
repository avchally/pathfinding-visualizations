import math


class Algorithm:

    def __init__(self, graph):
        self.running = False
        self.graph = graph
        self.allow_diagonal = True
        self.path = []
        self.drawing_path = False

    def start_algorithm(self):
        self.running = True

    def increment_algorithm(Self):
        """
        !! update in child classes !!

        """
        pass

    def get_cost(self, start_node, dest_node):
        """
        !! update in child classes !!

        """
        pass

    def calc_xy_dist(self, node_1, node_2):
        return abs(node_1.pos[0] - node_2.pos[0]) + abs(node_1.pos[1] - node_2.pos[1])

    def calc_sl_dist(self, node_1, node_2):
        a = node_1.pos[0] - node_2.pos[0]
        b = node_1.pos[1] - node_2.pos[1]
        return math.sqrt(a**2 + b**2)
