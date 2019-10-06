import copy
import sys
from heapq import heappop, heappush

adj_list = {}
def createAdjList(filename):
    with open(filename,'r') as file:
        for line in file:
            from_city = str.split(line)[0]
            to_city = str.split(line)[1]
            length = int(str.split(line)[2])
            speed_limit = float(str.split(line)[3])
            highway_name = str.split(line)[4]
            if from_city in adj_list.keys():
                #old = adj_list[from_city][0]
                adj_list[from_city][0].append((to_city,length,speed_limit,highway_name))
            else:
                #Elements:- (List of neighbors, dummy travelled cost, placeholder for latitude, placeholder for longitude).
                adj_list[from_city] = ([], 0, 0, 0)
                adj_list[from_city][0].append((to_city,length,speed_limit,highway_name))

            if to_city in adj_list.keys():
                #old = adj_list[to_city][0]
                adj_list[to_city][0].append((from_city,length,speed_limit,highway_name))
            else:
                adj_list[to_city] = ([], 0, 0, 0)
                adj_list[to_city][0].append((from_city,length,speed_limit,highway_name))

def readGPScoordinates(filename):
    with open(filename,'r') as file:
        for line in file:
            cityName = str.split(line)[0]
            latitude = float(str.split(line)[1])
            longitude = float(str.split(line)[2])
            if cityName in adj_list.keys():
                nodeObject = adj_list[cityName]
                adj_list[cityName] = (nodeObject[0], nodeObject[1], latitude, longitude)

def successors(currentNode):

    return adj_list[currentNode][0] #Returning only the neighbour list

def solve(source, destination, cost_function):

    if(cost_function == "segments"):
        #solution = []
        fringe = []
        visited = {(source)}
        heappush(fringe, (0, adj_list[source][1], [], source, adj_list[source], 0, 0))
        while len(fringe) > 0:
            (segments_until_now, cost_until_now, routeList, currentNode, state, time_taken, gas_used) = heappop(fringe)
            for (succ, distance, SpeedLimit, highwayName) in successors(currentNode):#highwayName is redundant here
                if succ == destination:
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
                if (succ not in visited):# and (succ not in fringe):
                    visited.add(succ)
                    cost = distance + cost_until_now #+ #Call heuristic
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    routeList.append(succ)#Add current node to our list
                    if((segments_until_now+1) != len(routeList)):
                        print("Not Possible!!!!!!!")
                    heappush(fringe, (len(routeList), cost_until_now + distance, copy.deepcopy(routeList), succ, adj_list[succ], time_taken+hours, gas_used+gas))
                    routeList.pop()#Prepare the routelist for next node, i.e. ignore the current node
    elif(cost_function == "distance"):
        #solution = []
        fringe = []
        visited = {(source)}
        heappush(fringe, (adj_list[source][1], [], source, adj_list[source], 0, 0))
        while len(fringe) > 0:
            (cost_until_now, routeList, currentNode, state, time_taken, gas_used) = heappop(fringe)
            for (succ, distance, SpeedLimit, highwayName) in successors(currentNode):#Speedlimit and highwayName are redundant here
                if succ == destination:
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
                if (succ not in visited):# and (succ not in fringe):
                    visited.add(succ)
                    cost = distance + cost_until_now #+ #Call heuristic
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    routeList.append(succ)#Add current node to our list
                    heappush(fringe, (cost, copy.deepcopy(routeList), succ, adj_list[succ], time_taken+hours, gas_used+gas))
                    routeList.pop()#Prepare the routelist for next node, i.e. ignore the current node
    elif(cost_function == "time"):
        #solution = []
        fringe = []
        visited = {(source)}
        heappush(fringe, (0, adj_list[source][1], [], source, adj_list[source], 0, 0))
        while len(fringe) > 0:
            (time_taken, cost_until_now, routeList, currentNode, state, time_taken, gas_used) = heappop(fringe)
            for (succ, distance, SpeedLimit, highwayName) in successors(currentNode):#highwayName is redundant here
                if succ == destination:
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
                if (succ not in visited):# and (succ not in fringe):
                    visited.add(succ)
                    cost = distance + cost_until_now #+ #Call heuristic
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    routeList.append(succ)#Add current node to our list
                    heappush(fringe, (time_taken+hours, cost_until_now + distance, copy.deepcopy(routeList), succ, adj_list[succ], time_taken+hours, gas_used+gas))
                    routeList.pop()#Prepare the routelist for next node, i.e. ignore the current node
    elif(cost_function == "mpg"):
        #solution = []
        fringe = []
        visited = {(source)}
        heappush(fringe, (0, adj_list[source][1], [], source, adj_list[source], 0, 0))
        while len(fringe) > 0:
            (gas_used, cost_until_now, routeList, currentNode, state, time_taken, gas_used) = heappop(fringe)
            for (succ, distance, SpeedLimit, highwayName) in successors(currentNode):#highwayName is redundant here
                if succ == destination:
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
                if (succ not in visited):# and (succ not in fringe):
                    visited.add(succ)
                    cost = distance + cost_until_now #+ #Call heuristic
                    hours = (distance/SpeedLimit)
                    v = SpeedLimit
                    gas = 400 * (v/150) * ((1 - (v/150))**4)
                    routeList.append(succ)#Add current node to our list
                    heappush(fringe, (gas_used+gas, cost_until_now + distance, copy.deepcopy(routeList), succ, adj_list[succ], time_taken+hours, gas_used+gas))
                    routeList.pop()#Prepare the routelist for next node, i.e. ignore the current node
    else:
        print("Should not have happened!")

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

    #Check if all the arguments are valid
    if(len(sys.argv) != 4):
        raise(Exception("Error: expected 2 arguments"))

    cost_function = sys.argv[3]
    if(cost_function == "segments"):
        pass
    elif(cost_function == "distance"):
        pass
    elif(cost_function == "time"):
        pass
    elif(cost_function == "mpg"):
        pass
    else:
        print("Please enter a valid cost-function")
        sys.exit()

    #Program starts here
    createAdjList('./road-segments.txt')

    readGPScoordinates('./city-gps.txt')

    source = sys.argv[1]#e.g.  Bloomington,_Indiana
    destination = sys.argv[2]#e.g.  Detroit,_Michigan

#    print("adjancency list format is:  ")
#    for key in adj_list.keys():
#        print("no of neighbours: ", len(adj_list[key]), " for city: ", key)
#        print(key, '->', adj_list[key])
#        break

    result = solve(source, destination, cost_function)

    totalsegments = len(result[1])+1  #Last segment is counted here as +1
    totalmiles = result[0]
    totalhours = result[2]
    totalgasgallons = result[3]
    print("%d %d %.4f %.4f %s" % ((totalsegments, totalmiles, totalhours, totalgasgallons, source)), end=" ")
    for point in result[1]:
        print(point, end=" ")
    print(destination)