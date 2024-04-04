n, k = map(int, input().split())
s = list(map(int, input().split()))
s.append(1)
s = sorted(s)
if k < n and s[k] == s[k + 1] :
    print("-1")
else :
    print(s[k])