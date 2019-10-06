adj_list = {}
def loadFile(adj_list):
    with open("C:\\Users\\Rohit\\Documents\\AI\\commit\\bagrawal-aahurkat-rrokde-a1\\part2\\road-segments.txt",'r') as file:
        for line in file:
            from_city = str.split(line)[0]
            to_city = str.split(line)[1]
            length = str.split(line)[2]
            speed_limit = str.split(line)[3]
            highway_name = str.split(line)[4]
            if from_city in adj_list.keys():
                old = adj_list[from_city]
                old.append((to_city,length,speed_limit,highway_name))
                adj_list[from_city] = old
            else:
                adj_list[from_city] = []
                adj_list[from_city].append((to_city,length,speed_limit,highway_name))
            
            if to_city in adj_list.keys():
                old = adj_list[to_city]
                old.append((from_city,length,speed_limit,highway_name))
                adj_list[to_city] = old
 
def successors(args):
    possible_list = args[0]
    source = args[1]
    destination = args[2]
    travelled_cost = args[3]

    return [(possible neighbour, ) for neighbour in adj_list[source]]
    return True

def solve(source, destination):
    solution = []
    possible_list = [(source)]
    fringe = [ (possible_list, source, destination, 0) ] #Forth paramter is the travelled cost
    while len(fringe) > 0:
        elem = fringe.pop()
        for neighbour in successors(elem):
            travelle_cost = 


    return True

def calculateHeurisic():
    return True

if __name__ == "__main__":

    loadFile(adj_list)

       
    print("adjancency list is:  ")
    for key in adj_list:
        print("no of neighbours: ", len(adj_list[key]), " for city: ", key)
        print(key, '->', adj_list[key])

