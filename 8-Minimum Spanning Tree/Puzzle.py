from collections import deque # deque (double-ended queue)

def solve_puzzle(Board, Source, Destination):
    if Source == Destination:
        return ([Source], '')
    
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    path = []
    visited = set()
    parent = {}
    q = deque([Source])
    visited.add(Source)
    
    while q:
        # Get the cell at the FRONT of the queue
        current = q.popleft() 

        # If destination is reached, build output and terminate
        if current == Destination:
            # Reconstruct path
            while current:
                path.append(current)
                current = parent.get(current)
            # Reverse path for proper output order
            path = path[::-1] 

            # Convert path to directions
            directions = ''
            for i in range(1, len(path)):
                for d, (dx, dy) in moves.items():
                    if (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]) == (dx, dy):
                        directions += d
                        break

            return (path, directions)
        
        # for all adjacent cells to the current cell:
        for d, (dx, dy) in moves.items():
            # calculate the location of the adjacent cell
            nx, ny = current[0] + dx, current[1] + dy
            
            # if the adjacent cell is within the board AND there is no barrier AND the cell has not already been visited:
            if 0 <= nx < len(Board) and 0 <= ny < len(Board[0]) and Board[nx][ny] == '-' and (nx, ny) not in visited:
                # append the adjacent cell to the queue, mark as visited, and track heritage
                q.append((nx, ny))          # add to BACK of the queue
                visited.add((nx, ny))
                parent[(nx, ny)] = current
    
    return None

# Example usage
puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

print(solve_puzzle(puzzle, (0, 2), (2, 2))) # Answer: ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
print(solve_puzzle(puzzle, (0, 0), (4, 4))) # Answer: ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')
print(solve_puzzle(puzzle, (0, 0), (4, 0))) # Answer: None
print(solve_puzzle(puzzle, (0, 0), (0, 0))) # Answer: ([(0, 0)], '')