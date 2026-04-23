from collections import defaultdict

class Solution:
    def distance(self, nums):
        n = len(nums)
        groups = defaultdict(list)

        for i, v in enumerate(nums):
            groups[v].append(i)

        res = [0] * n

        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)

            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx

        return res


nums = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
result = sol.distance(nums)
print("Output:", result)

# 1 3 1 1 2
# -> [5, 0, 3, 4, 0]