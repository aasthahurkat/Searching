import copy
from heapq import heappop, heappush

adj_list = {}
def createAdjList(filename):
    with open(filename,'r') as file:
        for line in file:
            from_city = str.split(line)[0]
            to_city = str.split(line)[1]
            length = int(str.split(line)[2])
            speed_limit = str.split(line)[3]
            highway_name = str.split(line)[4]
            if from_city in adj_list.keys():
                #old = adj_list[from_city][0]
                adj_list[from_city][0].append((to_city,length,speed_limit,highway_name))
            else:
                adj_list[from_city] = ([], 0, 0, 0)
                adj_list[from_city][0].append((to_city,length,speed_limit,highway_name))

            if to_city in adj_list.keys():
                #old = adj_list[to_city][0]
                adj_list[to_city][0].append((from_city,length,speed_limit,highway_name))
            else:
                adj_list[to_city] = ([], 0, 0, 0)
                adj_list[to_city][0].append((from_city,length,speed_limit,highway_name))
 
def successors(currentNode):

    return adj_list[currentNode][0] #Returning only the neighbour list
    #return [(copy.deepcopy(possible_list), neighbour, source, destination, travelled_cost ) for neighbour in adj_list[source]]

def solve(source, destination, cost_function):
    solution = []
    fringe = []
    visited = {(source)}
    #fringe = [ (visited, source, destination, 0) ] #Forth paramter is the travelled cost
    heappush(fringe, (adj_list[source][1], [], source, adj_list[source]))
    while len(fringe) > 0:
        (cost_until_now, routeList, currentNode, state) = heappop(fringe)
        for (succ, distance, SpeedLimit, highwayName) in successors(currentNode):
            if succ == destination:
                #time = 0
                #gas = 0
                return (cost_until_now + distance, routeList)
            if (succ not in visited):# and (succ not in fringe):
                visited.add(succ)
                cost = distance + cost_until_now #+ #Call heuristic
                routeList.append(succ)
                heappush(fringe, (cost, copy.deepcopy(routeList), succ, adj_list[succ]))
                routeList.pop()


def calculateHeuristic(cost_function, args):
    if(cost_function == "segments"):
        return True
    elif(cost_function == "distance"):
        succ = args[0]
        distance = args[1]
        SpeedLimit = args[2]
        highway = args[3]
        return distance
    elif(cost_function == "time"):
        return True
    elif(cost_function == "mpg"):
        return True
    else:
        print("Should not have happened!")

if __name__ == "__main__":

    createAdjList("/u/rrokde/bagrawal-aahurkat-rrokde-a1/part2/road-segments.txt")

       
#    print("adjancency list format is:  ")
#    for key in adj_list:
#        print("no of neighbours: ", len(adj_list[key]), " for city: ", key)
#        print(key, '->', adj_list[key])
#        break

    source = "Bloomington,_Indiana"
    destination = "Detroit,_Michigan"
    result = solve(source, destination, "distance")
    print("Total distance from ", source, " to ",  destination, " is " , result[0])
    print("The route to take is ", source, " ->", end=" ")
    for point in result[1]:
        print(point, " ->", end=" ")
    print(destination)
