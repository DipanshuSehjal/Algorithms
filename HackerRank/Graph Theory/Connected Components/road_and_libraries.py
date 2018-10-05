#!/bin/python3

"""
https://www.hackerrank.com/challenges/torque-and-development/problem
"""

import math
import os
import random
import re
import sys
from collections import defaultdict

tree_edge_in_comp = 0
color = {}
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n*c_lib

    vertices = defaultdict(list)
    
    for pair in cities:
        vertices[pair[0]].append(pair[1])
        vertices[pair[1]].append(pair[0])

    for u in vertices:
        color[u] = "white"
    conn_comp = 0
    for u in vertices:
        if color[u] == "white":

            conn_comp += 1
            DFS_visit(vertices, u)

    return (conn_comp + n - len(vertices.keys()))*c_lib + tree_edge_in_comp*c_road

def DFS_visit(vertices, u):
    color[u] = "black"
    for v in vertices[u]:
        if color[v] == "white":
            global tree_edge_in_comp
            tree_edge_in_comp += 1
            DFS_visit(vertices, v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        tree_edge_in_comp = 0
        color = {}
        fptr.write(str(result) + '\n')

    fptr.close()
