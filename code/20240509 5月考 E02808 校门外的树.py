L, M = map(int, input().split())
T = [1] * (L + 1)
for i in range(M) :
    u, v = map(int, input().split())
    for j in range(u, v + 1) :
        T[j] = 0
print(sum(T))