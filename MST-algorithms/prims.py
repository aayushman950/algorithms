import sys

class PrimAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.graph.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def PrimMST(self):
        key = [sys.maxsize] * self.graph.V
        parent = [None] * self.graph.V
        key[0] = 0
        mstSet = [False] * self.graph.V
        parent[0] = -1

        for _ in range(self.graph.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for edge in self.graph.graph:
                if edge[0] == u or edge[1] == u:
                    v = edge[1] if edge[0] == u else edge[0]
                    if not mstSet[v] and edge[2] < key[v]:
                        key[v] = edge[2]
                        parent[v] = u

        print("Edges in the constructed MST using Prim's Algorithm:")
        total_weight = 0
        for i in range(1, self.graph.V):
            for edge in self.graph.graph:
                if (edge[0] == parent[i] and edge[1] == i) or (edge[1] == parent[i] and edge[0] == i):
                    weight = edge[2]
                    total_weight += weight
                    print(f"{parent[i]} -- {i} == {weight}")
                    break
        print(f"Total Weight of MST: {total_weight}")
