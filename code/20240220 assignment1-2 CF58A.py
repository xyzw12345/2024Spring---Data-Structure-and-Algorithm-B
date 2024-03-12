s1 = "hello"
s = input()
n = -1
for c in s :
    if n < 4 :
        if c == s1[n+1] :
            n = n + 1
if n == 4 :
    print("YES")
else :
    print("NO")