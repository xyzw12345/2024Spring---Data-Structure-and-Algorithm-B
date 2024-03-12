n, a, b = map(int, input().split())
s = list(map(int, input().split()))
l = 0
r = n - 1
ans = 0
ra = a
rb = b
while l <= r :
    if l < r :
        if ra < s[l] :
            ans += 1
            ra = a
        ra -= s[l]
        if rb < s[r] :
            ans += 1
            rb = b
        rb -= s[r]
    else :
        if max(ra, rb) < s[l] :
            ans += 1
    l += 1
    r -= 1
print(ans)