#Task 1
class GameNode:
    def __init__(self, name, value=None, children=None, is_max=True):
        self.name = name
        self.value = value
        self.children = children
        self.is_max = is_max

L1 = GameNode("L1", value=3)
L2 = GameNode("L2", value=5)
L3 = GameNode("L3", value=6)
L4 = GameNode("L4", value=2)

N3 = GameNode("N3", children=[L1, L2], is_max=True)
N4 = GameNode("N4", children=[L3, L4], is_max=True)

L5 = GameNode("L5", value=1)
L6 = GameNode("L6", value=9)
L7 = GameNode("L7", value=4)
L8 = GameNode("L8", value=7)
N5 = GameNode("N5", children=[L5, L6], is_max=True)
N6 = GameNode("N6", children=[L7, L8], is_max=True)

N1 = GameNode("N1", children=[N3, N4], is_max=False)
N2 = GameNode("N2", children=[N5, N6], is_max=False)

root = GameNode("Root", children=[N1, N2], is_max=True)

visited_nodes = []

def minimax(node):
    visited_nodes.append(node.name)
    if not node.children:
        return node.value
    if node.is_max:
        best = -float('inf')
        for child in node.children:
            val = minimax(child)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for child in node.children:
            val = minimax(child)
            best = min(best, val)
        return best

root_value = minimax(root)
print("Minimax root value:", root_value)
print("Nodes visited:", visited_nodes)
