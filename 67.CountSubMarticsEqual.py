class Solution:
    def numberOfSubmatrices(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        sumX = [0] * cols
        sumY = [0] * cols
        res = 0

        for i in range(rows):
            rx = 0
            ry = 0
            for j in range(cols):
                if grid[i][j] == 'X':
                    rx += 1
                elif grid[i][j] == 'Y':
                    ry += 1
                
                sumX[j] += rx
                sumY[j] += ry
                
                if sumX[j] > 0 and sumX[j] == sumY[j]:
                    res += 1

        return res


# -------- INPUT PART --------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []
print("Enter grid row by row (only X or Y):")
for _ in range(rows):
    row = list(input().strip())   # Example input: XYXXY
    grid.append(row)

# -------- OUTPUT --------
obj = Solution()
result = obj.numberOfSubmatrices(grid)
print("Answer:", result)


# 2
# 3
# XYX
# YXX
# -> 3