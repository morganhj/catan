#!/usr/bin/env python3

import numpy as np


class Node:
    def __init__(self, id, cells_nodes, cell_resources, cells, roll_score):
        self.id = id
        self.cells_nodes = cells_nodes
        self.row = self.get_row()
        self.column = self.get_column()
        self.connected_cells_id = self.info().get("connected_cells")
        self.connected_cells = np.array(cells)[list(
            map(lambda x: x-1, self.connected_cells_id))]
        self.adjacent_nodes = self.info().get("adjacent_nodes")
        self.resources = self.gets_resources(cell_resources)
        self.score = self.get_score(roll_score)

    def info(self):
        cells_array = []
        adj_nodes = []
        for sub_array in self.cells_nodes:
            if self.id in sub_array:
                idx = sub_array.index(self.id)
                cells_array.append(self.cells_nodes.index(sub_array) + 1)
                idx_before = 5 if (idx == 0) else (idx - 1)
                idx_after = 0 if (idx == 5) else (idx + 1)
                if sub_array[idx_before] not in adj_nodes:
                    adj_nodes.append(sub_array[idx_before])
                if sub_array[idx_after] not in adj_nodes:
                    adj_nodes.append(sub_array[idx_after])
        node_info = {
            "connected_cells": cells_array,
            "adjacent_nodes": adj_nodes
        }
        return node_info

    def get_row(self):
        id = self.id
        if id <= 3:
            return 1
        elif id <= 7:
            return 2
        elif id <= 11:
            return 3
        elif id <= 16:
            return 4
        elif id <= 21:
            return 5
        elif id <= 27:
            return 6
        elif id <= 33:
            return 7
        elif id <= 38:
            return 8
        elif id <= 43:
            return 9
        elif id <= 47:
            return 10
        elif id <= 51:
            return 11
        elif id <= 54:
            return 12
        else:
            None

    def get_column(self):
        id = self.id
        if id in [22, 28]:
            return 1
        elif id in [12, 17, 34, 39]:
            return 2
        elif id in [4, 8, 23, 29, 44, 48]:
            return 3
        elif id in [1, 13, 18, 35, 40, 52]:
            return 4
        elif id in [5, 9, 24, 30, 45, 49]:
            return 5
        elif id in [2, 14, 19, 36, 41, 53]:
            return 6
        elif id in [6, 10, 25, 31, 46, 50]:
            return 7
        elif id in [3, 15, 20, 37, 42, 54]:
            return 8
        elif id in [7, 11, 26, 32, 47, 51]:
            return 9
        elif id in [16, 21, 38, 43]:
            return 10
        elif id in [27, 33]:
            return 11

    def gets_resources(self, cell_resources):
        resources = []
        for cell in self.connected_cells:
            resources.append(cell.resource)
        return resources

    def get_score(self, roll_score):
        score = 0
        for cell in self.connected_cells:
            score += cell.score
        return score
