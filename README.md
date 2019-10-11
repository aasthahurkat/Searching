Part 1:
Initial State -
The state provided as an input

Goal State -
A grid where the numbers are arranged sequentially with 0(blank tile) at the end.

State Space -
A list of all the configurations the state can take up.

Successors -
The configurations that can follow a current state with the valid possible moves. It would vary depending on the variations - original, circular and luddy.

Cost Function -
Initially, the code worked on Manhattan distance as a cost function only. But, this cost function did not prove to be very effective for luddy so we used the number of mispaced tiles and that worked far better for luddy but was slower on original and circular variations. So, we decided to use Manhattan distance for the latter versions.

Search Algorithm -
We have implemented the search algorithm #3 discussed in the class to solve this problem.
We need to find out the solution to a 15 puzzle problem with slightly modified rules.
The first case, however works on the typical rules of the game. Out first step was to check whether the puzzle is solvable or not. The function isSolvable() in the program is for the same.
For the second case, we introduced the extra moves which are allowed for the circular moves. If the circular moves are allowed, all the blocks in the puzzle get 4 possible moves - unlike in the original one.
The third case is similar to how a knight moves on a chess board. We defined the moves of the puzzle

Potential Issues -
The Luddy version does not always give the solution within the time limits.

Code Fix -
A better solution would be to use heuristic to be a combination of Manhattan distance and linear inversions for Luddy. 


Part 2 :
Initial State -
Source city given as input

Goal State -
Destination city given as output

State Space -
A list of all the cities and the highway junctions. The state space has been treated as a graph with individual states representing the nodes of the graph.

Successors -
A set of the nodes that are connected to the current state with a segment given in 'road-segments.txt'

Cost Function -
The Euclidean distance between any two states. This has been calculated as the Haversine distance.

Search Algorithm -
A* search algorithm has been used to solve this problem. The graph is represented using an adjacency matrix and dictionary is used to keep track of neighbours and latitude and longitude of each state. The neighbours in the value of each key is in turn, a tuple of successor state and all relevant features like distance and speed limit.

Potential Issues -
The code does not always provide the most optimal solution for longer routes. We have identified two possible reasons -
1. To deal with inconsistencies in the data set where latitude and longitude is missing the cost function returns 0 value.
2. The code does not correctly update the cost of a state if it finds a shorter path rather than in the existing fringe as the 'visited' is implemented as a set.

Code fix-
The following steps address each potential issue-
1. Get a better estimate of cost function in case of absence of latitude and longitude using the Successors rather than returning zero.
2. Implement each item in the fringe as a dictionary so that it's easier to update the cost function whenever a shorter path is discovered. 
