from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(vals[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(vals) - 1)


# -------- helper to build tree from input --------
def build_tree(data):
    if not data or data[0] == "null":
        return None

    root = TreeNode(int(data[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        node = queue.popleft()

        if i < len(data) and data[i] != "null":
            node.left = TreeNode(int(data[i]))
            queue.append(node.left)
        i += 1

        if i < len(data) and data[i] != "null":
            node.right = TreeNode(int(data[i]))
            queue.append(node.right)
        i += 1

    return root


# -------- helper to print tree (level order) --------
def print_tree(root):
    if not root:
        print([])
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # remove trailing nulls
    while result and result[-1] is None:
        result.pop()

    print(result)


# -------- main --------
user_input = input("Enter tree nodes (comma separated, use null): ")
data = user_input.split(",")

root = build_tree(data)
sol = Solution()
balanced_root = sol.balanceBST(root)

print("Balanced BST (level order):")
print_tree(balanced_root)



# 1,null,2,null,3,null,4
# -> [2, 1, 3, None, None, None, 4]