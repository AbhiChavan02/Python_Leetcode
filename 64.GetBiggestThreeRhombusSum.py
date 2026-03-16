from typing import List

diag = [[0]*51 for _ in range(100)]
antid = [[0]*51 for _ in range(100)]
OFFSET = 50

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        def rhombusSum(i, j, d):
            if d == 0:
                return grid[i][j]

            l, r, u, b = j-d, j+d, i-d, i+d

            i0, i1 = u-j+OFFSET, i-l+OFFSET
            Sum = diag[i0][r+1] - diag[i0][j]
            Sum += diag[i1][j+1] - diag[i1][l]

            j0, j1 = u+j, b+j
            Sum += antid[j0][i] - antid[j0][u+1]
            Sum += antid[j1][b] - antid[j1][i+1]

            return Sum

        m, n = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                i0, j0 = i-j+OFFSET, i+j
                diag[i0][j+1] = diag[i0][j] + x
                antid[j0][i+1] = antid[j0][i] + x

        dM = min(m, n) >> 1
        x = [-1]*3

        for d in range(dM+1):
            for i in range(d, m-d):
                for j in range(d, n-d):
                    y = rhombusSum(i, j, d)

                    if y in x:
                        continue

                    if y > x[0]:
                        x[2] = x[1]
                        x[1] = x[0]
                        x[0] = y
                    elif y > x[1]:
                        x[2] = x[1]
                        x[1] = y
                    elif y > x[2]:
                        x[2] = y

        return [v for v in x if v != -1]


# -------- Input Section --------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter the grid values row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

# -------- Execution --------

sol = Solution()
result = sol.getBiggestThree(grid)

print("Top 3 Rhombus Sums:", result)


# 3
# 3
# 3 4 5
# 1 2 6
# 7 8 9
# -> [19, 9, 8]