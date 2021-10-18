print('Enter the elements of the array : ')
a1 = list(map(int,input().split()))
maxi = 0
mini = 9999
for i in range(len(a1)):
    if a1[i] < mini:
        mini = a1[i]
    elif a1[i] > maxi:
        maxi = a1[i]
print('Maximum element in array is : ',maxi)
print('Minimum element in array is : ',mini)
