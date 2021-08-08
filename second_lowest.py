name = ['A','D','C','B']
score = [10,20,30,20]
d = dict(zip(name,score))
v = d.values()
second = sorted(list(v))[1]
lst = []
for key,value in d.items():
    if value == second:
        lst.append(key)
second_highest = sorted(lst)
print(second_highest)
