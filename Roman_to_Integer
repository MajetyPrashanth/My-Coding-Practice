class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000} 
        str1 = s
        sum1 = 0
        for i in range (0,len(str1)-1):
            if rom[str1[i]]<rom[str1[i+1]]:
                sum1 -= rom[str1[i]]
            else:
                sum1 += rom[str1[i]]
        return sum1 + rom[str1[-1]]
