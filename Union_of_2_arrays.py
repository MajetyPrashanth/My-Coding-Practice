print('Enter the elements of first array : ')
a1 = list(map(int,input().split()))
print('\nEnter the elements of first array : ')
a2 = list(map(int,input().split()))
d = {}
for i in range(len(a2)):
    a1.append(a2[i])
for i in range(len(a1)):
    if a1[i] not in d:
        d[a1[i]] = 0
    d[a1[i]] += 1
union = d.keys()
print('\nUNION OF 2 ARRAYS IS : ')
print(union, end = ' ')
