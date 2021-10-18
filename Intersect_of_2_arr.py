print('Enter the elements of first array : ')
a1 = list(map(int,input().split()))
print('\nEnter the elements of first array : ')
a2 = list(map(int,input().split()))
a3 = []
for i in range(len(a1)):
    if a1[i] in a2:
        a3.append(a1[i])
print('\nINTERSECTION OF 2 ARRAYS IS : ')
print(a3, end = ' ')
