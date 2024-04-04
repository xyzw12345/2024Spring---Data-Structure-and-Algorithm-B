n = int(input())
res = 1
for i in range(1, n + 1) :
    res *= (n + i)
    res = res // i
res = res // (n + 1)
print(res)
