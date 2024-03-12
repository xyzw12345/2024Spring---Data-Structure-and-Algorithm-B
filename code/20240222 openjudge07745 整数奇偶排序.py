s = list(map(int, input().split()))
s1 = []
s2 = []
for i in s :
    if i % 2 == 0 :
        s2.append(i)
    else :
        s1.append(i)
print(' '.join(str(item) for item in sorted(s1, reverse = 1) + sorted(s2) ))