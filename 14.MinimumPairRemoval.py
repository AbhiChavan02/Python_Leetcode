from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_not_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
                return True
            
        operations = 0

        while not is_not_decreasing(nums):
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i

            nums = nums[:index] + [min_sum] + nums[index + 2:]
            operations += 1

        return operations
    
if __name__ == "__main__":
    n = int(input("Enter number of Elements: "))
    nums = list(map(int, input("Enter the Numbers: ").split()))

    solution = Solution()
    result = solution.minimumPairRemoval(nums)

    print("Minimum operations needed: ", result)

    
    # 4
    # 5 2 4 1
    # -> 2