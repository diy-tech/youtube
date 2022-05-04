import sys

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

    def bellman_ford(self, startNodeName, targetNodeName):
        """!
        Computes the bellman-ford shortest path from startNodeName to
        targetNodeName.
        Returns the minimum distance from startNodeName to targetNodeName,
        as well as the path.
        """
        distance = [sys.maxsize]*len(self.nodes)
        predecessors = [None]*len(self.nodes)

        startIdx = [x.index for x in self.nodes if x.name == startNodeName][0]
        targetIdx = [x.index for x in self.nodes if x.name == targetNodeName][0]

        # init distance at startIdx
        distance[startIdx] = 0.

        for _ in range(len(self.nodes)-1):
            for edge in self.edges:
                u = edge.nodeFrom.index
                v = edge.nodeTo.index
                weight = edge.weight

                if distance[u]+weight < distance[v]:
                    distance[v] = distance[u]+weight
                    predecessors[v] = u
        
        # negative cycle detection
        for edge in self.edges:
            u = edge.nodeFrom.index
            v = edge.nodeTo.index
            weight = edge.weight
            if distance[u] + weight < distance[v]:
                return -1, []

        path = [targetIdx]
        u = targetIdx
        while predecessors[u] != None:
            u = predecessors[u]
            path.insert(0, u)
        
        return path, distance[targetIdx]


if __name__ == "__main__":
    g = Graph()

    g.insertEdge("A", "B", 1.5)
    g.insertEdge("A", "C", 2.7)
    g.insertEdge("A", "D", 3.5)
    g.insertEdge("C", "E", 1.1)
    g.insertEdge("C", "F", 1.5)
    g.insertEdge("D", "C", -1)

    g.print()

    print()
    print(g.bellman_ford("A", "F"))
