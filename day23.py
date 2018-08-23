#!/usr/bin/env python3


import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    # My implementation of a binary search tree breadth-first search.
    def levelOrder(self, root):
        queue = [root] if root else []
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)


if __name__ == "__main__":
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root,data)
    myTree.levelOrder(root)
