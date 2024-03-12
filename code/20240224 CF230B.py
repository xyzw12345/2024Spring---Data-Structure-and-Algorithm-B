import math

isprime = [1] * 1000005
isprime[0] = 0
isprime[1] = 0
for i in range(2, 1000005) :
    if isprime[i] == 1 :
        for j in range(i * i, 1000005, i) :
            isprime[j] = 0
n = int(input())
listNum = list(map(int, input().split()))
for num in listNum :
    u = int(math.sqrt(num))
    if u * u == num and isprime[u] == 1 :
        print("YES")
    else :
        print("NO")