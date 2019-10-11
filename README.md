Problem 1

We need to find out the solution to a 15 puzzle problem with slightly modified rules.
The first case, however works on the typical rules of the game. Out first step was to check whether the puzzle is solvable or not. The function isSolvable() in the program is for the same.
For the second case, we introduced the extra moves which are allowed for the circular moves. If the circular moves are allowed, all the blocks in the puzzle get 4 possible moves - unlike in the original one.
The third case is similar to how a knight moves on a chess board. We defined the moves of the puzzle

Part2 :
Initial State -
Source city given as input

Goal State -
Destination city given as output

State Space -
A list of all the cities and the highway junctions. The state space has been treated as a graph with individual states representing the nodes of the graph.
Successors -
A set of the nodes that are connected to the current state with a segment given in 'road-segments.txt'

Cost Function -
The Euclidean distance between any two states. This has been calculated as the Haversine distance.(Formula taken from https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude)

Potential Issues -
The code does not always provide the most optimal solution for longer routes. We have identified two possible reasons -
1. To deal with inconsistencies in the data set where latitude and longitude is missing the cost function returns 0 value.
2. The code does not correctly update the cost of a state if it finds a shorter path rather than in the existing fringe as the 'visited' is implemented as a set.

Code fix-
The following steps address each potential issue-
1. Get a better estimate of cost function in case of absence of latitude and longitude using the Successors rather than returning zero.
2. Implement each item in the fringe as a dictionary so that it's easier to update the cost function whenever a shorter path is discovered. 
