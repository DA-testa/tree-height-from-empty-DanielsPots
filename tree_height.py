# python3

import os

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []


def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None
    for i, parent_index in enumerate(parents):
        if parent_index == -1:
            root = nodes[i]
        else:
            nodes[parent_index].children.append(nodes[i])
    
    if root is None:
        return 0
    
    def dfs(node):
        if not node.children:
            return 1
        return 1 + max(dfs(child) for child in node.children)
    
    return dfs(root)


def main():
    # input from keyboard
    file_name = input("Enter input file name (press Enter for keyboard input): ")
    if file_name and 'a' not in file_name:
        if os.path.exists(f"test/{file_name}"):
            with open(f"test/{file_name}") as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().split()))
        else:
            print(f"File 'inputs/{file_name}' not found.")
            return
    else:
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of the nodes (space-separated): ").split()))
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
import sys, threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

