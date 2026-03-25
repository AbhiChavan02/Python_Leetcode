from itertools import accumulate, chain

class Solution:
    def canPartitionGrid(self, g):
        return sum(chain(*g)) / 2 in chain(*(accumulate(map(sum, g)) for g in (g, zip(*g))))

# ---- Input Section ----
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

print("Enter the grid values row by row:")

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# ---- Function Call ----
obj = Solution()
result = obj.canPartitionGrid(grid)

# ---- Output ----
print("Can partition grid:", result)

# 2
# 2
# 1 1
# 1 1
# -> True