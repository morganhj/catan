#!/usr/bin/env python3

import math


class Cell:
    def __init__(self, id, resources, cells_nodes, cell_roll, roll_score):
        self.id = id
        self.resource = resources["abrv"][resources["list"][id-1]]
        self.nodes = cells_nodes[id - 1]
        self.row = math.ceil(id / 4)
        self.column = self.get_column()
        self.roll = cell_roll[id - 1]
        self.score = roll_score[id - 1]

    def get_column(self):
        id = self.id
        if id in [8]:
            return 1
        elif id in [4, 13]:
            return 2
        elif id in [1, 9, 17]:
            return 3
        elif id in [5, 14]:
            return 4
        elif id in [2, 10, 18]:
            return 5
        elif id in [6, 15]:
            return 6
        elif id in [3, 11, 19]:
            return 7
        elif id in [7, 16]:
            return 8
        elif id in [12]:
            return 9
