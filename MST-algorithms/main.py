from graph import Graph
from kruskal import KruskalAlgorithm
from prims import PrimAlgorithm

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 3, 6)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 8)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 4, 7)
    g.addEdge(3, 4, 9)

    print("Running Kruskal's Algorithm:")
    kruskal = KruskalAlgorithm(g)
    kruskal.KruskalMST()

    print("\nRunning Prim's Algorithm:")
    prim = PrimAlgorithm(g)
    prim.PrimMST()
