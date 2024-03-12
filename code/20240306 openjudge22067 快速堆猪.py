h = []
while True :
    try :
        s = input().split()
        if s[0] == "min" :
            if h != [] :
                print(h[len(h) - 1])
        if s[0] == "push" :
            x = int(s[1])
            if h != [] :
                x = min(x, h[len(h) - 1])
            h.append(x)
        if s[0] == "pop" :
            if h != [] :
                h.pop()
    except :
        break