#!/usr/bin/env python3

import numpy as np
import os
from time import sleep
from cell import Cell
import node
import layout
from layout import *
from node import *

# =======================  TOOLS  =============================

os.system('clear')


def buffer(n):
    i = 0
    while i < n:
        print(" ")
        i += 1


buffer(11)
print(f'      >>{" "*20}Welcome{" "*20}<<')
sleep(2)
i = 0
while i <= 20:
    os.system('clear')
    buffer(11)
    print(f'      {" "*(i)}>>{" "*(20-i)}Welcome{" "*(20-i)}<<')
    sleep(0.05)
    i += 1

# =======================  TOOLS  =============================

# ====================  USER INPUTS  ==========================
os.system('clear')
buffer(10)
print(f'''
                          Specify Mode:

                            1. Test
                            2. Run
''')
mode = int(input('                          > '))

os.system('clear')
if mode == 2:
    count = 1
    cell_resources = []
    while count <= 19:
        os.system('clear')
        buffer(10)
        while True:
            try:
                print(f'''
                    {cell_resources}
        ''')
                cell_resource = input(
                    f'                  Recurso de celda {count}: ')
                if (cell_resource not in ['p', 't', 'o', 'a', 'm', 'd']):
                    os.system('clear')
                    print(f'''                  Error! El recurso no existe,
                    asignale a la celda {count} un recurso adecuado!
                ''')
                    continue
                break
            except Exception as e:
                print('                 >> Error: %s' % e)
        cell_resources.append(cell_resource)
        count += 1

    count = 1
    cell_rolls = []
    while count <= 19:
        os.system('clear')
        while True:
            try:
                print(f'''
                    {cell_rolls}
        ''')
                cell_roll = int(
                    input(f'                  Numero de celda {count}: '))
                if (cell_roll not in range(2, 13)):
                    os.system('clear')
                    print(f'''                  Error! El numero no existe,
                    asignale a la celda {count} un numero adecuado!
                ''')
                    continue
                break
            except Exception as e:
                print('                 >> Error: %s' % e)
        cell_rolls.append(cell_roll)
        count += 1
else:
    cell_rolls = [5, 10, 8, 2, 9, 3, 4, 6, 4, 11, 6, 11, 3, 7, 5, 12, 8, 10, 9]
    cell_resources = list('ptoamtpmttmmpdoaoao')

# cell_rolls = list(map(lambda x: int(x),cell_rolls))

# ========================  END  ==============================


def score(roll):
    if roll in [6, 8]:
        return 5
    elif roll in [5, 9]:
        return 4
    elif roll in [4, 10]:
        return 3
    elif roll in [3, 11]:
        return 2
    elif roll in [2, 12]:
        return 1
    elif roll in [7]:
        return 0


# ================== Scoring Cell Rolls =======================
roll_score = np.array(list(map(score, cell_rolls)))
# print(roll_score)


# ======================  LIBRARY  ============================
resources = {
    "list": cell_resources,
    "abrv": {
        "m": "MADERA",
        "a": "ARCILLA",
        "o": "OVEJA",
        "t": "TRIGO",
        "p": "PIEDRA",
        "d": "DESIERTO"
    }
}

dice = list(range(2, 13))

# ========================  END  ==============================

cells_nodes = [[1, 5, 9, 13, 8, 4],
               [2, 6, 10, 14, 9, 5],
               [3, 7, 11, 15, 10, 6],
               [8, 13, 18, 23, 17, 12],
               [9, 14, 19, 24, 18, 13],
               [10, 15, 20, 25, 19, 14],
               [11, 16, 21, 26, 20, 15],
               [17, 23, 29, 34, 28, 22],
               [18, 24, 30, 35, 29, 23],
               [19, 25, 31, 36, 30, 24],
               [20, 26, 32, 37, 31, 25],
               [21, 27, 33, 38, 32, 26],
               [29, 35, 40, 44, 39, 34],
               [30, 36, 41, 45, 40, 35],
               [31, 37, 42, 46, 41, 36],
               [32, 38, 43, 47, 42, 37],
               [40, 45, 49, 52, 48, 44],
               [41, 46, 50, 53, 49, 45],
               [42, 47, 51, 54, 50, 46]]

