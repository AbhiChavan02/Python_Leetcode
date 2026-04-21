from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        sets = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        ans = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                ans += 1

        return ans


n = int(input("Enter size of array: "))

print("Enter source array elements (space separated):")
source = list(map(int, input().split()))

print("Enter target array elements (space separated):")
target = list(map(int, input().split()))

m = int(input("Enter number of allowed swaps: "))

allowedSwaps = []
print("Enter allowed swap pairs (0-based index):")
for _ in range(m):
    a, b = map(int, input().split())
    allowedSwaps.append([a, b])

sol = Solution()
result = sol.minimumHammingDistance(source, target, allowedSwaps)

print("Minimum Hamming Distance:", result)


# 4
# 1 2 3 4
# 2 1 4 5
# 2
# 0 1
# 2 3
# -> 1