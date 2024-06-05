from collections import Counter
from itertools import product
n = int(input())
A = []
B = []
C = []
D = []
for i in range(n) :
    u = list(map(int, input().split()))
    A.append(u[0])
    B.append(u[1])
    C.append(u[2])
    D.append(u[3])
A = sorted(A)
B = sorted(B)
C = sorted(C)
D = sorted(D)
res = 0
AB = Counter(map(lambda x : x[0] + x[1], product(A, B)))
for c in C :
    for d in D :
        res += AB.get(-c - d, 0)
print(res)