cells = []
for id in range(1, len(cells_nodes) + 1):
    new_cell = Cell(id, resources, cells_nodes, cell_rolls, roll_score)
    cells.append(new_cell)

nodes = []
for id in range(1, 55):
    new_node = Node(id, cells_nodes, cell_resources, cells, roll_score)
    nodes.append(new_node)

action_string = '''

                        What element do you want to visualize?

                          1. Choose a cell.
                          2. Choose a node.
                          3. Top scores
                          4. Quit.

                        > '''


def query_cell():
    while True:
        try:
            buffer(10)
            query = int(input('                       What cell: ')) - 1
            if (query not in range(0, 19)):
                os.system('clear')
                print(f'''Error! only 19 cells available.
              Re-enter please
              ''')
                continue
            break
        except Exception as e:
            print('                       >> Error: %s' % e)

    os.system('clear')
    query_string = f'''
                  ===========================================================

                        Cell {query + 1}:

                          Resource: {cells[query].resource}
                          Nodes: {cells[query].nodes}
                          Roll: {cells[query].roll}
                          Score: {cells[query].score}'''
    print_layout()
    print(query_string)


def query_node():
    while True:
        try:
            buffer(10)
            query = int(input('                       What node: ')) - 1
            if (query not in range(0, 54)):
                os.system('clear')
                print(f'''Error! only 54 nodes available.
              Re-enter please
              ''')
                continue
            break
        except Exception as e:
            print('                       >> Error: %s' % e)

    os.system('clear')
    query_string = f'''
                  ===========================================================

                           Node {query + 1}:

                             Connected to cells: {nodes[query].connected_cells_id}
                             Adjacent to nodes: {nodes[query].adjacent_nodes}
                             in Row: {nodes[query].row}
                             in Column: {nodes[query].column}
                             Will get: {nodes[query].resources}
                             Score: {nodes[query].get_score(roll_score)}
  '''
    print_layout()
    print(query_string)


def query_score():
    os.system('clear')
    nodes_scores = np.array(list(map(lambda x: x.score, nodes)))
    max_score = np.amax(nodes_scores)
    first_scores = np.where(nodes_scores == max_score)[0]
    second_scores = np.where(nodes_scores == (max_score - 1))[0]
    third_scores = np.where(nodes_scores == (max_score - 2))[0]
    forth_scores = np.where(nodes_scores == (max_score - 3))[0]
    print_layout()
    print('')
    print(f'                    1st place nodes (score = {max_score}):')
    print('')
    for node in first_scores:
        print(
            f'       Node {nodes[node].id} on row: {nodes[node].row} col: {nodes[node].column} --> that gives: {nodes[node].resources}')
    print('')
    if second_scores.any():
        print(
            f'                    2nd place nodes (score = {max_score - 1}):')
        print('')
        for node in second_scores:
            print(
                f'       Node {nodes[node].id} on row: {nodes[node].row} col: {nodes[node].column} --> that gives: {nodes[node].resources}')
        print('')
    if third_scores.any():
        print(
            f'                    3rd place nodes (score = {max_score - 2}):')
        print('')
        for node in third_scores:
            print(
                f'       Node {nodes[node].id} on row: {nodes[node].row} col: {nodes[node].column} --> that gives: {nodes[node].resources}')
        print('')
    if forth_scores.any():
        print(
            f'                    4th place nodes (score = {max_score - 3}):')
        print('')
        for node in forth_scores:
            print(
                f'       Node {nodes[node].id} on row: {nodes[node].row} col: {nodes[node].column} --> that gives: {nodes[node].resources}')

# ====================  RUN PROGRAM  ==========================


print_layout()
run = True
while run:
    user_input = input(action_string)
    action = int(user_input) if user_input != '' else 0
    os.system('clear')
    if action == 1:
        query_cell()
    elif action == 2:
        query_node()
    elif action == 3:
        query_score()
    elif action == 4:
        print('Game Over')
        run = False
    else:
        print('Input a number from 1 to 3')


os.system('clear')
# ========================  END  ==============================
