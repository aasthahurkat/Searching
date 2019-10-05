#!/usr/local/bin/python3

# put your routing program here!
class Vertex:
    def __init__(self, vertex,lat,lon):
        self.name = vertex
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
            #self.vertices[vertex.name] = vertex.neighbors
            self.vertices[vertex.name] = vertex.neighbors

    def add_edge(self, vertex_from, vertex_to,dist,limit,highway):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            print("inside first if")
            vertex_from.add_neighbor(vertex_to,dist,limit,highway)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                print("inside second if")
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
            else:
                print("inner else")
        else:
            print("add edge encountered else")
     

    def add_edge1(self, vertex_from, vertex_to,dist,limit,highway):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            print("inside first if")
            vertex_from.add_neighbor(vertex_to,dist,limit,highway)
            if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
                print("inside second if")
                self.vertices[vertex_from.name] = vertex_from.neighbors
                self.vertices[vertex_to.name] = vertex_to.neighbors
            else:
                print("inner else")
        else:
            print("add edge encountered else")
                            
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
    with open("city-gps.txt",'r') as file:
        for line in file:
            city_name = str.split(line)[0]
            latitude = str.split(line)[1]
            longitude = str.split(line)[2] 
            #print("city name: ",city_name)
            city = Vertex(city_name,latitude,longitude)
            US_map.add_vertex(city)
    
    with open("road-segments.txt",'r') as file:
        for line in file:
            from_city = str.split(line)[0]
            print("from_city: ", from_city)
            to_city = str.split(line)[1]
            print("to-city: ", to_city)
            length = str.split(line)[2]
            speed_limit = str.split(line)[3]
            highway_name = str.split(line)[4]
            US_map.add_edge(from_city,to_city,length,speed_limit,highway_name)
    
    print("Adjancency list is:")
    print(graph(US_map))