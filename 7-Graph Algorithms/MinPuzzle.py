# from collections import deque

# def minEffort(puzzle):
#     height, width = len(puzzle), len(puzzle[0])

#     # 2D matrix to track the minimum effort required to reach each cell. Values initialized to infinity
#     effort = [[float('inf')] * width for _ in range(height)]
#     effort[0][0] = 0 # Initialize effort to reach starting cell to 0

#     # Queue to store cells in BFS order, starting with the cell [0, 0]
#     queue = deque([(0, 0, 0)])  # 0 effort to reach Cell [0][0]

#     while queue:
#         # Extract the cell with the minimum effort from the queue (effort, cell [x, y] coordinates)
#         eff, x, y = queue.popleft()

#         # Terminate when we reach bottom right cell [m-1][n-1]
#         if x == height - 1 and y == width - 1:
#             return eff
        
#         # For each of the current cell's 4 neighbors (up, down, left, right), calculate the effort needed to reach each neighbor 
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

#             # Calculate neighbor cell coordinates
#             nx, ny = x + dx, y + dy

#             # If neighbor cell is in puzzle grid, calculate the effort needed to move from the current cell (x, y) to the neighbor cell (nx, ny)
#             if 0 <= nx < height and 0 <= ny < width:                        
#                 new_eff = max(eff, abs(puzzle[nx][ny] - puzzle[x][y]))    

#                 # If new_eff is less than previously recorded efforts, update to lower value
#                 if effort[nx][ny] > new_eff:
#                     effort[nx][ny] = new_eff
#                     queue.append((new_eff, nx, ny))

#     return effort[height-1][width-1]

def minEffort(puzzle):
    height, width = len(puzzle), len(puzzle[0])

    # 2D matrix to track the minimum effort required to reach each cell. Values initialized to infinity
    effort = [[float('inf')] * width for _ in range(height)]
    effort[0][0] = 0  # Starting cell requires no effort to reach from itself.
    
    # Directions for moving to neighboring cells: right, down, left, up.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y, currentEffort):
        # Terminate when we reach bottom right cell [m-1][n-1]
        if x == height - 1 and y == width - 1:
            return currentEffort
        
        # Temporarily mark this cell as visited by setting its effort to a special value.
        temp = effort[x][y]
        effort[x][y] = float('-inf')  # Use -inf to indicate the cell is being visited.
        
        minEffort = float('inf')
        # Explore all 4 neighboring cells.
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # If neighbor cell is in puzzle grid, calculate the effort needed to move from the current cell to the neighbor cell
            if 0 <= nx < height and 0 <= ny < width and effort[nx][ny] != float('-inf'):
                newEffort = max(currentEffort, abs(puzzle[nx][ny] - puzzle[x][y]))

                # If new_eff is less than previously recorded efforts, update to lower value
                if newEffort < effort[nx][ny]:
                    candidateEffort = dfs(nx, ny, newEffort)
                    minEffort = min(minEffort, candidateEffort)
        
        # Restore the cell's effort after visiting.
        effort[x][y] = temp
        
        return minEffort if minEffort != float('inf') else currentEffort
    
    # Start DFS from the top-left cell.
    return dfs(0, 0, 0)

# Example usage
example_puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(example_puzzle))                    # Output: 1