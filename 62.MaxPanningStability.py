class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

        self.components -= 1
        return True


class Solution:
    def canAchieve(self, n, edges, k, x):
        dsu = DSU(n)

        for u, v, s, must in edges:
            if must == 1:
                if s < x:
                    return False
                if not dsu.unite(u, v):
                    return False

        for u, v, s, must in edges:
            if must == 0 and s >= x:
                dsu.unite(u, v)

        used_upgrades = 0

        for u, v, s, must in edges:
            if must == 0 and s < x and 2 * s >= x:
                if dsu.unite(u, v):
                    used_upgrades += 1
                    if used_upgrades > k:
                        return False

        return dsu.components == 1

    def maxStability(self, n, edges, k):
        dsu = DSU(n)

        for u, v, s, must in edges:
            if must == 1:
                if not dsu.unite(u, v):
                    return -1

        low, high = 1, 200000
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if self.canAchieve(n, edges, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


# --------- Input Section ---------

n, m, k = map(int, input("Enter n m k: ").split())

edges = []
print("Enter edges (u v s must):")

for _ in range(m):
    u, v, s, must = map(int, input().split())
    edges.append((u, v, s, must))

sol = Solution()
result = sol.maxStability(n, edges, k)

print("Maximum Stability:", result)


# 4 4 1
# 0 1 5 1
# 1 2 4 0
# 2 3 3 0
# 0 3 6 0
# -> 4