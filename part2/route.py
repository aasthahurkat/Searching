#!/usr/local/bin/python3

import copy
import sys
from heapq import heappop, heappush
from math import cos, asin, sqrt

adj_list = {}

def add_neighbour(from_city,to_city,length,speed_limit):
    if from_city in adj_list.keys():
        adj_list[from_city][0].append((to_city,length,speed_limit))
    else:
        #Elements:- (List of neighbors, dummy travelled cost, placeholder for latitude, placeholder for longitude).
        adj_list[from_city] = ([], 0, 0, 0)
        adj_list[from_city][0].append((to_city,length,speed_limit))

def createAdjList(filename):
    with open(filename,'r') as file:
        for line in file:
            add_neighbour(str.split(line)[0],str.split(line)[1],int(str.split(line)[2]),float(str.split(line)[3]))
            add_neighbour(str.split(line)[1],str.split(line)[0],int(str.split(line)[2]),float(str.split(line)[3]))

def readGPScoordinates(filename):
    with open(filename,'r') as file:
        for line in file:
            cityName = str.split(line)[0]
            latitude = float(str.split(line)[1])
            longitude = float(str.split(line)[2])
            if cityName in adj_list.keys():
                nodeObject = adj_list[cityName]
                adj_list[cityName] = (nodeObject[0], nodeObject[1], latitude, longitude)

def cal_distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

def cal_heuristic(current,destination):
    if adj_list[current][1] == 0 or adj_list[current][2] == 0:
        return 0
    else:
        return cal_distance(adj_list[current][1],adj_list[current][2],adj_list[destination][1],adj_list[destination][2])

def successors(currentNode):
    return adj_list[currentNode][0]                          #Returning only the neighbour list

def solve_segments(source,destination):
    fringe = []
    visited = {(source)}
    heappush(fringe, (0, adj_list[source][1], [], source, 0, 0))
    while len(fringe) > 0:
        (segments_until_now, cost_until_now, routeList, currentNode, time_taken, gas_used) = heappop(fringe)
        for (succ, distance, SpeedLimit) in successors(currentNode):
            hours = (distance/SpeedLimit)
            gas = (400 * (SpeedLimit/150) * ((1 - (SpeedLimit/150))**4))/distance
            if succ == destination:
                return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
            if (succ not in visited):
                visited.add(succ)      
                routeList.append(succ)                               #Add current node to our list
                heappush(fringe, (len(routeList), cost_until_now + distance, copy.deepcopy(routeList), succ, time_taken+hours, gas_used+gas))
                routeList.pop()                                      #Prepare the routelist for next node, i.e. ignore the current node

def solve_distance(source,destination):
    fringe = []
    visited = {(source)}
    heappush(fringe, (cal_heuristic(source,destination) , adj_list[source][1], [], source, 0, 0))
    while len(fringe) > 0:
        (heuristic_val, cost_until_now, routeList, currentNode, time_taken, gas_used) = heappop(fringe)
        for (succ, distance, SpeedLimit) in successors(currentNode):
            hours = (distance/SpeedLimit)
            gas = (400 * (SpeedLimit/150) * ((1 - (SpeedLimit/150))**4))/distance
            if succ == destination:
                return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
            if (succ not in visited):
                visited.add(succ)
                cost = distance + cost_until_now                                 
                routeList.append(succ)                                           #Add current node to our list
                heappush(fringe, (cost + cal_heuristic(succ,destination), cost, copy.deepcopy(routeList), succ, time_taken+hours, gas_used+gas))
                routeList.pop()                                                  #Prepare the routelist for next node, i.e. ignore the current node

def solve_time(source,destination):
    fringe = []
    visited = {(source)}
    heappush(fringe, (0, adj_list[source][1], [], source, 0))
    while len(fringe) > 0:
        (time_taken, cost_until_now, routeList, currentNode, gas_used) = heappop(fringe)
        for (succ, distance, SpeedLimit) in successors(currentNode):
            hours = (distance/SpeedLimit)
            gas = (400 * (SpeedLimit/150) * ((1 - (SpeedLimit/150))**4))/distance
            if succ == destination:
                return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
            if (succ not in visited):   
                visited.add(succ)
                routeList.append(succ)                                     #Add current node to our list
                heappush(fringe, (time_taken+hours, cost_until_now + distance, copy.deepcopy(routeList), succ, gas_used+gas))
                routeList.pop()                                           #Prepare the routelist for next node, i.e. ignore the current node

def solve_mpg(source,destination):
    fringe = []
    visited = {(source)}
    heappush(fringe, (0, adj_list[source][1], [], source, 0))
    while len(fringe) > 0:
        (gas_used, cost_until_now, routeList, currentNode, time_taken) = heappop(fringe)
        for (succ, distance, SpeedLimit) in successors(currentNode):
            hours = (distance/SpeedLimit)
            gas = (400 * (SpeedLimit/150) * ((1 - (SpeedLimit/150))**4))/distance
            if succ == destination:        
                return (cost_until_now + distance, routeList, time_taken+hours, gas_used+gas)
            if (succ not in visited):
                visited.add(succ)
                routeList.append(succ)                                      #Add current node to our list
                heappush(fringe, (gas_used+gas, cost_until_now + distance, copy.deepcopy(routeList), succ, time_taken+hours))
                routeList.pop()                                             #Prepare the routelist for next node, i.e. ignore the current node       

if __name__ == "__main__":
    #Check if all the arguments are valid
    if(len(sys.argv) != 4):
        raise(Exception("Error: expected 2 arguments"))
    
    #Program starts here
    createAdjList('./road-segments.txt')
    readGPScoordinates('./city-gps.txt')

    source = sys.argv[1]                          
    destination = sys.argv[2]
    cost_function = sys.argv[3]

    if(cost_function.lower() == "segments"):
        result = solve_segments(source, destination)
    elif(cost_function.lower() == "distance"):
        result = solve_distance(source, destination)
    elif(cost_function.lower() == "time"):
        result = solve_time(source, destination)
    elif(cost_function.lower() == "mpg"):
        result = solve_mpg(source, destination)
    else:
        print("Please enter a valid cost function")
        sys.exit()

    if result is not None:
        totalsegments = len(result[1])+1                 #Last segment is counted here as +1
        totalmiles = result[0]
        totalhours = result[2]
        totalgasgallons = result[3]
        print("%d %d %.4f %.4f %s" % ((totalsegments, totalmiles, totalhours, totalgasgallons, source)), end=" ")
        for point in result[1]:
            print(point, end=" ")
        print(destination)
    else:
        print("INF")