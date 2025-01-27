class KruskalAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph.graph = sorted(self.graph.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.graph.V):
            parent.append(node)
            rank.append(0)

        while e < self.graph.V - 1:
            u, v, w = self.graph.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Edges in the constructed MST using Kruskal's Algorithm:")
        total_weight = 0
        for u, v, weight in result:
            total_weight += weight
            print(f"{u} -- {v} == {weight}")
        print(f"Total Weight of MST: {total_weight}")
