T = int(input())
for Case in range(T) :
    n = int(input())
    i = 1
    while i <= n :
        i = i << 1
    print(int(n * (n + 1) / 2 - 2 * (i - 1)))