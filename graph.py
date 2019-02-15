import Queue 
import os

class Vertex():
    def __init__(self, x):
        self.id = x 
        self.adjacent = {}
        self.visited = False 

    def addAdjacent(self, adjvertex):
        self.adjacent[adjvertex] = 1

    def getAdjacent(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id 

class Graph():
    def __init__(self):
        self.vertexList = []
        self.numVertices = 0
    
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertexList.append(newVertex)
        self.numVertices += 1
        return newVertex

    def getVertex(self, key):
        isthere = False
        for i, v in enumerate(self.vertexList):
            if v.getId() == key:
                return v 
        return None 
    
    def addEdge(self, a, b, weight=1):
        a_vertex = self.getVertex(a)
        b_vertex = self.getVertex(b)
        if a_vertex is None:
            a_vertex = self.addVertex(a)
            self.numVertices += 1
        if b_vertex is None:
            b_vertex = self.addVertex(b)
            self.numVertices += 1

        # undirected graph
        a_vertex.addAdjacent(b_vertex)
        #b_vertex.addAdjacent(a_vertex)

    def printGraph(self):
        for v in self.vertexList:
            print(v.getId())

def breadthfirstsearch(g, start, end):
    if start.getId() == end.getId():
        return True
    q = Queue.Queue(g.numVertices)
    start.visited = True
    q.put(start)
    traverse = []
    while not q.empty():
        r = q.get()
        #print(r.getId())
        traverse.append(r.getId())
        if r != None:
            adjacent = r.getAdjacent()
            for v in adjacent:
                if v.visited == False:
                    if v.getId() == end.getId():
                        #print(v.getId())
                        traverse.append(v.getId())
                        return True 
                    else:
                        q.put(v)
                    v.visited = True 
    return False         

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