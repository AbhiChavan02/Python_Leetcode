from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff


if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    nums = list(map(int, input("Enter the scores: ").split()))
    k = int(input("Enter k: "))

    sol = Solution()
    print("Minimum difference:", sol.minimumDifference(nums, k))


# 4
# 9 4 1 7
# 2
# -> 2