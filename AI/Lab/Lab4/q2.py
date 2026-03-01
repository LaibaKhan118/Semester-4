graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': ['G'],
'E': [],
'F': ['H'],
'G': [],
'H': []
}

def dls(graph, goal, limit, curr, path, visited):
  visited.append(curr)
  path.append(curr)
  if curr == goal:
    return True
  if limit <=0:
    path.pop()
    return False
  
  for neighbor in graph[curr]:
    if dls(graph, goal, limit-1, neighbor, path, visited):
      return True
  
  path.pop()
  return False

def run(limit):
  print("Running DLS with depth limit", limit)
  path = []
  visited= []
  found = dls(graph, 'H', limit, 'A', path, visited)

  print("Visit Order: ", visited)
  if found:
    print("Goal Found\nPath: ", path)
  else:
    print("Goal Not Found")

run(2)
run(3)
