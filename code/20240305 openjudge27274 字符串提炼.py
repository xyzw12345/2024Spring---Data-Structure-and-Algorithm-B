s = input()
l = len(s)
i = 0
while 1 << (i + 1) <= l :
    i += 1
l = 0
r = i
while l <= r :
    print(s[(1 << l) - 1], end = "")
    if l < r :
        print(s[(1 << r) - 1], end = "")
    l += 1
    r -= 1
    