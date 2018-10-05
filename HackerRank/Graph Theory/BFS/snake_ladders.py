"""
https://www.hackerrank.com/challenges/the-quickest-way-up/problem
"""

import math
import os
import random
import re
import sys
from collections import defaultdict
from queue import deque

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    # Initialize the graph
    adj_dict = defaultdict(list)
    level = defaultdict(None)
    visited = defaultdict()
    snake_list = set()
    ladder_list = set()

    # add ladders
    for ladder in ladders:
        adj_dict[ladder[0]].append(ladder[1])     # go up
        ladder_list.add(ladder[0])   # accommodate the ladder level.
        # straight up to next vertex w/o incrementing the level in BFS

    # add snakes
    for snake in snakes:
        adj_dict[snake[0]].append(snake[1])       # go down
        snake_list.add(snake[0])    # accommodate the snake level 0

    # make other graph
    for i in range(1, 101): # 100 nodes total
        if i not in adj_dict:       # only one possible location from snake/ladder
            for j in range(1, 7):
                if i + j > 100:
                    break
                adj_dict[i].append(i+j)     # add next 6 vertices to the current node
        visited[i] = False

    # BFS source = 1
    visited[1] = True
    level[1] = 0

    # BFS
    q = deque()
    q.append(1)
    """
    Deque is preferred over list in the cases where we need quicker append and 
    pop operations from both the ends of container, as deque provides an O(1) time complexity 
    for append and pop """

    while len(q) != 0:
        u = q.popleft()     # integer

        for v in adj_dict[u]:
            #
            if v == 100 and u in ladder_list:  # found the goal
                return level[u] # direct reach
            elif v == 100:
                return level[u] + 1

            if visited[v] is False:
                # if v == 100:  # found the goal
                #     return level[u] + 1
                visited[v] = True
                if u in snake_list or u in ladder_list:
                    level[v] = level[u]
                else:
                    level[v] = level[u] + 1
                q.append(v)

    return -1 # did not find 100 in BFS


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
    