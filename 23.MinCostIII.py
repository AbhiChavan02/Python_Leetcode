from typing import List
from unittest import result


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        rest = nums[1:]
        rest.sort()
        return first + rest[0] + rest[1]
    
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter array elements separated by space: ").split()))

    solution = Solution()
    result = solution.minimumCost(nums)

    print("Minimum Cost: ", result)


    # 4
    # 10 3 1 1
    # -> 12