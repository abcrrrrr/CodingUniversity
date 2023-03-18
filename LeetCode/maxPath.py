from cmath import inf


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def maxPath(root):
    maxPath = -inf
    def findMaxPath(node):
        if not node:
            return 0
        nonlocal maxPath
        lLength = max(findMaxPath(node.left),0)
        rLength = max(findMaxPath(node.right),0)
        maxPath = max(maxPath, node.val + lLength + rLength)
        return max(node.val + lLength, node.val + rLength)
    findMaxPath(root)
    return maxPath


