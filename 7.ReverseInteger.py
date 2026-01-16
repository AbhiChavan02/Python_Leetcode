class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10

            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return 0
            
            result = result * 10 + digit
        
        return sign * result
    
if __name__ == "__main__":
    x = int(input("Enter a 32 bit Integer: "))

    solution = Solution()
    result = solution.reverse(x)

    print("Reversed Integer: ", result)