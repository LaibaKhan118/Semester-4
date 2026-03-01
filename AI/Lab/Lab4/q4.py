graph = {
  'S': {'A': 4, 'B': 2},
  'A': {'C': 5, 'D': 10},
  'B': {'E': 3},
  'C': {'G': 4},
  'D': {'G': 1},
  'E': {'D': 4},
  'G': {}
}

def ucs(graph, start, goal):
  frontier=[(start, 0)]
  visited= set()
  costSoFar={start:0}
  cameFrom={start:None}

  while frontier:
    frontier.sort(key=lambda x: x[1])
    currNode, currCost = frontier.pop(0)
    if currNode in visited:
      continue
    visited.add(currNode)
    if currNode == goal:
      path=[]
      while currNode is not None:
        path.append(currNode)
        currNode=cameFrom[currNode]
      path.reverse()
      print("\nLeast Cost Path: ", path, "\nTotal Cost: ", currCost)
      return
    for neighbour, cost in graph[currNode].items():
      newCost=currCost+cost
      if neighbour not in costSoFar or newCost<costSoFar[neighbour]:
        costSoFar[neighbour]=newCost
        cameFrom[neighbour]=currNode
        frontier.append((neighbour, newCost))

  print("Goal Not Found")



ucs(graph,'S', 'G')
