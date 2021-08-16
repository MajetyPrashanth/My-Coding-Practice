def reverseWord(s):
    str1 = s[::-1]
    return str1
 if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1
