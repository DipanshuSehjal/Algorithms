"""

What will I learn?
Conditions

In this puzzle, you learn to position an object on a one-dimensional grid.
External resources Conditions


Statement:
Guide the clones towards the exit of the maze, stop when you’re going away from the exit, continue if you are going the right way. You are given the position and direction of your clones.

https://www.codingame.com/training/medium/don't-panic-episode-1

"""


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

elevator_floor_list = []
elevator_pos_list = []
# add the final positions first
elevator_pos_list.append(exit_pos)
elevator_floor_list.append(exit_floor)

inp = {}
    
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    inp[elevator_floor] = elevator_pos

inp[exit_floor] = exit_pos
inp[exit_floor+1] = 0 # stop condition

    
flag = 0


mark_1 = False
# game loop

i = 0 # last elevator in list(first elevator in the game). added the exit pos to the start

start = 0
right = 0
close = 0

while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    if nb_elevators == 0:
        if clone_pos > exit_pos and not mark_1:
            print("BLOCK")
            mark_1 = True
        else:
            print("WAIT")
    else:
        current_elev_floor = i
        curr = inp[i]
        nxt = inp[i+1]
    
        if clone_pos > curr and clone_floor == current_elev_floor and close == 0:
            print("BLOCK")
            right = 1
            close = 1
        else:
            start = 1
        
        if right == 0 and start == 1:
            if clone_floor == (current_elev_floor+1):
                i+=1
            if clone_floor == (current_elev_floor+1) and clone_pos == curr and nxt-curr > 0 and flag == 1:
                print("BLOCK")
                flag = 0 
            elif clone_floor == (current_elev_floor+1) and clone_pos == curr and nxt-curr < 0 and flag == 0:
                print("BLOCK")
                flag = 1
            else:
                print("WAIT")
                
        elif right == 1 and start == 1: # right
            if clone_floor == (current_elev_floor+1):
                i+=1
            
            if clone_floor == (current_elev_floor+1) and clone_pos == curr and nxt-curr > 0 and flag == 0:
                print("BLOCK")
                flag = 1
            # elif clone_floor == current_elev_floor and clone_pos < elevator_pos:
            #     print("WAIT")
            elif clone_floor == (current_elev_floor+1) and clone_pos == curr and nxt-curr < 0 and flag == 1:
                print("BLOCK")
                flag = 0
            else:
                print("WAIT")
        
    start = 1
    close = 1