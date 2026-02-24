from collections import deque

# Tree Node Definition
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Build tree from level-order list
def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


# Required LeetCode Format
class Solution:
    def sumRootToLeaf(self, root):
        
        def dfs(node, current):
            if not node:
                return 0

            current = (current << 1) | node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


# Main function for local execution
if __name__ == "__main__":
    user_input = input("Enter tree as list (e.g. [1,0,1,0,1,0,1]): ")

    values = user_input.strip()[1:-1].split(',')
    arr = []

    for v in values:
        v = v.strip()
        if v.lower() == "null":
            arr.append(None)
        else:
            arr.append(int(v))

    root = build_tree(arr)

    obj = Solution()
    print("Output:", obj.sumRootToLeaf(root))


    # [1,0,1,0,1,0,1]
    # -> 22