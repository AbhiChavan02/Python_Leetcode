from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                res = min(res, abs(i - start))
        return res


nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target value: "))
start = int(input("Enter start index: "))
sol = Solution()
result = sol.getMinDistance(nums, target, start)
print("Minimum Distance:", result)

# 1 2 3 4 5
# 5
# 3
# -> 1