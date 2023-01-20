"""
D* grid planning

author: Nirnay Roy
"""
import math
import time
import argparse

from sys import maxsize
from GridManager import GridMaker

import matplotlib.pyplot as plt

show_animation = False


class State:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.state = "."
        self.t = "new"  # tag for state
        self.h = 0
        self.k = 0

    def cost(self, state):
        if self.state == "#" or state.state == "#":
            return maxsize

        return math.sqrt(math.pow((self.x - state.x), 2) +
                         math.pow((self.y - state.y), 2))

    def set_state(self, state):
        """
        .: new
        #: obstacle
        e: oparent of current state
        *: closed state
        s: current state
        """
        if state not in ["s", ".", "#", "e", "*"]:
            return
        self.state = state


class Map:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = self.init_map()

    def init_map(self):
        map_list = []
        for i in range(self.row):
            tmp = []
            for j in range(self.col):
                tmp.append(State(i, j))
            map_list.append(tmp)
        return map_list

    def get_neighbors(self, state):
        state_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if state.x + i < 0 or state.x + i >= self.row:
                    continue
                if state.y + j < 0 or state.y + j >= self.col:
                    continue
                state_list.append(self.map[state.x + i][state.y + j])
        return state_list

    def set_obstacle(self, point_list):
        for x, y in point_list:
            if x < 0 or x >= self.row or y < 0 or y >= self.col:
                continue

            self.map[x][y].set_state("#")


class Dstar:
    def __init__(self, maps):
        self.map = maps
        self.open_list = set()

    def process_state(self):
        x = self.min_state()

        if x is None:
            return -1

        k_old = self.get_kmin()
        self.remove(x)

        if k_old < x.h:
            for y in self.map.get_neighbors(x):
                if y.h <= k_old and x.h > y.h + x.cost(y):
                    x.parent = y
                    x.h = y.h + x.cost(y)
        elif k_old == x.h:
            for y in self.map.get_neighbors(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y) \
                        or y.parent != x and y.h > x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
        else:
            for y in self.map.get_neighbors(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
                else:
                    if y.parent != x and y.h > x.h + x.cost(y):
                        self.insert(y, x.h)
                    else:
                        if y.parent != x and x.h > y.h + x.cost(y) \
                                and y.t == "close" and y.h > k_old:
                            self.insert(y, y.h)
        return self.get_kmin()

    def min_state(self):
        if not self.open_list:
            return None
        min_state = min(self.open_list, key=lambda x: x.k)
        return min_state

    def get_kmin(self):
        if not self.open_list:
            return -1
        k_min = min([x.k for x in self.open_list])
        return k_min

    def insert(self, state, h_new):
        if state.t == "new":
            state.k = h_new
        elif state.t == "open":
            state.k = min(state.k, h_new)
        elif state.t == "close":
            state.k = min(state.h, h_new)
        state.h = h_new
        state.t = "open"
        self.open_list.add(state)

    def remove(self, state):
        if state.t == "open":
            state.t = "close"
        self.open_list.remove(state)

    def modify_cost(self, x):
        if x.t == "close":
            self.insert(x, x.parent.h + x.cost(x.parent))

    def run(self, start, end):

        rx = []
        ry = []

        self.insert(end, 0.0)

        while True:
            self.process_state()
            if start.t == "close":
                break

        start.set_state("s")
        s = start
        s = s.parent
        s.set_state("e")
        tmp = start

        while tmp != end:
            tmp.set_state("*")
            rx.append(tmp.x)
            ry.append(tmp.y)
            if show_animation:
                plt.plot(rx, ry, "-r")
                plt.pause(0.01)
            if tmp.parent.state == "#":
                self.modify(tmp)
                continue
            tmp = tmp.parent
        tmp.set_state("e")

        return rx, ry

    def modify(self, state):
        self.modify_cost(state)
        while True:
            k_min = self.process_state()
            if k_min >= state.h:
                break


def main():
    
     # Parser de argumentos
    parser = argparse.ArgumentParser()
    # Número del mapa
    parser.add_argument("-m", "--maze", type=int, help="Número del laberinto a procesar")
    args = parser.parse_args()
    maze = 1
    resize = 1

    # start and goal position
    sx = 5.0  # [m]
    sy = 3.0  # [m]
    gx = 80.0 # [m]
    gy = 40.0  # [m]

    if maze == 1:
        # start and goal position
        sx = 5.0  # [m]
        sy = 3.0  # [m]
        gx = 80.0 # [m]
        gy = 40.0  # [m]
        resize = 5
    
    elif maze == 2:
        # start and goal position
        sx = 60.0  # [m]
        sy = 115.0  # [m]
        gx = 60.0 # [m]
        gy = 60.0  # [m]
        resize = 2

    elif maze == 3:
        # start and goal position
        sx = 200.0  # [m]
        sy = 100.0  # [m]
        gx = 25.0 # [m]
        gy = 41.0  # [m]
        resize = 1

    elif maze == 4:
        # start and goal position
        sx = 120.0  # [m]
        sy = 30.0  # [m]
        gx = 93.0 # [m]
        gy = 74.0  # [m]
        resize = 9
    
    # Creamos un mapa
    gm = GridMaker('Mazes/maze' + str(maze) + '.png', resize)
    ox, oy = gm.ox, gm.oy

    m = Map(round(max(ox)), round(max(oy)))

    m.set_obstacle([(i, j) for i, j in zip(ox, oy)])

    start = [int(sx), int(sy)]
    goal = [int(gx), int(gy)]

    start = m.map[start[0]][start[1]]
    end = m.map[goal[0]][goal[1]]
    dstar = Dstar(m)
    rx, ry = dstar.run(start, end)

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.show()

def start(maze:int):
    '''Ejecuta el algortimo A* sobre el mapa indicado.'''
    print("Maze" + str(maze) +  " start!!")
    resize = 1

    if maze == 1:
        # start and goal position
        sx = 5.0  # [m]
        sy = 3.0  # [m]
        gx = 80.0 # [m]
        gy = 40.0  # [m]
        resize = 5
    
    elif maze == 2:
        # start and goal position
        sx = 60.0  # [m]
        sy = 115.0  # [m]
        gx = 60.0 # [m]
        gy = 60.0  # [m]
        resize = 2

    elif maze == 3:
        # start and goal position
        sx = 200.0  # [m]
        sy = 100.0  # [m]
        gx = 25.0 # [m]
        gy = 41.0  # [m]
        resize = 1

    elif maze == 4:
        # start and goal position
        sx = 120.0  # [m]
        sy = 30.0  # [m]
        gx = 93.0 # [m]
        gy = 74.0  # [m]
        resize = 9
    
    # Creamos un mapa
    gm = GridMaker('Mazes/maze' + str(maze) + '.png', resize)
    ox, oy = gm.ox, gm.oy

    m = Map(round(max(ox)), round(max(oy)))

    m.set_obstacle([(i, j) for i, j in zip(ox, oy)])

    start = [int(sx), int(sy)]
    goal = [int(gx), int(gy)]

    start = m.map[start[0]][start[1]]
    end = m.map[goal[0]][goal[1]]
    # Start Time
    start_time = time.perf_counter()

    # Execute algorithm
    dstar = Dstar(m)

    # Stop Time
    end_time = time.perf_counter()
    print("Tiempo de ejecución:", end_time - start_time)

    rx, ry = dstar.run(start, end)

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.show()

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()
    
    return end_time - start_time

if __name__ == '__main__':
    main()
