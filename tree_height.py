# python3

import sys
import threading


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
    file_num = input()
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    if 'a' in file_num:
        print("Invalid file, enter a file without the letter 'a'")
        return
    file_name = "{:02d}".format(int(file_num))
    try:
        with open(f"test/{file_name}", 'r') as f:
            # input values in one variable, separate with space, split these values in an array
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    except FileNotFoundError:
        print("File not found, enter a valid file")
        return
    # call the function and output it's result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
