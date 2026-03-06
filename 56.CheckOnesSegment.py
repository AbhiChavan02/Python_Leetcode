class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


# take input from local machine
s = input("Enter binary string: ")

# create object of class
obj = Solution()

# call function and print result
print(obj.checkOnesSegment(s))


# 111110
# -> True

# 110101
# -> False