from typing import List
from math import inf

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))

    sol = Solution()
    result = sol.minMirrorPairDistance(nums)

    print("Output:", result)

    # 12 21 13 31
    # -> 1