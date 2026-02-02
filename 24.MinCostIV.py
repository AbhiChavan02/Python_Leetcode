import bisect
from typing import List
from unittest import result


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        base = nums[0]

        window = []
        chosen_sum = 0

        def add(x):
            nonlocal chosen_sum
            bisect.insort(window, x)
            if len(window) <= k - 1:
                chosen_sum += x
            else:
                if x < window[k - 1]:
                    chosen_sum += x
                    chosen_sum -= window[k - 1]

        def remove(x):
            nonlocal chosen_sum
            idx = bisect.bisect_left(window, x)
            if idx < k - 1:
                chosen_sum -= x
                if len(window) > k - 1:
                    chosen_sum += window[k - 1]
            window.pop(idx)

        for i in range(1, dist + 2):
            add(nums[i])

        ans = base + chosen_sum

        for i in range(dist + 2, n):
            remove(nums[i - dist - 1])
            add(nums[i])
            ans = min(ans, base + chosen_sum)
        
        return ans
    

if __name__ == "__main__":
    nums = list(map(int, input("Enter array Elements (space separated): ").split()))
    k = int(input("Enter k: "))
    dist = int(input("Enter list: "))

    solution = Solution()
    result = solution.minimumCost(nums, k, dist)

    print("Output: ", result)


    # 10 8 18 9
    # 3
    # 1
    # -> 36