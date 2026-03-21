class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        sc, ec = y, y + k - 1
        sr = x

        for j in range(sc, ec + 1):
            for i in range(k // 2):
                grid[sr + i][j], grid[sr + k - i - 1][j] = grid[sr + k - i - 1][j], grid[sr + i][j]

        return grid


# ----------- INPUT SECTION -----------

# rows and columns
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# grid input
grid = []
print("Enter grid values row-wise:")
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

# submatrix inputs
x = int(input("Enter starting row (x): "))
y = int(input("Enter starting column (y): "))
k = int(input("Enter size of submatrix (k): "))


# ----------- FUNCTION CALL -----------

sol = Solution()
result = sol.reverseSubmatrix(grid, x, y, k)


# ----------- OUTPUT SECTION -----------

print("Updated Grid:")
for row in result:
    print(*row)


# 3
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 0
# 0
# 3
# -> 7 8 9
# -> 4 5 6
# -> 1 2 3