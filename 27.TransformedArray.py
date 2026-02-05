from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0

            else:
                new_index = (i + nums[i]) % n
                result[i] = nums[new_index]

        return result
    
if __name__ == "__main__":
    nums = list(map(int, input("Enter Array elements (space separated): ").split()))
    solution = Solution()
    result = solution.constructTransformedArray(nums)
    print("Transformed Array: ", result)


    # 3 -2 1 1
    # -> [1, 1, 1, 3]

    # -1 4 -1
    # -> [-1, -1, 4]