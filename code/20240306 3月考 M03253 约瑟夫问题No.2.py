while(True) :
    n, p, m = map(int, input().split())
    if n == 0 and m == 0 and p == 0 :
        break
    h = []
    for i in range(p, n + 1) :
        h.append(i)
    for i in range(1, p) :
        h.append(i)
    tot = 0
    flag = False
    while h != [] :
        tot += 1
        x = h[0]
        del(h[0])
        if tot == m :
            if not flag :
                print(x, end="")
            else :
                print(f",{x}", end="")
            flag = True
            tot = 0
        else :
            h.append(x)
    print("")
