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
        if vTo == None:
            vTo = self.Vertex(vertexTo, self.currentIndex)
            self.currentIndex += 1
        self.nodes.append(vFrom)
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

    def shortestPathDijkstra(self, srcNodeName, targetNodeName):
        """!
        Computes the shortest path between srcNodeName and targetNodeName.
        Returns the path from srcNodeName to targetNodeName, as well as the
        minimal distance between them.
        """
        # compute index for node
        srcIndex = [x.index for x in self.nodes if x.name == srcNodeName][0]
        targetIndex = [x.index for x in self.nodes if x.name == targetNodeName][0]

        # generate adjacent matrix
        adjMatrix = self.getAdjacentMatrix()

        # stores the predecessor with minimal cost
        predecessors = [None]*len(adjMatrix)

        # stores the minimal costs for each node
        costs = [np.infty]*len(adjMatrix)

        queue = [(srcIndex, 0.)]

        while len(queue) > 0:
            
            currentNode, value = queue[0]
            queue = queue[1:]

            for successor in range(len(adjMatrix)):
                if adjMatrix[currentNode][successor] > 0:
                    if costs[successor] > adjMatrix[currentNode][successor]+value:
                        costs[successor] = adjMatrix[currentNode][successor]+value
                        predecessors[successor] = currentNode
                    queue.append((successor, costs[successor]))
        
            queue.sort(key=lambda x: x[1])
            if len(queue) > 0 and queue[0] == targetIndex:
                break

        # find the minimal path 
        path = [targetIndex]
        node = targetIndex
        while predecessors[node] != None:
            node = predecessors[node]
            path.insert(0, node)

        return path, costs[targetIndex]



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

    print("===== shortest path from 1 to 6 =====")
    print(g.shortestPathDijkstra("A", "F"))



