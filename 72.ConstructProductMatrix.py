class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p


# ----------- Input / Output Handling -----------

if __name__ == "__main__":
    # Take input
    n, m = map(int, input("Enter rows and columns: ").split())
    
    grid = []
    print("Enter matrix values row-wise:")
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    # Solve
    sol = Solution()
    result = sol.constructProductMatrix(grid)

    # Print output
    print("Result matrix:")
    for row in result:
        print(*row)

    # 2 2
    # 1 2
    # 3 4
    # -> 24 12
    # -> 8 6