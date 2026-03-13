import math

class Solution:
    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
        lo, hi = 1, 10**16

        while lo < hi:
            mid = (lo + hi) >> 1
            tot = 0
            for t in times:
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if tot >= height:
                    break

            if tot >= height:
                hi = mid
            else:
                lo = mid + 1

        return lo


# ---- Local Machine Input ----
height = int(input("Enter height: "))
times = list(map(int, input("Enter times separated by space: ").split()))

sol = Solution()
result = sol.minNumberOfSeconds(height, times)

print("Minimum seconds:", result)


# 10
# 1 2 3
# -> 15