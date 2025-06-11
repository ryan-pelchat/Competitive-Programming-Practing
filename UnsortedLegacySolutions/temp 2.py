class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


# Helper function to print the AVL Tree structure
def pre_order(root):
    if not root:
        return
    print(f"{root.key}", end=" ")
    pre_order(root.left)
    pre_order(root.right)


import graphviz


def visualize_tree(root):
    def add_nodes_edges(dot, node):
        if node:
            dot.node(str(node.key), str(node.key))
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                add_nodes_edges(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                add_nodes_edges(dot, node.right)

    dot = graphviz.Digraph()
    add_nodes_edges(dot, root)
    return dot


# Create AVL tree, insert nodes, and generate visualization
avl_tree = AVLTree()
root = None
numbers = list(range(74))

for number in numbers:
    root = avl_tree.insert(root, number)

# Generate and view the graph
dot = visualize_tree(root)
dot.render("avl_tree", format="png", cleanup=True)
