n = int(input())
s = input()
res = []
for i in range(n) :
    res.append([])
for i in range(len(s)) :
    j = i % (2 * n)
    if j >= n :
        res[2 * n - j - 1].append(s[i])
    else :
        res[j].append(s[i])
print("".join("".join(item for item in res[i]) for i in range(n)))