goals = ['I', 'J']
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}
def bfs(graph, start, goals):
  frontier=[(start, 0)]
  visited= set()
  path = []
  foundGoals=set()

  while frontier and len(foundGoals)<len(goals):
    frontier.sort(key=lambda x: x[1])
    currNode, _ = frontier.pop(0)
    if currNode in visited:
      continue
    visited.add(currNode)
    path.append(currNode)
    if currNode in goals:
      print(f"Goal {currNode} found!")
      foundGoals.add(currNode)
    for neighbour, h_val in graph[currNode]:
      if neighbour not in visited:
        frontier.append((neighbour, h_val))

  if len(foundGoals) == len(goals):
    print("\nAll goals visited!\nTraversal path: ", path)
  else:
    print("Could not reach all goals")

bfs(graph, 'S', goals)
