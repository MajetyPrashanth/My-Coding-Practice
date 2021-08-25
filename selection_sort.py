print('Enter the list of numbers : ',end='')
user_list = list(map(int,input().split()))
sorted_list = []
for i in range (0,len(user_list)):
    temp = min(user_list)
    sorted_list.append(temp)
    user_list.remove(temp)
print('Sorted list is : ')
print(sorted_list)
