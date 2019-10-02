#!/usr/local/bin/python3
# solve_luddy.py : Sliding tile puzzle solver
#
# Code by: [PLEASE PUT YOUR NAMES AND USER IDS HERE]
#
# Based on skeleton code by D. Crandall, September 2019
#
from queue import PriorityQueue
import sys
from heapq import heappop,heappush

#MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }

MOVES = {"E": (1, 2), "G": (-1, 2), "B": (2, -1),"D": (-2, -1),"H": (-1, -2),"F": (1, -2),"C": (-2, 1),"A": (2, 1)}


def rowcol2ind(row, col):
    return row*4 + col

def ind2rowcol(ind):
    return (int(ind/4), ind % 4)

def valid_index(row, col):
    return 0 <= row <= 3 and 0 <= col <= 3

def swap_ind(list, ind1, ind2):
    return list[0:ind1] + (list[ind2],) + list[ind1+1:ind2] + (list[ind1],) + list[ind2+1:]

def swap_tiles(state, row1, col1, row2, col2):
    return swap_ind(state, *(sorted((rowcol2ind(row1,col1), rowcol2ind(row2,col2)))))

def printable_board(row):
    return [ '%3d %3d %3d %3d'  % (row[j:(j+4)]) for j in range(0, 16, 4) ]

# return a list of possible successor states
def successors(state):
    #print("exploring state:",state)
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    result = []
    for (c, (i, j)) in MOVES.items():
        if valid_index(empty_row+i, empty_col+j):
            temp = swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j)
            cost = calculate_heuristic(temp)
            result.append((cost, c, temp))
    return result
    #return [ (temp, c, calculate_heuristic(temp)) \
             #for (c, (i, j)) in MOVES.items() if valid_index(empty_row+i, empty_col+j) ]

# check if we've reached the goal
def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) and state[-1]==0


def solve2(initial_board):
    fringe =[]
    visited =set()
    heappush(fringe, ("","",initial_board))
    while len(fringe) > 0:
        (cost, route_so_far, state) = heappop(fringe)
        visited.add(state)
        print("popped state:\n" +"\n".join(printable_board(tuple(state))))
        for (cost, move, succ) in successors( state ):
            if is_goal(succ):
                return( route_so_far + move )
            if succ not in visited:
                #if succ in fringe:
                print("succ state:\n" +"\n".join(printable_board(tuple(succ))))
                print("total cost of succ", len(route_so_far) + cost)
                print("route so far: ", route_so_far)
                print("actual cost: ", cost)
                print("len of route so far: ", len(route_so_far))
                heappush(fringe,(len(route_so_far) + cost, route_so_far + move, succ)) 
    return False

def calculate_heuristic(state):
    cost = 0
    for i in range(len(state)):
        num = state[i]
        #if num != 0:
        if num != i+1 and num != 0:
            #print("i is: ", i)
            #print("num is: ", num)
            correct_row, correct_col = ind2rowcol(num - 1)
           # print("correct row,col:" , correct_row, "  ", correct_col)
            curr_row, curr_col = ind2rowcol(i)
            #print("curr_row,curr-col:" , curr_row,"  " , curr_col)
            #print("individual cost: ", abs(curr_row - correct_row) + abs(curr_col - correct_col))
            cost += abs(curr_row - correct_row) + abs(curr_col - correct_col)
        elif num == 0:
            curr_row, curr_col = ind2rowcol(i)
            cost += abs(3 - curr_row) + abs(3 - curr_col)
            #print("i is: ", i)
            #print("num is: ", num)
            #print("correct row,col:" , correct_row, "  ", correct_col)
            #print("curr_row,curr-col:" , curr_row,"  " , curr_col)
            #print("individual cost: ", abs(curr_row - correct_row) + abs(curr_col - correct_col))
    #print("value returned: ", cost )
    return cost

# test cases
if __name__ == "__main__":
   # if(len(sys.argv) != 3):
    #    raise(Exception("Error: expected 2 arguments"))
    start_state = []
    with open("C:\\Users\\HP\\Downloads\\board4test.txt", 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    #if(sys.argv[2] != "original"):
     #   raise(Exception("Error: only 'original' puzzle currently supported -- you need to implement the other two!"))

    if len(start_state) != 16:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve2(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)