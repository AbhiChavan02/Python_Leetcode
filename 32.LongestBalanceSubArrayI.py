from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            evens = set()
            odds = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    evens.add(nums[j])
                else:
                    odds.add(nums[j])

                if len(evens) == len(odds):
                    ans = max(ans, j - i + 1)

        return ans


# -------- user input --------
nums = list(map(int, input("Enter array elements (space separated): ").split()))

obj = Solution()
print(obj.longestBalanced(nums))


# 1 2 3 2
# -> 3