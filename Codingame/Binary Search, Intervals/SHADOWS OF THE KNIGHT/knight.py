"""
The goal of this puzzle is to guess the coordinate of a bomb (line and column of a 
2 dimensional array). You will have to make a guess at each 
step of the puzzle and adjust it from given feedbacks. 
Of course, you have a limited number of guess.

External resources Multidimensional arrayBinary search2D Binary Search explained by Gaurav Sen 

https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1

"""

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
l = 0
t = 0
r = w-1
d = h-1


def two_d_binary_search(bomb_dir, l, r, t, d, x0, y0):
    if bomb_dir == "U":
        l, r = x0, x0
        d = y0-1
        mid = [x0, (t+d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "D":
        l, r = x0, x0
        t = y0 + 1
        mid = [x0, (t + d) // 2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "L":
        t, d = y0, y0
        r = x0 - 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "R":
        t, d = y0, y0
        l = x0 + 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "UR":
        l = x0 + 1
        d = y0 - 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "UL":
        r = x0 - 1
        d = y0 - 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "DR":
        l = x0 + 1
        t = y0 + 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

    elif bomb_dir == "DL":
        r = x0 - 1
        t = y0 + 1
        mid = [(l+r)//2, (t + d)//2]
        return mid, l, r, t, d, mid[0], mid[1]

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    mid, l, r, t, d, x0, y0 = two_d_binary_search(bomb_dir, l, r, t, d, x0, y0)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.
    print("{0} {1}".format(mid[0], mid[1]))

