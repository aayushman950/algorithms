import time
import matplotlib.pyplot as plt
from graph import Graph
from kruskal import KruskalAlgorithm
from prims import PrimAlgorithm

def generate_graph(num_vertices, num_edges):
    """Generate a random graph with the specified number of vertices and edges."""
    import random
    graph = Graph(num_vertices)
    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        while u == v:
            v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 100)
        graph.addEdge(u, v, weight)
    return graph

def measure_execution_time(vertices, edges):
    """Measure and return execution times for Kruskal and Prim algorithms."""
    graph = generate_graph(vertices, edges)

    # Measure time for Kruskal
    kruskal_algo = KruskalAlgorithm(graph)
    start_time = time.time()
    kruskal_algo.KruskalMST()
    kruskal_time = time.time() - start_time

    # Measure time for Prim
    prim_algo = PrimAlgorithm(graph)
    start_time = time.time()
    prim_algo.PrimMST()
    prim_time = time.time() - start_time

    return kruskal_time, prim_time

if __name__ == '__main__':
    # Graph sizes for comparison
    sizes = [
        (10, 30),
        (100, 1000),
        (200, 2000),
        (300, 3000),
        (500, 5000),
        (700, 10000),
    ]

    kruskal_times = []
    prim_times = []
    vertices_list = [size[0] for size in sizes]

    for vertices, edges in sizes:
        kruskal_time, prim_time = measure_execution_time(vertices, edges)
        kruskal_times.append(kruskal_time)
        prim_times.append(prim_time)
        print(f"Graph with {vertices} vertices and {edges} edges:")
        print(f"Kruskal's Algorithm Time: {kruskal_time:.6f} seconds")
        print(f"Prim's Algorithm Time: {prim_time:.6f} seconds")
        print("-" * 50)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(vertices_list, kruskal_times, label="Kruskal's Algorithm", marker='o')
    plt.plot(vertices_list, prim_times, label="Prim's Algorithm", marker='s')
    plt.title("Comparison of Running Times: Kruskal vs Prim")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()
