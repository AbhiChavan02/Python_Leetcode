from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        n = len(source)

        strings = set(original) | set(changed)
        idx = {s: i for i, s in enumerate(strings)}
        m = len(idx)

        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # ---------- Step 2: DP ----------
        dp = [INF] * (n + 1)
        dp[n] = 0

        lengths = set(len(s) for s in strings)

        for i in range(n - 1, -1, -1):

            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for L in lengths:
                j = i + L - 1
                if j >= n:
                    continue

                s = source[i:j + 1]
                t = target[i:j + 1]

                if s in idx and t in idx:
                    c = dist[idx[s]][idx[t]]
                    if c < INF:
                        dp[i] = min(dp[i], c + dp[j + 1])

        return -1 if dp[0] == INF else dp[0]


if __name__ == "__main__":
    source = input("Enter source: ").strip()
    target = input("Enter target: ").strip()

    m = int(input("Enter number of operations: "))

    original = []
    changed = []
    cost = []

    print("Enter original changed cost:")
    for _ in range(m):
        o, c, w = input().split()
        original.append(o)
        changed.append(c)
        cost.append(int(w))

    sol = Solution()
    ans = sol.minimumCost(source, target, original, changed, cost)

    print("Output:", ans)


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
