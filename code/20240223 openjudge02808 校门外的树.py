s = list(map(int, input().split()))
n = s[0]
m = s[1]
list = [1] * (n + 1)
for i in range(m) :
    s = input().split()
    l = int(s[0])
    r = int(s[1])
    for j in range(l, r + 1) :
        list[j] = 0
ans = 0
for i in range(n + 1):
    ans += list[i]
print(ans)