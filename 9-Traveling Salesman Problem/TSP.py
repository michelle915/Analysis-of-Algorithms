def solve_tsp(G):
    n = len(G)
    visited = [False] * n

    # Start from the first city (index 0)
    path = [0]      
    visited[0] = True

    for _ in range(1, n):
        last_visited_node = path[-1]
        nearest_node = -1
        nearest_distance = float('inf')

        # update nearest_node and nearest_distance with the index and distance of the nearest unvisited node
        for i in range(n):
            if not visited[i] and 0 < G[last_visited_node][i] < nearest_distance:
                nearest_node = i
                nearest_distance = G[last_visited_node][i]

        path.append(nearest_node)
        visited[nearest_node] = True    

    # Complete the cycle by going back to the starting city
    path.append(0)  

    return path

# Example
input = [ 
	[0, 2, 3, 20, 1], 
	[2, 0, 15, 2, 20], 
	[3, 15, 0, 20, 13], 
	[20, 2, 20, 0, 9], 
	[1, 20, 13, 9, 0], 
	]

print(solve_tsp(input)) # Answer: [0, 4, 3, 1, 2, 0]