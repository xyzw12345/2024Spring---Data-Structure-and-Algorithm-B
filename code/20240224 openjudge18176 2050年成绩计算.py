import math

isprime = [1] * 20005
isprime[0] = 0
isprime[1] = 0
for i in range(2, 20005) :
    if isprime[i] :
        for j in range(i * i, 20005, i) :
            isprime[j] = 0
s = input().split()
m = int(s[0])
tot = 0
cnt = 0
for i in range(m) :
    s = input().split()
    tot = 0
    cnt = 0
    flag = 0
    for item in s :
        u = int(item)
        v = int(math.sqrt(u))
        if v * v == u and isprime[v] == 1 :
            tot += u
            flag = 1
        cnt += 1
    if flag == 0 :
        print(0)
    else :
        print(f"{tot / cnt :.2f}")