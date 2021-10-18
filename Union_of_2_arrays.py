print('Enter the elements of first array : ')
a1 = list(map(int,input().split()))
print('\nEnter the elements of first array : ')
a2 = list(map(int,input().split()))
for i in range(len(a2)):
    a1.append(a2[i])
print('\nUNION OF 2 ARRAYS IS : ')
print(a1, end = ' ')
