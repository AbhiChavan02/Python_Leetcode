from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2


nums = list(map(int, input("Enter numbers separated by space: ").split()))

obj = Solution()
result = obj.minimumDistance(nums)

print("Output:", result)


# 1 2 1 3 1
# -> 4