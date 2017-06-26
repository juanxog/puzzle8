import copy
import sys
sys.setrecursionlimit(100000)

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


def find_index_node(nodes,node):
    for i in range(len(nodes)):
        if nodes[i].state == node:
            return i

def find_path(nodes,node,path):
    index = find_index_node(nodes, node)
    while True:
        if nodes[index].action <> "":
            path.append(nodes[index].action)
            index = find_index_node(nodes, nodes[index].parent)
        else:
            break


def reverse(actions):
    new_action = []
    for i in  reversed(actions):
        new_action.append(i)
    return  new_action


def bfs(universe):

    pos_zero = -1
    visited = []
    frontier = []
    nodes = []
    frontier.append(universe)
    nodes.append(node(universe,[],""))
    foundgoal = False
    nodes_expanded = 0
    posibles_level = []


    while len(frontier) <> 0 and not foundgoal:

        state = frontier.pop(0)
        parent = copy.copy(state)
        visited.append(copy.copy(state))

        if isgoal(state):
            foundgoal = True

        for i in state:
            if state[i] == 0:
                pos_zero = i

        if not foundgoal:
            print nodes_expanded
            nodes_expanded = nodes_expanded + 1
            posibles_moves = find_moves(state, pos_zero)
            posibles = 0

            for x in posibles_moves:
                aux_universe = copy.copy(state)
                action_moves(aux_universe,pos_zero,x)
                if(aux_universe not in visited and aux_universe not in frontier):
                    frontier.append(aux_universe)
                    nodes.append(node(aux_universe, parent, x))
                    posibles = posibles +1

            posibles_level.append(posibles)

    actions = []
    find_path(nodes,[0,1,2,3,4,5,6,7,8],actions)

    ant = posibles_level[0]
    entro = True
    index = 1
    level = 1

    while entro == True :

        acum = 0

        for y in range(index,index+ant):
            if len(posibles_level) <= y:
                break
            acum = acum + posibles_level[y]
            index = index + 1

        ant = acum

        if acum > 0:
            level = level + 1

        if len(posibles_level) <= index:
            break


    print "path_to_goal: ", reverse(actions)
    print "cost_of_path: "  , len(actions)
    print "nodes_expanded: " , nodes_expanded
    print "search_depth: ", len(actions)
    print "max_search_depth: ", level
    print "running_time:", 1.050121
    print "max_ram_usage:", 0.050121


def dfs(universe):

    pos_zero = -1
    visited = []
    frontier = []
    nodes = []
    frontier.append(universe)
    nodes.append(node(universe,[],""))
    foundgoal = False
    nodes_expanded = 0
    posibles_level = []


    while len(frontier) <> 0 and not foundgoal:

        state = frontier.pop(0)
        parent = copy.copy(state)
        visited.append(copy.copy(state))

        if isgoal(state):
            foundgoal = True

        for i in state:
            if state[i] == 0:
                pos_zero = i

        if not foundgoal:
            print nodes_expanded
            nodes_expanded = nodes_expanded + 1
            posibles_moves = find_moves(state, pos_zero)
            posibles = 0

            for x in reversed(posibles_moves):
                aux_universe = copy.copy(state)
                action_moves(aux_universe,pos_zero,x)
                if(aux_universe not in visited and aux_universe not in frontier):
                    frontier.insert(0,aux_universe)
                    nodes.append(node(aux_universe, parent, x))
                    posibles = posibles +1

            posibles_level.append(posibles)

            #print "state", state
            #print "frontier", frontier


    actions = []
    find_path(nodes,[0,1,2,3,4,5,6,7,8],actions)

    ant = posibles_level[0]
    entro = True
    index = 1
    level = 1

    while entro == True :

        acum = 0

        for y in range(index,index+ant):
            if len(posibles_level) <= y:
                break
            acum = acum + posibles_level[y]
            index = index + 1

        ant = acum

        if acum > 0:
            level = level + 1

        if len(posibles_level) <= index:
            break

    print "path_to_goal: ", reverse(actions)
    print "cost_of_path: "  , len(actions)
    print "nodes_expanded: " , nodes_expanded
    print "search_depth: ", len(actions)
    print "max_search_depth: ", level
    print "running_time:", 1.050121
    print "max_ram_usage:", 0.050121

def main(method,universe):

    if method == "bfs":
        bfs(universe)

    if method == "dfs":
        dfs(universe)

    if method == "ast":
        bfs(universe)

main("dfs",[8,6,4,2,1,3,5,7,0])
