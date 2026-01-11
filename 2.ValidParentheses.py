class Solution:
    def isValid(self, s:str) -> bool:
        stack = []

        bracket_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if ch in bracket_map:
                top = stack.pop() if stack else '#'
                if bracket_map[ch] != top:
                    return False
            else:
                stack.append(ch)

        return not stack
    
if __name__ == "__main__":
    s = input("Enter parentheses string: ").strip()

    solution = Solution()
    result = solution.isValid(s)

    print("Valid Parentheses: ", result)


    # ([]) = True 
    # ([)) = False