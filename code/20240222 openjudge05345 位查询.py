MOD1 = 65536
listAns = [] # listAns[i][j] 表示前缀和MOD2^(i+1)余j时查询i得到的结果
cnt = [0] * 65536
Sumcnt = [0] * 65536
def getSum(l, r) :
    global Sumcnt
    if l >= 65536 :
        return getSum(l - 65536, r - 65536)
    if r >= 65536 :
        return getSum(l, 65535) + getSum(0, r - 65536)
    if l > 0 :
        return Sumcnt[r] - Sumcnt[l - 1]
    if l == 0 :
        return Sumcnt[r]

for i in range(16) :
    listAns.append([])
s = list(map(int, input().split()))
n = s[0]
m = s[1]
a = list(map(int, input().split()))
tot = 0
for i in range(16) :
    listAns[i] = [0] * (1 << (i + 1))
for num in a :
    cnt[num % MOD1] += 1
Sumcnt[0] = cnt[0]
for i in range(1, 65536) :
    Sumcnt[i] = Sumcnt[i - 1] + cnt[i]
for i in range(16) :
    for j in range(1 << (i + 1)) :
        for k in range(j, 65536 + j, (1 << (i + 1))) :
            listAns[i][j] += getSum(k + (1 << i), k + (1 << (i + 1)) - 1)
while m >= 1 :
    m -= 1
    u = input().split()
    x = int(u[1])
    if u[0] == 'C' :
        tot = (MOD1 + tot - x % MOD1) % MOD1
    if u[0] == 'Q' :
        print(listAns[x][tot % (1 << (x + 1))])
    
