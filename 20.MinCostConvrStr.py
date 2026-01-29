from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        INF = 10**18
        N = 26

        dist = [[INF] * N for _ in range(N)]
        for i in range(N):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            x = ord(o) - ord('a')
            y = ord(c) - ord('a')
            dist[x][y] = min(dist[x][y], w)

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue

            x = ord(s) - ord('a')
            y = ord(t) - ord('a')

            if dist[x][y] == INF:
                return -1
            
            total_cost += dist[x][y]
        
        return total_cost
    

if __name__ == "__main__":
    source = input("Enter source string: ").strip()
    target = input("Enter target string: ").strip()

    m = int(input("Enter number of conversion rules: "))

    original = []
    changed = []
    cost = []

    print("Enter conversion rules (original changed cost):")
    for _ in range(m):
        o, c, w = input().split()
        original.append(o)
        changed.append(c)
        cost.append(int(w))

    sol = Solution()
    result = sol.minimumCost(source, target, original, changed, cost)

    print("Minimum Cost:", result)


    # abcd
    # acbe
    # 6
    # a b 2
    # b c 5
    # c b 5
    # c e 1
    # e b 2
    # d e 20
    # -> 28
