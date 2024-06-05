N = int(input())
h = []
for i in range(N) :
    h.append(int(input()))
qmax = []
qmin = []
nextmin = []
vismin = set()
res = 0
for i in range(N) :
    while qmax and h[qmax[-1]] < h[i]:
        qmax.pop()
    qmax.append(i)
    while qmin and h[qmin[-1]] >= h[i] :
        vismin.remove(qmin[-1])
        qmin.pop()
    qmin.append(i)  # qmin increase 
    vismin.add(i)
    nextmin.append(i)
    #print(qmax, qmin)
    u = 0 if len(qmax) == 1 else qmax[-2]
    l = nextmin[u]
    tmpstack = [u]
    while l not in vismin :
        tmpstack.append(l)
        l = nextmin[l + 1]
    for tmp in tmpstack :
        nextmin[tmp] = l
    res = max(res, i - l + 1 if l != i else 0)   
print(res) 
    


