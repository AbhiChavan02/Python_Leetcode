from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            # rotate 90 degree clockwise
            mat = [list(r) for r in zip(*mat[::-1])]
        return False


# ---- Taking input from user ----

n = int(input("Enter size of matrix (n): "))

print("Enter matrix (mat):")
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

print("Enter target matrix:")
target = []
for _ in range(n):
    row = list(map(int, input().split()))
    target.append(row)


# ---- Calling function ----
sol = Solution()
result = sol.findRotation(mat, target)

# ---- Output ----
print("Output:", result)


# 2
# 1 2
# 3 4
# 3 1
# 4 2
# -> True