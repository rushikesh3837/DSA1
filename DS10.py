import heapq

# Maze Representation
# 0 = Free Path, 1 = Wall
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

ROWS = len(maze)
COLS = len(maze[0])
start = (0, 0)
goal = (4, 4)

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search Algorithm
def astar(maze, start, goal):
    priority_queue = []
    # Push item as (f_cost, coordinates)
    heapq.heappush(priority_queue, (0, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    while priority_queue:
        # Pop the node with the lowest f_cost
        current = heapq.heappop(priority_queue)[1]
        
        # Goal check
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
            
        x, y = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            # Check boundaries
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                # Check if it's a free path (not a wall)
                if maze[nx][ny] == 0:
                    new_cost = g_cost[current] + 1
                    neighbor = (nx, ny)
                    
                    # If neighbor hasn't been visited or a shorter path is found
                    if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                        g_cost[neighbor] = new_cost
                        f_cost = new_cost + heuristic(neighbor, goal)
                        heapq.heappush(priority_queue, (f_cost, neighbor))
                        came_from[neighbor] = current
                        
    return None

# Display Maze
def printMaze(maze, path):
    display = []
    for row in maze:
        display.append(row[:])
        
    # Mark the path elements
    if path:
        for x, y in path:
            display[x][y] = "*"
            
    # Mark Start and Goal locations
    sx, sy = start
    gx, gy = goal
    display[sx][sy] = "S"
    display[gx][gy] = "G"
    
    print("\nSolved Maze\n")
    for row in display:
        for cell in row:
            if cell == 1:
                print("█", end=" ")
            elif cell == "*":
                print("*", end=" ")
            elif cell == "S":
                print("S", end=" ")
            elif cell == "G":
                print("G", end=" ")
            else:
                print(".", end=" ")
        print()

# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    path = astar(maze, start, goal)
    
    if path:
        print("\nShortest Path Found\n")
        print(path)
        print("\nPath Length =", len(path) - 1)
        printMaze(maze, path)
    else:
        print("No Path Found")
