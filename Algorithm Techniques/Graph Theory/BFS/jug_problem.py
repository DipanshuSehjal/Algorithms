from queue import deque
from math import gcd

"""

Jug problem is solvable iff gcd(a,b) divides target. Diophantine equation
with Extended Euclidean algorithm.

Make states on the fly!

The two water jug puzzle solved wth BFS:
We run breadth first search on the states and these states will be created
after applying allowed operations and we also use a dictionary to keep a record of visited states. 
Note that: This solution can also be achieved using depth first search
"""


class State:
    def __init__(self, j1=None, j2=None):
        self.j1 = j1
        self.j2 = j2


def jug_BFS(jug1, jug2, target):
    """
    First start with the initial state
    :return:
    """
    if target % gcd(jug1, jug2) != 0:
        return "Insolvable"

    path = []
    is_visited = {}
    q = deque()
    init_state = State(j1=0, j2=0)
    q.append(init_state)     # initial state of 0,0
    # is_visited has [boolean, parent]
    is_visited[(init_state.j1, init_state.j2)] = [None, None]       # not visited yet

    while len(q) != 0:
        curr = q.popleft()      # get the current state
        # FOUND THE SOLUTION
        # if we reach the solution state
        # BE SMART to detect the solution beforehand to save time
        if curr.j1 == target or curr.j2 == target:
            final_state = (curr.j1, curr.j2)
            if curr.j1 == target:
                if curr.j2 != 0:  # add one more step where we empty the second jug
                    is_visited[(curr.j1, 0)] = [True, (curr.j1, curr.j2)]
                    final_state = (curr.j1, 0)
                    # else jug2 is already empty

            else:  # second jug has target
                if curr.j1 != 0:
                    is_visited[(0, curr.j2)] = [True, (curr.j1, curr.j2)]
                    final_state = (0, curr.j2)
                    # empty the first jug and add to path

            # print the solution
            print(("count of steps\n(Don't count (0,0)): ", print_path(is_visited, final_state)))
            break
        # 4 cases for every instance

        # Case 1: fill jug 1.
        if (jug1, curr.j2) not in is_visited:   # check if the new state is not already visited
            q.append(State(jug1, curr.j2))       # add new state
            is_visited[(jug1, curr.j2)] = [True, (curr.j1, curr.j2)]    # add parent

        # Case 2: fill jug 2
        if (curr.j1, jug2) not in is_visited:   # check if the new state is not already visited
            q.append(State(curr.j1, jug2))       # add new state
            is_visited[(curr.j1, jug2)] = [True, (curr.j1, curr.j2)]

        # Case 3: pour j1 to j2
        diff = min(curr.j1, jug2 - curr.j2)
        if (curr.j1 - diff, diff + curr.j2) not in is_visited:
            q.append(State(curr.j1 - diff, diff + curr.j2))
            is_visited[(curr.j1 - diff, diff + curr.j2)] = [True, (curr.j1, curr.j2)]

        # Case 4: pour j2 to j1
        diff = min(jug1 - curr.j1, curr.j2)
        if (curr.j1 + diff, curr.j2 - diff) not in is_visited:
            q.append(State(curr.j1 + diff, curr.j2 - diff))
            is_visited[(curr.j1 + diff, curr.j2 - diff)] = [True, (curr.j1, curr.j2)]


def print_path(parent, v):
    """

    :param parent: is_visited[child] = [boolean, parent]
    :param v: child
    :return: count of steps and (print path)
    """
    # simple recursion
    if parent[v][1]:    # parent of v
       cnt = 1 + print_path(parent, parent[v][1])        # go to parent
    print(v)
    if parent[v][1] is None:
        cnt = 0
    return cnt


jug1 = 5
jug2 = 3
target = 1
(jug_BFS(jug1, jug2, target))


