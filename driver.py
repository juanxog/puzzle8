import math

def move_up(universe, pos, action):

    if pos - 3 < 0:
        return False
    else:
        if action:
            universe[pos] = universe[pos - 3]
            universe[pos - 3] = 0
        return True

def move_down(universe, pos, action):

    if pos + 3 > len(universe):
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
    if move_up(universe,pos,False):
        print "UP"
    if move_down(universe,pos,False):
        print "DOWN"
    if move_left(universe, pos,False):
        print "LEFT"
    if move_right(universe, pos,False):
        print "RIGHT"

def action_moves(universe,pos,action):
    if action == 'UP':
        move_up(universe,pos,True)
    if action == 'DOWN':
        move_down(universe, pos, True)
    if action == 'LEFT':
        move_left(universe, pos, True)
    if action == 'RIGHT':
        move_right(universe, pos, True)


def main():
        universe = [1, 2, 5, 3, 4, 0, 6, 7, 8]
        find_moves(universe,5)




main()
