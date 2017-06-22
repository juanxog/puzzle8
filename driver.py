import math
import copy

class node:

    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action



def move_up(universe, pos, action):

    if pos - 3 < 0:
        return False
    else:
        if action:
            universe[pos] = universe[pos - 3]
            universe[pos - 3] = 0
        return True

def move_down(universe, pos, action):

    if pos + 3 >= len(universe):
        return False
    else:
        if action:
            universe[pos] = universe[pos + 3]
            universe[pos + 3] = 0
        return True

def move_left(universe, pos, action):

    if pos in [0,3,6]:
        return False
    else:
        if action:
            universe[pos] = universe[pos - 1]
            universe[pos - 1] = 0
        return True

def move_right(universe, pos, action):

    if pos in [2,5,8]:
        return False
    else:
        if action:
            universe[pos] = universe[pos + 1]
            universe[pos + 1] = 0
    return True

def find_moves(universe,pos):

    posibilities = []

    if move_up(universe,pos,False):
        posibilities.append("UP")
    if move_down(universe,pos,False):
        posibilities.append("DOWN")
    if move_left(universe, pos,False):
        posibilities.append("LEFT")
    if move_right(universe, pos,False):
        posibilities.append("RIGHT")

    return posibilities

def action_moves(universe,pos,action):
    if action == 'UP':
        move_up(universe,pos,True)
    if action == 'DOWN':
        move_down(universe, pos, True)
    if action == 'LEFT':
        move_left(universe, pos, True)
    if action == 'RIGHT':
        move_right(universe, pos, True)


def isgoal(universe):

    goal = False

    for x in universe:
        if x == universe[x]:
            goal = True
        else:
            return False

    return goal


def main(universe):

    #posibles_moves = find_moves(universe,5)
    pos_zero = -1
    visited = []
    frontier = []
    frontier.append(universe)


    while len(frontier) <> 0:

        state = frontier.pop(-1)
        parent = copy.copy(state)
        visited.append(copy.copy(state))
        posibles_moves = find_moves(state, 5)

        for i in state:
            if state[i] == 0:
                pos_zero = i

        if isgoal(state):
            print("---------------------------------------------")
            print("metaaaaaaaaaaa")
            print(state)
            print("---------------------------------------------")
            print (frontier)
            print("---------------------------------------------")
            print (visited)


        for x in posibles_moves:
            aux_universe = copy.copy(state)
            action_moves(aux_universe,pos_zero,x)
            if(aux_universe not in visited and aux_universe not in frontier ):
                frontier.append(aux_universe)

            #print "*************************************************************"
            #print frontier
            #print "............................................................."
            #print visited
            #print "*************************************************************"


main([1,2,5,3,4,0,6,7,8])
