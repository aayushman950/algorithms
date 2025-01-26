import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def PrimMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                for edge in self.graph:
                    if edge[0] == u and edge[1] == v or edge[0] == v and edge[1] == u:
                        if edge[2] < key[v] and mstSet[v] == False:
                            key[v] = edge[2]
                            parent[v] = u
                            
        self.printMST(parent)

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.getEdgeWeight(parent[i], i))

    def getEdgeWeight(self, u, v):
        for edge in self.graph:
            if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                return edge[2]
        return 0
