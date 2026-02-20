class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        count = 0
        start = 0
        subs = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                subs.append("1" + inner + "0")
                start = i + 1
        
        subs.sort(reverse=True)
        return "".join(subs)


if __name__ == "__main__":
    s = input("Enter special binary string: ")
    sol = Solution()
    result = sol.makeLargestSpecial(s)
    print("Output:", result)


    # 11011000
    # -> 11100100