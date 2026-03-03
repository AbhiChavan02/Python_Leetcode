class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        length = (1 << n) - 1
        mid = (length + 1) // 2
        
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        c = self.findKthBit(n - 1, length - k + 1)
        return '1' if c == '0' else '0'


# Taking input from user
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# Creating object and printing result
obj = Solution()
print("Kth bit is:", obj.findKthBit(n, k))

# 3
# 1
# -> 0