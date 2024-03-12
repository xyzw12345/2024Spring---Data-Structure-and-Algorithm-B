def isPrime(n) :
    i = 2
    while i * i <= n :
        if n % i == 0 :
            return 0
        i = i + 1
    return 1

n = int(input())
i = 1
while i <= n / 2 :
    if isPrime(i) == 1 and isPrime(n - i) == 1 :
        print(f"{i} {n - i}")
        break
    i = i + 1