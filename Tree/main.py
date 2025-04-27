import copy
from collections import deque


class Node:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def print_inorder(root_node):
    if root_node is not None:
        print_inorder(root_node.left)
        print(root_node.key)
        print_inorder(root_node.right)


def print_preorder(root_node):
    arr = list()
    if root_node is not None:
        arr.append(root_node.key)
        arr += print_preorder(root_node.left)
        arr += print_preorder(root_node.right)
    return arr


def print_postorder(root_node):
    # print(root_node)
    if root_node is not None:
        print_postorder(root_node.left)
        print_postorder(root_node.right)
        print(root_node.key)


def print_level_order(root_node):
    q = deque()
    q.append(root_node)
    while len(q) > 0:
        curr = q.popleft()
        print(curr.key)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


def return_postorder(root_node):
    if not root_node:
        return []
    return return_postorder(root_node.left) + return_postorder(root_node.right) + [root_node.key]


def height_of_tree(root_node):
    if root_node is None:
        return -1
    else:
        lh = height_of_tree(root_node.left)
        lr = height_of_tree(root_node.right)
        return max(lh, lr) + 1


def size_of_tree(root_node):
    if root_node is None:
        return 0
    else:
        lh = size_of_tree(root_node.left)
        lr = size_of_tree(root_node.right)
        return lh + lr + 1


def print_k_distance(root_node, k):
    if root_node is None:
        return
    if k is 0:
        print(root_node.key, end=" ")
    else:
        print_k_distance(root_node.left, k-1)
        print_k_distance(root_node.right, k - 1)


def compareTree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    # and condition handled above
    # if not tree1 or not tree2:
    #     return False
    if tree1.key != tree2.key:
        return False
    return compareTree(tree1.left, tree2.left) and compareTree(tree1.right, tree2.right)


def buildTree(tree_inorder, tree_postorder):
    if not tree_inorder or not tree_postorder:
        return None
    root_val = tree_postorder.pop()
    root_node = Node(root_val)

    index = tree_inorder.index(root_val)
    root_node.right = buildTree(tree_inorder[index+1:], tree_postorder)
    root_node.left = buildTree(tree_inorder[:index], tree_postorder)

    return root_node


def buildTreePreOrderInorder(tree_preorder, tree_inorder):
    if not tree_inorder or not tree_preorder:
        return None
    root_val = tree_preorder.pop(0)
    root_node = Node(root_val)

    index = tree_inorder.index(root_val)
    root_node.left = buildTree(tree_preorder, tree_inorder[:index])
    root_node.right = buildTree(tree_preorder, tree_inorder[index+1:])

    return root_node


def checkHeightBalancedTree(root_node):
    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        if left_h == -1:
            return -1
        right_h = height(node.right)
        if right_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1
    return height(root_node) != -1


def is_symmetric(root_node):
    def helper(left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return left.key == right.key and helper(left.left, right. right) and helper(left.right, right. left)

    helper(root_node.left, root_node.right)


def invertTree(root_node):
    if not root_node:
        return root_node
    invert_tree_left = invertTree(root_node.left)
    invert_tree_right = invertTree(root_node.right)

    root_node.left = invert_tree_right
    root.right = invert_tree_left
    return root_node


def findTitle(root_node):
    def helper(node, answer):
        if not node:
            return 0
        left_sum = helper(node.left, answer)
        right_sum = helper(node.right, answer)
        answer[0] += abs(left_sum - right_sum)
        return left_sum + right_sum + node.key
    if not root_node:
        return 0
    ans = [0]
    helper(root_node, ans)


def printRightSideView(root_node):
    if not root_node:
        return []
    q = deque([root_node])
    result = []
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:
                result.append(node.key)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


def helper(root_node, level, ans):
    if not root_node:
        return

    if level == len(ans):
        ans.append(root_node.val)

    helper(root_node.right, level + 1, ans)
    helper(root_node.left, level + 1, ans)


def rightSideView(root_node):
    ans = []
    helper(root_node, 0, ans)
    return ans


def IsBSTValid(root_node):
    def bst_helper(node, minimum_val, maximum_val):
        if not node:
            return True
        elif not (minimum_val < node.val < maximum_val):
            return False
        return bst_helper(node.left, minimum_val, node.val) and bst_helper(node.right, node.val, maximum_val)

    return bst_helper(root_node)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(70)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.right.right = Node(60)
root1 = copy.deepcopy(root)
root1.left = Node(100)

print(printRightSideView(root))

# print_inorder(root)
# print("*****" * 20)
# print(print_preorder(root))
# print("*****" * 20)
# print_postorder(root)
# print(return_postorder(root))
# base_tree = Node(10)
# print(height_of_tree(root))
# print_k_distance(root, 2)
# print_level_order(root)
# print(size_of_tree(root))
# print(compareTree(root, root1))
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# print(print_inorder(buildTree(inorder, postorder)))
# print(checkHeightBalancedTree(root))



