s = [0, 1, 1]
for i in range(30) :
    s.append(s[i]+s[i+1]+s[i+2])
n = int(input())
print(s[n])