import heapq
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

        return -1 if dist[n - 1] == INF else dist[n - 1]
    
if __name__ == "__main__":
    n = int(input("Enter number of nodes: "))
    m = int(input("Enter number of edges: "))

    edges = []
    for i in range(m):
        u, v, w = map(int, input(f"Enter edge {i + 1} (u v w): ").split())
        edges.append([u, v, w])

    solution = Solution()
    print("Minimum Cost: ", solution.minCost(n, edges))


    # 3
    # 3
    # 2 1 1
    # 1 0 1
    # 2 0 16
    # -> 4