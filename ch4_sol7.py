''' build order: you are given a list of projects and list of dependencies. 
Find a build order that will allow the projects to be built. 
If there is no valid build order, return an error '''

''' This is a classic topological sort of a DAG '''

'''
Input:
projects: a, b, c, d, e, f
dependencies: (a,d), (f, b), )b, d), (f, a), (d, c)

Output: f, e, a, b, d, c
'''

import os
import networkx as nx 
from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = {} # dictionary containing adjacency list
        for v in vertices:
            self.graph[v] = []
        self.V = len(vertices) # No. of vertices

    def addEdge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = []
        self.graph[u].append(v)
        

    def topologicalSortUtil(self, v, visited, stack):
        # mark the node as visited
        visited[v] = True

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)
        
        # push the current vertex to stack which stores result
        stack.insert(0,v)

    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = {}
        for v in self.graph.keys():
            visited[v] = False
        stack = []

        # Call the recursive helper function to store topological sort
        # starting from all vertices one by one
        #for i in range(self.V):
        #    if visited[i] is False:
        #        self.topologicalSortUtil(i, visited, stack)
        for v in self.graph.keys():
            if visited[v] is False:
                self.topologicalSortUtil(v, visited, stack)
        
        return stack


if __name__=="__main__":
    vertices = [0, 1, 2, 3, 4, 5]
    g = Graph(vertices)
    g.addEdge(5,2)
    g.addEdge(5,0)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)

    stack = g.topologicalSort()
    print(stack)

    vertices = ["a", "b", "c", "d", "e", "f"]
    g = Graph(vertices)
    g.addEdge("a", "d") # d depends on a
    g.addEdge("f", "b")
    g.addEdge("b", "d")
    g.addEdge("f", "a")
    g.addEdge("d", "c")

    stack = g.topologicalSort()
    print(stack)
    print(g.graph)