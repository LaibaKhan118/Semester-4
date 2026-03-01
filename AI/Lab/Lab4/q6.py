import random
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic ={
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}

def randomEdge(graph):
    u = random.choice(list(graph.keys()))
    if not graph[u]:
        return None
    v =random.choice(list(graph[u].keys()))
    oldCost= graph[u][v]
    change = random.choice([-3, -2, -1, 1, 2, 3])
    newCost =max(1, oldCost+change)
    graph[u][v] = newCost
    print(f"\nEdge cost changed: {u}->{v}: {oldCost}->{newCost}")
    return u, v

def dynamic_astar(graph, heuristic, start, goal):
    frontier = [(start, 0)]
    gCost= {start: 0}
    parent = {start: None}
    visited =set()
    steps = 0
    while frontier:
        frontier.sort(key=lambda x: x[1])
        curr, _ =frontier.pop(0)
        if curr in visited:
            continue
        visited.add(curr)

        if curr== goal:
            path=[]
            node =goal
            while node is not None:
                path.append(node)
                node =parent[node]
            path.reverse()
            print("\nOptimal Path Found:", path)
            print("Total Cost:", gCost[goal])
            return

        steps += 1
        if steps%3 ==0:
            changed =randomEdge(graph)
        for neighbor, cost in graph[curr].items():
            newG =gCost[curr] +cost
            if neighbor not in gCost or newG<gCost[neighbor]:
                gCost[neighbor] = newG
                f_value=newG+heuristic[neighbor]
                parent[neighbor] =curr
                frontier.append((neighbor, f_value))
    print("Goal not reachable")

dynamic_astar(graph, heuristic, 'A', 'G')
