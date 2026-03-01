directions = [(0,1), (0, -1),(1, 0), (-1,0)]
def gridToGraph(grid):
  graph = {}
  rows = len(grid)
  cols=len(grid[0])
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        neighbors=[]
        for x, y in directions:
          nx, ny = x+i, y+j
          if 0<=nx<rows and 0<=ny<cols:
            if grid[nx][ny]==1:
              neighbors.append((nx, ny))
        graph[(i,j)]=neighbors
  return graph

def bfs(graph, start, goal):
  visited=[]
  queue=[]
  parent={}
  visited.append(start)
  queue.append(start)
  parent[start]=None
  print("BFS Traversal Order:");
  while queue:
    node=queue.pop(0)
    print(node, end=" ")
    if node == goal:
      print("\nGoal found!")
      break
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)
        parent[neighbor]=node
  path = []
  if goal in parent:
    curr = goal
    while curr is not None:
      path.append(curr)
      curr=parent[curr]
    path.reverse()
    print("\nShortest Path:\n", path)
  else:
    print("\nNo path found!")
  
building = [
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [1, 1, 0, 1],
  [1, 0, 1, 1]
]
graph= gridToGraph(building)
start=(0,0)
goal=(3,3)
bfs(graph, start, goal)
