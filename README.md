#Part 1: The Luddy puzzle
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

-----------------------------------------

#Part 2 : Road Trip!
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

-----------------------------------------
#Part 3 - Choosing a team (Robot selection problem)

1. State space:- It consists of all combinations of all the person's data. The starts with one person in each list and then goes
on to add all the other remaining ones along with a conditional check to verify if the selection is within the budget.

   Successor function:- It selects all the person only one at a time which do not already exist in the current selection.
   
   Goal state:- To arrive at the goal state, we are first calculating all the possible goal states, store them in a list, sort
   them in a descending order and then choose the first element as our goal state.
   
   Heuristic function:- This is not implemented, and even if it were used, we would still need to explore all possibilities to
   get the optimal solution. So there was no point in using a heuristic function.
   
2. Brief description of how our search algorithm works:-
    Look for all the combinations of persons, add their skills and rates, and then choose a selection with the highest skill.
   
   
3. In my first try, I wrote my program to maximize the total skill of robots. So my first code commit
	selected robots based on higher skill to rate ratios. As it turned out this approach was wrong because we could not select
	a robot more than once. 

	Then I did some initial research on the internet, this is problem which comes in he knowen category of problems viz the Knapsack problem.
	Part 3 was a specific type of Knapsack problem called as 0/1 Knapsack problem. So in order to solve this, I could've
	used Dynamic programming to arrive at a solution. But the Dynamic programming needs the bounds in the form of integers.
	Since in our case, the allowed weights(rates) we used were rational numbers, Dynamic programming approach couldn't have
	been used. Although we could multiply the rational numbers with 10^n to make turn the decimal numbers into integers,
	make our program work and then divide the answer by 10^n again. But for long decimals, this approach could fail and would
	not ensure optimality.

	So I posted a question on piazza to get some kind of direction to appraoch this problem. So I found out that branch and bound and A* could
	be used to solve 0/1 knapsack problem. So I implemented the A* algorithm sans the visited data structure. This algorithm tries
	all the possible combinations to get the best result.
-----------------------------------------
