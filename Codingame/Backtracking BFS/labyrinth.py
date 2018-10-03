"""
Kirk just got out of the spaceship and has to join the control room of the base, lost deep down in a labyrinth full of corridors 
and dead ends.You will have to help the Captain find his way out of this, but beware: the clock is running. Tick Tock.

https://www.codingame.com/training/hard/the-labyrinth/
"""


import sys
import math
from queue import deque



# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

c_flag = False
comp_flag = False
back_flag = False
back_path = []
fwd_dirxn = ""
fwd_path = []       # from T to current posn of Kirk


# get path
def BFS_labyrinth(grid, c_flag, r, c, t_flag, source, target_char):
    q = deque()
    q.append(source)  # append S
    print("hele", source, file=sys.stderr)
    visited = {}
    dirxn_ret = ""
    parent = {}
    parent[source] = [None, None, None]  # v:[dirxn, parent of v]
    visited[source] = True

    while len(q) != 0:
        flag_r, flag_u, flag_l, flag_d = False, False, False, False
        f1, f2, f3, f4 = False, False, False, False
        current = q.popleft()
        print(current, file=sys.stderr)

        # RIGHT
        next = (current[0], current[1] + 1)
        if current[1] + 1 < c and grid[current[0]][current[1] + 1] != '#' and next not in visited:  # RIGHT

            if current == source:  # start
                parent[next] = ['RIGHT', current, 'RIGHT']
            else:
                parent[next] = ['RIGHT', current, parent[current][2]]
                # this I am doing for closest ?

            if grid[current[0]][current[1] + 1] != ".":

                if grid[current[0]][current[1] + 1] == target_char:  # 'C' / 'T'
                    # found a path from current to C. Now make a path from curr to C
                    parent[next] = ['RIGHT', current, parent[current][2]]  # current is parent
                    path = get_fwd_path(parent, next, source)

                    # if the target is C then return path_to_C
                    if t_flag is False:

                        # find full_path_from C to T. back path
                        full_path = BFS_labyrinth(grid=grid, c_flag=True, r=r, c=c,
                                                  t_flag=True, source=next, target_char='T')
                        return path, full_path, True

                    # in BFS for finding back path to T from C
                    else:  # if finding path to T from C then simply return the complete path
                        return path

                elif grid[current[0]][current[1] + 1] == '?':
                    if dirxn_ret == "":  # first time
                        if current == source:
                            dirxn_ret = 'RIGHT'
                        else:
                            dirxn_ret = parent[current][2]
                        if not c_flag:  # return from here only when C is not in the grid
                            return dirxn_ret
                else:
                    q.append(next)  # special for T in grid
                    visited[next] = True        

            else:
                q.append(next)
                visited[next] = True  # add to visited: True
        else:
            f1 = True
            if grid[current[0]][current[1] + 1] == '.':
                flag_r = True

        # LEFT
        next = (current[0], current[1] - 1)
        if current[1] - 1 > -1 and grid[current[0]][current[1] - 1] != '#' and next not in visited:  # LEFT

            if current == source:  # start
                parent[next] = ['LEFT', current, 'LEFT']
            else:
                parent[next] = ['LEFT', current, parent[current][2]]

            if grid[current[0]][current[1] - 1] != ".":
                if grid[current[0]][current[1] - 1] == target_char:
                    # found a path from current to C. Now make a path from curr to C
                    parent[next] = ['LEFT', current, parent[current][2]]  # current is parent
                    path = get_fwd_path(parent, next, source)

                    # if the target is C then return path_to_C
                    if t_flag is False:

                        # find full_path_from C to T. back path
                        full_path = BFS_labyrinth(grid=grid, c_flag=True, r=r, c=c,
                                                  t_flag=True, source=next, target_char='T')
                        return path, full_path, True

                    # in BFS for finding back path to T from C
                    else:  # if finding path to T from C then simply return the complete path
                        return path
                elif grid[current[0]][current[1] - 1] == '?':
                    if dirxn_ret == "":  # first time
                        if current == source:
                            dirxn_ret = 'LEFT'
                        else:
                            dirxn_ret = parent[current][2]
                        if not c_flag:  # return from here only when C is not in the grid
                            return dirxn_ret
                else:
                    q.append(next)  # special for T in grid
                    visited[next] = True    

            else:
                q.append(next)
                visited[next] = True  # add to visited: True
        else:
            f4 = True
            if grid[current[0]][current[1] - 1] == '.':
                flag_l = True

        # RIGHT
        next = (current[0], current[1] + 1)
        if current[1] + 1 < c and grid[current[0]][current[1] + 1] != '#' and next not in visited:  # RIGHT

            if current == source:  # start
                parent[next] = ['RIGHT', current, 'RIGHT']
            else:
                parent[next] = ['RIGHT', current, parent[current][2]]
                # this I am doing for closest ?

            if grid[current[0]][current[1] + 1] != ".":

                if grid[current[0]][current[1]+1] == target_char:  # 'C' / 'T'
                    # found a path from current to C. Now make a path from curr to C
                    parent[next] = ['RIGHT', current, parent[current][2]]  # current is parent
                    path = get_fwd_path(parent, next, source)

                    # if the target is C then return path_to_C
                    if t_flag is False:

                        # find full_path_from C to T. back path
                        full_path = BFS_labyrinth(grid=grid, c_flag=True, r=r, c=c,
                                                  t_flag=True, source=next, target_char='T')
                        return path, full_path, True

                    # in BFS for finding back path to T from C
                    else:  # if finding path to T from C then simply return the complete path
                        return path

                elif grid[current[0]][current[1] + 1] == '?':
                    if dirxn_ret == "":  # first time
                        if current == source:
                            dirxn_ret = 'RIGHT'
                        else:
                            dirxn_ret = parent[current][2]
                        if not c_flag:  # return from here only when C is not in the grid
                            return dirxn_ret
                else:
                    q.append(next)  # special for T in grid
                    visited[next] = True    

            else:
                q.append(next)
                visited[next] = True  # add to visited: True
        else:
            f1 = True
            if grid[current[0]][current[1] + 1] == '.':
                flag_r = True

        # UP
        next = (current[0] - 1, current[1])
        if current[0] - 1 > -1 and grid[current[0] - 1][current[1]] != '#' and next not in visited:  # UP

            if current == source:  # start
                parent[next] = ['UP', current, 'UP']
            else:
                parent[next] = ['UP', current, parent[current][2]]

            if grid[current[0] - 1][current[1]] != ".":
                if grid[current[0] - 1][current[1]] == target_char:
                    # found a path from current to C. Now make a path from curr to C
                    parent[next] = ['UP', current, parent[current][2]]  # current is parent
                    path = get_fwd_path(parent, next, source)

                    # if the target is C then return path_to_C
                    if t_flag is False:

                        # find full_path_from C to T. back path
                        full_path = BFS_labyrinth(grid=grid, c_flag=True, r=r, c=c,
                                                  t_flag=True, source=next, target_char='T')
                        return path, full_path, True

                    # in BFS for finding back path to T from C
                    else:  # if finding path to T from C then simply return the complete path
                        return path
                    # if the target is C then return path_to_C
                elif grid[current[0] - 1][current[1]] == '?':
                    if dirxn_ret == "":  # first time
                        if current == source:
                            dirxn_ret = 'UP'
                        else:
                            dirxn_ret = parent[current][2]
                        if not c_flag:  # return from here only when C is not in the grid
                            return dirxn_ret
                
                else:
                    q.append(next)  # special for T in grid
                    visited[next] = True    
                    
            else:
                q.append(next)
                visited[next] = True  # add to visited: True
        else:
            f3 = True
            if grid[current[0] - 1][current[1]] == '.':
                flag_u = True

        # DOWN
        next = (current[0] + 1, current[1])
        if current[0] + 1 < r and grid[current[0] + 1][current[1]] != '#' and next not in visited:  # DOWN

            if current == source:  # start
                parent[next] = ['DOWN', current, 'DOWN']
            else:
                parent[next] = ['DOWN', current, parent[current][2]]
                # this I am doing for closest ?

            if grid[current[0] + 1][current[1]] != ".":

                if grid[current[0] + 1][current[1]] == target_char:  # 'C' / 'T'
                    # found a path from current to C. Now make a path from curr to C
                    parent[next] = ['DOWN', current, parent[current][2]]  # current is parent
                    path = get_fwd_path(parent, next, source)

                    # if the target is C then return path_to_C
                    if t_flag is False:

                        # find full_path_from C to T. back path
                        full_path = BFS_labyrinth(grid=grid, c_flag=True, r=r, c=c,
                                                  t_flag=True, source=next, target_char='T')
                        return path, full_path, True

                    # in BFS for finding back path to T from C
                    else:  # if finding path to T from C then simply return the complete path
                        return path

                elif grid[current[0] + 1][current[1]] == '?':
                    if dirxn_ret == "":  # first time
                        if current == source:
                            dirxn_ret = 'DOWN'
                        else:
                            dirxn_ret = parent[current][2]
                        if not c_flag:  # return from here only when C is not in the grid
                            return dirxn_ret
                
                else:
                    q.append(next)  # special for T in grid
                    visited[next] = True    
                    
            # if target; make a path and return the path
            else:
                q.append(next)
                visited[next] = True  # add to visited: True
        else:
            f2 = True
            if grid[current[0] + 1][current[1]] == '.':
                flag_d = True

    return dirxn_ret, None, False       # return None as a full_path and next_dirxn to closest ?


