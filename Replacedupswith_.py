d = {}
nums = [1,1,1,1,1,2,2,3,3,3,3,4,4,5,6,7]
for i in nums : 
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
nums = []
nums = list(d.keys())
c = 1
for key,value in d.items():
    if value > 1:
        c += 1
        for i in range(value-1):
            nums.append('_')
print('Number:',c,'\nList :',nums)
