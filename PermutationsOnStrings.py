str1 = input("Enter the string: ")
str2 = input("Enter the string to be checked : ")
c = 0
if len(str1) == len(str2):
    for i in str2:
        if i in str1:
            c+=1         
            continue
if c == len(str1):
    print("Yes, String2 is a permutation of String1")
else:
    print("No, String2 is not a permutation of",str1)
