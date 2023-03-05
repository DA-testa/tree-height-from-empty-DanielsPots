# python3

import sys
import threading
import os


def compute_height(n, parents):
    # An array of nodes with empty children
    nodes = [[] for _ in range(n)]
    # Filling the array of nodes with their corresponding children
    for i in range(n):
        if parents[i] == -1:
            root = 1
        else:
            nodes[parents[i]].append(i)
    # Recursivley computing the height of the tree
    def height(node):
        if not nodes[node]:
            return 1
        return 1 + max(height(child) for child in nodes[node])
    return height(root)


def main():
    # implement input form keyboard and from files
    file_name = input().strip()
    # let user input file name to use, don't allow file names with letter 'a'
    while 'a' in file_name:
        print("Invalid file, enter a file name without the letter 'a'")
        file_name = input().strip()
    # check if the file exists in the folder
    while not os.path.exists(f"test/{file_name}"):
        print("File not found, enter a valid file name")
        file_name = input().strip()
        while 'a' in file_name:
            print("Invalid file, enter a file name without the letter 'a'")
            file_name = input().strip()
    # read inputs from the file
    with open(f"test/{file_name}", 'r') as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))
    # call the function and output its result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
