from winreg import ExpandEnvironmentStrings
import numpy as np

class Graph:

    class Vertex:
        index = None  # should always be a number
        name = None

        def __init__(self, name, index):
            self.index = index
            self.name = name

        def __repr__(self):
            return "name: {}, index: {}".format(self.name, self.index)

    class Edge:
        nodeFrom = None
        nodeTo = None
        weight = None

        def __init__(self, nodeFrom, nodeTo, weight=0):
            self.nodeFrom = nodeFrom
            self.nodeTo = nodeTo
            self.weight = weight

        def __repr__(self):
            return "Node from: {}, Node to: {}, weight: {}".\
                format(repr(self.nodeFrom), repr(self.nodeTo), self.weight)

    nodes = []
    edges = []

    currentIndex = 0

    def insertEdge(self, vertexFrom, vertexTo, weight=0):
        """!
        Inserts an edge into the graph.
        """
        vFrom = None
        vTo = None

        for node in self.nodes:
            if node.name == vertexFrom:
                vFrom = node
            if node.name == vertexTo:
                vTo = node
        
        if vFrom == None:
            vFrom = self.Vertex(vertexFrom, self.currentIndex)
            self.currentIndex += 1            
            self.nodes.append(vFrom)
        if vTo == None:
            vTo = self.Vertex(vertexTo, self.currentIndex)
            self.currentIndex += 1
            self.nodes.append(vTo)
        self.edges.append(self.Edge(vFrom, vTo, weight))
        
    def print(self):
        for edge in self.edges:
            print(edge)

    def getAdjacentMatrix(self):
        """!
        Returns the adjacent matrix of our graph.
        """
        adjacentMatrix = np.zeros([self.currentIndex, self.currentIndex])

        for edge in self.edges:
            adjacentMatrix[edge.nodeFrom.index][edge.nodeTo.index] = edge.weight
        
        return adjacentMatrix
    
    def printAdjacentMatrix(self):
        """!
        Prints the adjacent matrix.
        """
        print(self.getAdjacentMatrix())

if __name__ == "__main__":
    g = Graph()

    g.insertEdge("A", "B", 1.5)
    g.insertEdge("A", "C", 1)
    g.insertEdge("A", "D", 2.7)
    g.insertEdge("C", "D", 3.5)
    g.insertEdge("D", "E", 1.1)
    g.insertEdge("D", "F", 1.5)

    g.print()

    g.printAdjacentMatrix()

