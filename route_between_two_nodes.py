# Given a directed graph, design an algorithm to find out whether there is a route between two nodes

import os
from graph import Graph, Vertex
from graph import breadthfirstsearch 

# Solution: A simple breadth first or depth first search will work here
# solution in graph.py file
# or dijkstra's algorithm to find the shortest path


if __name__=="__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)
    g.printGraph() 

    print(breadthfirstsearch(g, g.getVertex(0), g.getVertex(4))) 