def get_fwd_path(parent, v, source):

    path = []
    while v != source:
        path.append(parent[v][0])
        v = parent[v][1]        # {v: [dir, parent]}
    print(path, file=sys.stderr)
    return path


T = False
path_to_C_from_current = None
full_path_to_T_from_C = None
prev_dirxn = None
opp_path = {'UP': 'DOWN', 'DOWN': 'UP', 'RIGHT': 'LEFT', 'LEFT': 'RIGHT'}
# game loop
while True:

    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]  # start point
    grid = []
    print(kr, kc, file=sys.stderr)

    if T is False:
        T = (kr, kc)        # get T

    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        grid.append(row)
        print(row, file=sys.stderr)
        if 'C' in row:
            print("YES", file=sys.stderr)
            c_flag = True

    print(grid[kr][kc], file=sys.stderr)
    if grid[kr][kc] == 'C':     # start traversing back to T. Run BFS from C to T
        back_flag = True

    if back_flag:
        bk_dirxn = full_path_to_T_from_C.pop()  # Got this complete path from C to T when I reached from current to C
        print(bk_dirxn)

    else:

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)
        if c_flag:  # c is in grid. Look for C specifically
            # try to find path from current to C
            if not comp_flag:  # if BFS path to C is not found yet
                path_to_C_from_current, full_path_to_T_from_C, comp_flag = \
                    BFS_labyrinth(grid=grid, c_flag=c_flag, r=r, c=c,
                                  t_flag=False, source=(kr, kc), target_char='C')
            print(path_to_C_from_current, file=sys.stderr)
            if comp_flag:  # found C and path to it. Print the next dirxn to reach C
                print(path_to_C_from_current.pop())

            else:  # could not reach C directly. Look for first '?'
                # if complete path not found then print the current dirxn to nearest ?

                # path_to_C from Current will be just a string, here
                print(path_to_C_from_current)  # print the first dirxn. It comes by default from the BFS function

        else:  # C is not grid. c_flag is False
            # it will return just a string if c_flag is False
            dirxn = BFS_labyrinth(grid=grid, c_flag=c_flag, r=r, c=c,
                                  t_flag=False, source=(kr, kc), target_char='C')
            if dirxn == ('', None, False):
                print(prev_dirxn)
            else:
                print(dirxn)
                prev_dirxn = opp_path[dirxn]


        # Kirk's next move (UP DOWN LEFT or RIGHT).
