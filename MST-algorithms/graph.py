from kruskal import Graph as KruskalGraph
from prims import Graph as PrimGraph

if __name__ == '__main__':
    # Kruskal's Algorithm
    g1 = KruskalGraph(5)
    g1.addEdge(0, 1, 2)
    g1.addEdge(0, 3, 6)
    g1.addEdge(1, 2, 3)
    g1.addEdge(1, 3, 8)
    g1.addEdge(1, 4, 5)
    g1.addEdge(2, 4, 7)
    g1.addEdge(3, 4, 9)
    g1.KruskalMST()

    # Prim's Algorithm
    g2 = PrimGraph(5)
    g2.addEdge(0, 1, 2)
    g2.addEdge(0, 3, 6)
    g2.addEdge(1, 2, 3)
    g2.addEdge(1, 3, 8)
    g2.addEdge(1, 4, 5)
    g2.addEdge(2, 4, 7)
    g2.addEdge(3, 4, 9)
    g2.PrimMST()
