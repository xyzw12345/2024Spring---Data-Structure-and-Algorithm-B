def Median(s) :
    s1 = sorted(s)
    n = len(s)
    if n % 2 == 0 :
        return (s1[n//2 - 1] + s1[n//2]) / 2
    else :
        return s1[(n - 1)//2]

n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [sum(map(int, i.split(','))) for i in pairs]
prices = list(map(int, input().split()))
ratio = [distances[i] / prices[i] for i in range(n)]
price_m = Median(prices)
ratio_m = Median(ratio)
res = 0
for i in range(n) :
    if prices[i] < price_m and ratio[i] > ratio_m :
        res += 1
print(res)
