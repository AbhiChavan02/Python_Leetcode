from typing import List


class Solution:
    def minBitwiseArrayII(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
                continue

            cnt = 0
            temp = num
            while temp & 1:
                cnt += 1
                temp >>= 1

            ans.append(num - (1 << (cnt - 1)))

        return ans
    
if __name__ == "__main__":
    n = int(input("Enter number of Elements: "))
    nums = list(map(int, input("Enter the Numbers: ").split()))
    solution = Solution()
    result = solution.minBitwiseArrayII(nums)
    print("Result: ", result)