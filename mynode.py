from graphviz import Digraph

class Node():
  def __init__(self, key):
    # self.key = key
  
    self.left = None
    self.right = None
    self.value = key

  # Функция для добавления нового узла
def insert(root, key):
    if root is None:
      return Node(key)
    else:
      if root.value < key:
          root.right = insert(root.right, key)
      else:
          root.left = insert(root.left, key)
    return root

def visualize_tree(root):
    dot = Digraph()
    _add_nodes_edges(dot, root)
    return dot

def _add_nodes_edges(dot, node):
    if node is not None:
        dot.node(str(node.value), str(node.value))
        if node.left:
            dot.edge(str(node.value), str(node.left.value))
            _add_nodes_edges(dot, node.left)
        if node.right:
            dot.edge(str(node.value), str(node.right.value))
            _add_nodes_edges(dot, node.right)
  
root = Node(70)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

tree_visual = visualize_tree(root)
tree_visual.render('binary_search_tree', format='png', cleanup=True)