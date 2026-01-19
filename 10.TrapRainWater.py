from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
        
        return water
    
if __name__ == "__main__":
    user_input = input("Enter the heights separated by spaces (example: 0 1 0 2 1 0 1 3 2 1 2 1): \n")

    height = list(map(int, user_input.strip().split()))
    solution = Solution()
    result = solution.trap(height)
    print("Total trapped rain water: ", result)


    # 0 1 0 2 1 0 1 3 2 1 2 1
    # -> 6
                