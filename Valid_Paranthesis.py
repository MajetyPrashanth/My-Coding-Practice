
s = '([]{})'
d = {'(': 0 , ')': 0 , '{': 0 , '}': 0 , '[': 0 ,']': 0 }

for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
        

for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == '(':
            if s[j] == ')':
                d[s[i]] -= 1
        elif s[i] == '{':
            if s[j] == '}':
                d[s[i]] -= 1
        elif s[i] == '[':
            if s[j] == ']':
                d[s[i]] -= 1                
print(d)

if d['('] == 0 and d['['] == 0 and d['{'] == 0 :
    print('True')
else:
    print('False')
