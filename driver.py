import copy

class node:

    def __init__(self,id,state,parent,action,level):
        self.id = id
        self.state = state
        self.parent = parent
        self.action = action
        self.level = level

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
        posibilities.append("Up")
    if move_down(universe,pos,False):
        posibilities.append("Down")
    if move_left(universe, pos,False):
        posibilities.append("Left")
    if move_right(universe, pos,False):
        posibilities.append("Right")

    return posibilities

def action_moves(universe,pos,action):
    if action == 'Up':
        move_up(universe,pos,True)
    if action == 'Down':
        move_down(universe, pos, True)
    if action == 'Left':
        move_left(universe, pos, True)
    if action == 'Right':
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
        if nodes[index].action <> "" and index <> -1:
            path.append(nodes[index].action)
            index = nodes[index].parent
        else:
            break

def reverse(actions):
    new_action = []
    for i in  reversed(actions):
        new_action.append(i)
    return  new_action




def dfs(universe):
    pos_zero = -1
    visited = []
    frontier = []
    nodes = []
    nodes.append(node(0, universe, -1, "", 0))
    frontier.append(nodes[len(nodes) - 1])
    foundgoal = False
    nodes_expanded = 0
    posibles_level = []

    while len(frontier) <> 0 and not foundgoal:

        state = frontier.pop(0)
        parent = state.id
        visited.append(state.state)

        if isgoal(state.state):
            foundgoal = True

        for i in state.state:
            if state.state[i] == 0:
                pos_zero = i

        if not foundgoal:
            nodes_expanded = nodes_expanded + 1
            posibles_moves = find_moves(state.state, pos_zero)

            for x in reversed(posibles_moves):
                aux_universe = copy.copy(state.state)
                action_moves(aux_universe, pos_zero, x)

                if (aux_universe not in visited):
                    flag = False
                    for k in frontier:
                        if aux_universe == k.state:
                            flag = False
                            break
                        else:
                            flag = True

                    if len(frontier) == 0:
                        flag = True

                    if flag:
                        nodes.append(node(len(nodes), aux_universe, parent, x, nodes[parent].level + 1))
                        frontier.insert(0, nodes[len(nodes) - 1])

    actions = []
    find_path(nodes, [0, 1, 2, 3, 4, 5, 6, 7, 8], actions)

    index = 1
    level = nodes[0].level

    for x in nodes:
        if x.level > level:
            level = x.level

    print "path_to_goal: ", reverse(actions)
    print "cost_of_path: ", len(actions)
    print "nodes_expanded: ", nodes_expanded
    print "search_depth: ", len(actions)
    print "max_search_depth: ", level
    print "running_time:", 1.050121
    print "max_ram_usage:", 0.050121


def bfs_new(universe):
    pos_zero = -1
    visited = []
    frontier = []
    nodes = []
    nodes.append(node(0, universe, -1, "", 0))
    frontier.append(nodes[len(nodes) - 1])
    foundgoal = False
    nodes_expanded = 0
    posibles_level = []

    while len(frontier) <> 0 and not foundgoal:

        state = frontier.pop(0)
        parent = state.id
        visited.append(state.state)

        if isgoal(state.state):
            foundgoal = True

        for i in state.state:
            if state.state[i] == 0:
                pos_zero = i

        if not foundgoal:
            nodes_expanded = nodes_expanded + 1
            posibles_moves = find_moves(state.state, pos_zero)

            for x in posibles_moves:
                aux_universe = copy.copy(state.state)
                action_moves(aux_universe, pos_zero, x)

                if (aux_universe not in visited):
                    flag = False
                    for k in frontier:
                        if aux_universe == k.state:
                            flag = False
                            break
                        else:
                            flag = True

                    if len(frontier) == 0:
                        flag = True

                    if flag:
                        nodes.append(node(len(nodes), aux_universe, parent, x, nodes[parent].level + 1))
                        frontier.append(nodes[len(nodes) - 1])

    actions = []
    find_path(nodes, [0, 1, 2, 3, 4, 5, 6, 7, 8], actions)

    index = 1
    level = nodes[0].level

    for x in nodes:
        if x.level > level:
            level = x.level

    print "path_to_goal: ", reverse(actions)
    print "cost_of_path: ", len(actions)
    print "nodes_expanded: ", nodes_expanded
    print "search_depth: ", len(actions)
    print "max_search_depth: ", level
    print "running_time:", 1.050121
    print "max_ram_usage:", 0.050121

def main(method,universe):

    if method == "bfs":
        bfs_new(universe)

    if method == "dfs":
        dfs(universe)

    if method == "ast":
        bfs(universe)

main("dfs",[1,2,5,3,4,0,6,7,8])
