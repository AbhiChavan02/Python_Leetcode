from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        for hour in range(12):
            for minute in range(60):
                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        
        return result


if __name__ == "__main__":
    turnedOn = int(input("Enter number of LEDs turned on: "))
    
    obj = Solution()
    answer = obj.readBinaryWatch(turnedOn)
    
    print("Possible times:")
    for time in answer:
        print(time)


# 1
# -> 0:01
# -> 0:02
# -> 0:04
# -> 0:08
# -> 0:16
# -> 0:32
# -> 1:00
# -> 2:00
# -> 4:00
# -> 8:00