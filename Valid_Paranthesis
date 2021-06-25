
s = '([]{})'
d = {'(': 0 , ')': 0 , '{': 0 , '}': 0 , '[': 0 ,']': 0 }
#To count brackets value
for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
        
#To find the closing bracket
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
#to check for all 0s
if d['('] == 0 and d['['] == 0 and d['{'] == 0 :
    print('True')
else:
    print('False')
