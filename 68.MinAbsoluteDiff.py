class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                v = sorted(set(
                    grid[x][y]
                    for x in range(i, i + k)
                    for y in range(j, j + k)
                ))
                if len(v) <= 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = min(v[p+1] - v[p] for p in range(len(v) - 1))

        return ans


# ----------- INPUT PART -----------
print("Enter number of rows and columns (m n):")
m, n = map(int, input().split())

print("Enter the grid row by row:")
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print("Enter k:")
k = int(input())

# ----------- FUNCTION CALL -----------
sol = Solution()
result = sol.minAbsDiff(grid, k)

# ----------- OUTPUT -----------
print("Output:")
for row in result:
    print(*row)


    # 3 3
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 2
    # -> 1 1
    # -> 1 1