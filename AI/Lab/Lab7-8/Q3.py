#Task 3:
class GameNode:
    def __init__(self, name, value=None, children=None, is_max=True):
        self.name = name
        self.value = value
        self.children = children
        self.is_max = is_max

L1 = GameNode("L1", value=8)
L2 = GameNode("L2", value=5)
L3 = GameNode("L3", value=6)
L4 = GameNode("L4", value=2)

N3 = GameNode("N3", children=[L1, L2], is_max=True)
N4 = GameNode("N4", children=[L3, L4], is_max=True)

L5 = GameNode("L5", value=1)
L6 = GameNode("L6", value=0)
L7 = GameNode("L7", value=4)
L8 = GameNode("L8", value=7)
L9 = GameNode("L9", value=10)

N5 = GameNode("N5", children=[L5, L6], is_max=True)
N6 = GameNode("N6", children=[L7, L8, L9], is_max=True)

N1 = GameNode("N1", children=[N3, N4], is_max=False)
N2 = GameNode("N2", children=[N5, N6], is_max=False)

root = GameNode("Root", children=[N1, N2], is_max=True)

def minimax(node):
    if not node.children:
        return node.value
    if node.is_max:
        return max(minimax(child) for child in node.children)
    else:
        return min(minimax(child) for child in node.children)

def alphabeta_path(node, alpha, beta, path):
    path.append(node.name)
    if not node.children:
        return node.value, path
    if node.is_max:
        best = -float('inf')
        best_path = None
        for child in node.children:
            val, child_path = alphabeta_path(child, alpha, beta, path[:])
            if val > best:
                best = val
                best_path = child_path
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best, best_path
    else:
        best = float('inf')
        best_path = None
        for child in node.children:
            val, child_path = alphabeta_path(child, alpha, beta, path[:])
            if val < best:
                best = val
                best_path = child_path
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best, best_path

root_val = minimax(root)
print("Minimax root value (modified tree):", root_val)

ab_val, optimal_path = alphabeta_path(root, -float('inf'), float('inf'), [])
print("Alpha‑Beta root value:", ab_val)
print("Optimal path for Max:", " -> ".join(optimal_path))
