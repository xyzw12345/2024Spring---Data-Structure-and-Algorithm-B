m, n = map(int, input().split())
s = list(map(int, input().split()))
mem = []
res = 0 
for item in s :
    #print(mem)
    if not item in mem :
        res += 1
        mem.append(item)
        if len(mem) > m :
            mem.pop(0)
print(res)