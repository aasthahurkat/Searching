#!/usr/local/bin/python3

# put your routing program here!
class Vertex:
    def __init__(self, name,lat,lon):
        self.name = name
        self.neighbors = []
        self.lat = lat
        self.lon = lon
        
    def add_neighbor(self, neighbor,dist,limit,highway):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append((neighbor.name,dist,limit,highway))
                neighbor.neighbors.append((self.name,dist,limit,highway))
        else:
            print("not added neighbour")
            return False
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex
            #self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, vertex_from, vertex_to,dist,limit,highway):
        #if isinstance(Vertex[vertex_from], Vertex) and isinstance(Vertex[vertex_to, Vertex):
        
        if vertex_from in self.vertices and vertex_to in self.vertices:
           # print("inside first if")
            self.vertices[vertex_from].neighbors.append((self.vertices[vertex_to], dist, limit, highway))
            self.vertices[vertex_to].neighbors.append((self.vertices[vertex_from], dist, limit, highway))
        else:
            print("decide fo rjunction: from: ", vertex_from, "to:  ", vertex_to)
        
                      
    def adjacencyList(self):
        if len(self.vertices) >= 1:
                return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]  
        else:
            return dict()

def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) 

if __name__ == "__main__":
    #count = len(open("city-gps.txt",'r').readlines())
    US_map = Graph()
    cities = []
    i = 0
    with open("D:\\Fall 2019\\551 - EAI\\Assignment\\1\\bagrawal-aahurkat-rrokde-a1-master\\bagrawal-aahurkat-rrokde-a1-master\\part2\\city-gps.txt",'r') as file:
        for line in file:
            city_name = str.split(line)[0]
            latitude = str.split(line)[1]
            longitude = str.split(line)[2] 
            #print("city name: ",city_name)
            city = Vertex(city_name,latitude,longitude)
            US_map.add_vertex(city)
    
    with open("D:\\Fall 2019\\551 - EAI\\Assignment\\1\\bagrawal-aahurkat-rrokde-a1-master\\bagrawal-aahurkat-rrokde-a1-master\\part2\\road-segments.txt",'r') as file:
        for line in file:
            from_city = str.split(line)[0]
            #print("from_city: ", from_city)
            to_city = str.split(line)[1]
            #print("to-city: ", to_city)
            length = str.split(line)[2]
            speed_limit = str.split(line)[3]
            highway_name = str.split(line)[4]
            US_map.add_edge(from_city,to_city,length,speed_limit,highway_name)
    
    print("Adjancency list is:")
    print(graph(US_map))