class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2147483647 or x <=  -2147483648 or x ==0 :
            return 0
        elif x > 0 and x < 2147483647:
            str1 = str(x)
            y = str1[::-1]
            num = int(y)
            if num >= 2147483647 or num <=  -2147483648 or x ==0 :
                return 0
            else:
                return num
        elif x < 0 and x >= -2147483648:
            temp = abs(x)
            str1 = str(temp)
            y = str1[::-1]
            temp1 = int(y)
            num = 0-temp1
            if num >= 2147483647 or num <=  -2147483648 or x ==0 :
                return 0
            else:
                return num
