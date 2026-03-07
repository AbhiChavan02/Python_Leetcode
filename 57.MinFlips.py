class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        ans = n
        mis0 = 0

        for i in range(2 * n):

            expected0 = '0' if i % 2 == 0 else '1'

            if t[i] != expected0:
                mis0 += 1

            if i >= n:
                left = i - n
                exp_left = '0' if left % 2 == 0 else '1'
                if t[left] != exp_left:
                    mis0 -= 1

            if i >= n - 1:
                mis1 = n - mis0
                ans = min(ans, min(mis0, mis1))

        return ans


# Taking input from user
s = input("Enter binary string: ")

# Creating object and calling function
obj = Solution()
result = obj.minFlips(s)

# Printing result
print("Minimum flips:", result)


# 111000
# -> 2