#!/usr/local/bin/python3

# put your routing program here!

class Graph:
    def __init__(self):
        self.vertices = {}
  
    def add_edge(self,src,dest):
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n")

class Vertex:
    def __init__(self,city):
        self.name = city
        self.neighbours = []
    
    def add_neighbour(self,neighbour,dist):
        if isinstance(neighbour,Vertex):
            self.neighbours = neighbour

if __name__ == "__main__":
    count = len(open("city-gps.txt",'r').readlines())
    graph = Graph(count)
    with open("city-gps.txt",'r') as file:
        for line in file:

