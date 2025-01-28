import time
import random
import matplotlib.pyplot as plt
from kruskal import kruskal
from prim import prim

def generate_connected_graph(V, E):
    if E < V - 1:
        raise ValueError("E must be at least V-1")
    edges = []
    for i in range(1, V):
        u = i
        v = random.randint(0, i-1)
        edges.append((u, v, random.randint(1, 100)))
    for _ in range(E - (V - 1)):
        u, v = random.sample(range(V), 2)
        edges.append((u, v, random.randint(1, 100)))
    adj_list = [[] for _ in range(V)]
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    return edges, adj_list

def main():    
    # Modify dense_vertices to test larger graphs (e.g., up to V=200)
    dense_vertices = range(10, 1000, 100)  # Increased step size for faster testing
    dk_times, dp_times = [], []
    for V in dense_vertices:
        E = V * (V - 1) // 2
        edges, adj_list = generate_connected_graph(V, E)
        start = time.time()
        kruskal(V, edges)
        dk_times.append(time.time() - start)
        start = time.time()
        prim(adj_list, V)
        dp_times.append(time.time() - start)

    plt.plot(dense_vertices, dk_times, label='Kruskal')
    plt.plot(dense_vertices, dp_times, label='Prim')
    plt.xlabel('Vertices')
    plt.ylabel('Time (s)')
    plt.legend()

    plt.tight_layout()
    plt.savefig('comparison.png')
    plt.show()

if __name__ == "__main__":
    main()