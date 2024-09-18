import heapq  

def Prims(G):
    num_vertices = len(G)
    mst_vertices = [False] * num_vertices       # Track vertices included in MST
    edge_count = 0                              # Number of edges in MST
    mst = []
    pq = []                                     # Priority queue (pq): (weight, v1, v2). pq keeps the element with the smallest weight at the root of the heap

    # Start with vertex 0 and add all its edges to the priority queue
    mst_vertices[0] = True
    for y, weight in enumerate(G[0]):           # enumerate(G[0]) -> y, weight = index, value @ index
        if weight > 0:
            heapq.heappush(pq, (weight, 0, y))

    # While the pq is not empty AND the MST is not complete
    while pq and (edge_count < num_vertices - 1):
        weight, x, y = heapq.heappop(pq)        # returns the element with the smallest weight from the heap

        # If new vertix, connect:
        if not mst_vertices[y]:
            mst_vertices[y] = True
            mst.append((x, y, weight))          # MST: (v1, v2, weight)
            edge_count += 1

            # Add all valid edges from the new vertex to the priority queue
            for z, weight in enumerate(G[y]):
                if weight > 0 and not mst_vertices[z]:
                    heapq.heappush(pq, (weight, y, z))

    return mst

example_graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

print("MST:", Prims(example_graph)) # MST:  [(0, 2, 5), (2, 3, 3), (3, 1, 2), (3, 4, 12), (2, 5, 16), (4, 6, 4)]