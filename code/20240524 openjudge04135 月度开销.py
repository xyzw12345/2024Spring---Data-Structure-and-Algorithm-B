n, m = map(int, input().split())
s = []
for i in range(n) :
    s.append(int(input()))
def check(M) :
    if M < max(s) :
        return False
    cnt = 1
    tmp = 0
    for i in range(n):
        if tmp + s[i] > M:
            cnt += 1
            tmp = s[i]
        else :
            tmp += s[i]
    return cnt <= m

L, R = 0, sum(s)
while R > L :
    M = (L + R) // 2
    if not check(M):
        L = M + 1
    else :
        R = M
print(L)