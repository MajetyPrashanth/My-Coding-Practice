# create a new array and take input from user
arr = list(map(int,input().split()))

# to store the position in which the next negative number should be placed
j = 0
for i in range(len(arr)):
  if arr[i] < 0:
    # swapping
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    j += 1
print(arr,end = ' ')
