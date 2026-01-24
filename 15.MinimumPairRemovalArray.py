from typing import List

def minPairSum(nums: List[int]) -> int:
    nums.sort()
    
    left, right = 0, len(nums) - 1
    max_sum = 0

    while left < right:
        pair_sum = nums[left] + nums[right]
        max_sum = max(max_sum, pair_sum)
        left += 1
        right -= 1

    return max_sum


n = int(input("Enter number of elements (even): "))
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Minimized Maximum Pair Sum:", minPairSum(nums))


# 4
# 3 5 2 3
# -> 7
