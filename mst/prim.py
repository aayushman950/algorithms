import heapq

def prim(adj_list, num_vertices):
    key = [float('inf')] * num_vertices
    parent = [None] * num_vertices
    key[0] = 0
    heap = [(0, 0)]
    visited = [False] * num_vertices

    while heap:
        current_key, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj_list[u]:
            if not visited[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(heap, (w, v))
    return parent