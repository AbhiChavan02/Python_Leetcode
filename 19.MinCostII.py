import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        ptr = [0] * (k + 1)

        pq = [(0, 0, 0, 0)]

        while pq:
            cost, r, c, t = heapq.heappop(pq)

            if cost > dist[r][c][t]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            # Normal moves
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < dist[nr][nc][t]:
                        dist[nr][nc][t] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, t))

            # Teleport
            if t < k:
                while ptr[t] < len(cells) and cells[ptr[t]][0] <= grid[r][c]:
                    _, x, y = cells[ptr[t]]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    ptr[t] += 1

        return -1


if __name__ == "__main__":
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))

    grid = []
    print("Enter grid rows (space separated):")
    for i in range(m):
        grid.append(list(map(int, input(f"Row {i + 1}: ").split())))

    k = int(input("Enter number of teleports (k): "))

    sol = Solution()
    ans = sol.minCost(grid, k)
    print("Minimum cost:", ans)


    # 3
    # 3
    # 1 3 3
    # 2 5 4
    # 4 3 5
    # 2
    # -> 7