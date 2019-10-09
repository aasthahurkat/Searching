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
import math

#Following code given in the below function is taken from https://stackoverflow.com/questions/34570344/check-if-15-puzzle-is-solvable
def isSolvable(puzzle):
    gridWidth = int(math.sqrt(len(puzzle)))
    parity = 0
    currentrow = 0
    blankRow = 0
    for i in range(len(puzzle)):
        if ((i % (gridWidth)) == 0): #advance to next row
            #print(" #advance to next row", currentrow)
            currentrow += 1
        if (puzzle[i] == 0):#the blank tile
            blankRow = currentrow #save the row on which encountered
            continue
        for j in range(i+1, len(puzzle)):
            if (puzzle[i] > puzzle[j] and puzzle[j] != 0):
                parity += +1
    if (gridWidth % 2 == 0): #even grid
        if (((blankRow) % 2) == 0): #blank on odd row; counting from bottom
            return ((parity % 2) == 0)
        else:
            return ((parity % 2) != 0) #blank on even row; counting from bottom
    else: #{ // odd grid
        return ((parity % 2) == 0)

MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }

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
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    result = []
    for (c, (i, j)) in MOVES.items():
        if valid_index(empty_row+i, empty_col+j):
            temp = swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j)
            cost = calculate_heuristic(temp)
            result.append((cost, c, temp))
    return result

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
        for (cost, move, succ) in successors( state ):
            if is_goal(succ):
                return( route_so_far + move )
            if succ not in visited:
                heappush(fringe,(len(route_so_far) + cost, route_so_far + move, succ)) 
    return False

def calculate_heuristic(state):
    cost = 0
    for i in range(len(state)):
        num = state[i]
        if num != i+1 and num != 0:
            correct_row, correct_col = ind2rowcol(num - 1)
            curr_row, curr_col = ind2rowcol(i)
            cost += abs(curr_row - correct_row) + abs(curr_col - correct_col)
        elif num == 0:
            curr_row, curr_col = ind2rowcol(i)
            cost += abs(3 - curr_row) + abs(3 - curr_col)
    return cost

# test cases
if __name__ == "__main__":
    #if(len(sys.argv) != 3):
      #  raise(Exception("Error: expected 2 arguments"))
    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]
    
    if isSolvable(start_state)==True:

        if(sys.argv[2] == "original"):
            MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }
            
            if len(start_state) != 16:
                raise(Exception("Error: couldn't parse start state file"))
        
            print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
        
            print("Solving...")
            route = solve2(tuple(start_state))
            
            print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)
            
            
        elif(sys.argv[2] == "circular"):
            MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0), "M": (0, -3), "N": (0, +3), "O": (-3, 0), "P": (+3, 0)}
            if len(start_state) != 16:
                raise(Exception("Error: couldn't parse start state file"))

            print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

            print("Solving...")
            route = solve2(tuple(start_state))
        
            print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)
            
        elif(sys.argv[2] == "luddy"):
            MOVES = {"E": (1, 2), "G": (-1, 2), "B": (2, -1),"D": (-2, -1),"H": (-1, -2),"F": (1, -2),"C": (-2, 1),"A": (2, 1)}
            if len(start_state) != 16:
                raise(Exception("Error: couldn't parse start state file"))

            print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

            print("Solving...")
            route = solve2(tuple(start_state))
            
            print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)
    else:
        print("Inf")
