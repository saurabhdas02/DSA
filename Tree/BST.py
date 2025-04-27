import copy
from collections import deque


class Node:

    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = None
        self.right = None


def insertInBST(root_node, node):
    if root_node.key < node.key:
        if root_node.right is None:
            root_node.right = node
        else:
            insertInBST(root_node.right, node)
    elif root_node.key > node.key:
        if root_node.left is None:
            root_node.left = node
        else:
            insertInBST(root_node.left, node)


class SortedArrayToBST:
    def helper(self, i, j, arr):
        if i > j:
            return None
        mid = (i + j) // 2

        node = Node(arr[mid])
        node.left = self.helper(i, mid - 1, arr)
        node.right = self.helper(mid + 1, j, arr)

        return node

    def sortedArrayToBST(self, nums):
        return self.helper(0, len(nums) - 1, nums)


def sortedArrayToBST(arr, i, j):
    if i > j:
        return None
    mid = (i + j) // 2

