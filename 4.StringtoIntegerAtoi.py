class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])

            if sign * num <= INT_MIN:
                return INT_MIN
            if sign * num >= INT_MAX:
                return INT_MAX
            
            i += 1

        return sign * num
    
if __name__ == "__main__":
    user_input = input("Enter a String: ")
    solution = Solution()
    result = solution.myAtoi(user_input)
    print("Converted Integer: ", result)