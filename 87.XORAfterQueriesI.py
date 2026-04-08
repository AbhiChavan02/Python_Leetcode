from typing import List

class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        res = 0
        for x in nums:
            res ^= x

        return res


nums = list(map(int, input("Enter nums (space separated): ").split()))

q = int(input("Enter number of queries: "))

queries = []
print("Enter queries as: l r k v")

for _ in range(q):
    queries.append(list(map(int, input().split())))

sol = Solution()
result = sol.xorAfterQueries(nums, queries)

print("Result:", result)


# 1 2 3 4 5
# 2
# l r k v
# 0 4 1 2
# 1 3 2 3
# -> 26