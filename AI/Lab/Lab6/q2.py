def h(n):
  return abs(20-n)
def beamSearch(start, goal, k):
  beam=[(start, [start])]
  level=0
  while beam:
    print(f"\nLevel {level} explored:", [node for node, _ in beam])
    newStates=[]
    for node,path in beam:
      if node==goal:
        print(f"\nGoal Reached\nPath: {path}")
        return
      neighbors=[node+2, node+3, node*2]
      for n in neighbors:
        if n <= goal:
          newStates.append((n, path+[n]))
    newStates.sort(key=lambda x: h(x[0]))
    beam = newStates[:k]
    level+=1

beamSearch(1, 20, 2)
