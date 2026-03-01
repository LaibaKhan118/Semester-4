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

def run(start, goal, depth):
  for limit in range(depth+1):
    print("At depth limit: ", limit)
    path = []
    visited= []
    found = dls(graph, goal, limit, start, path, visited)

    print("Visit Order: ", visited)
    if found:
      print("Goal Found\nPath: ", path)
      return
    else:
      print("Goal Not Found")

run('A', 'G', 5)
