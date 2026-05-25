
import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#1296F0"
        self.id = str(uuid.uuid4())


def generate_color(step, total):
    intensity = int(255 * (step / total))
    return f"#{intensity:02x}{100:02x}{255-intensity:02x}"


def dfs(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()

        if node:
            order.append(node)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

    return order


def bfs(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()

        if node:
            order.append(node)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return order


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}

    tree = add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )

    plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)

    traversal = dfs(root)

    for i, node in enumerate(traversal):
        node.color = generate_color(i, len(traversal))

    draw_tree(root)
