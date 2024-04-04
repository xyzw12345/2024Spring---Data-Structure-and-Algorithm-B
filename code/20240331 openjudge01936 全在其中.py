while True :
    try :
        s, t = input().split()
        tot = 0
        for i in t :
            if tot < len(s) and s[tot] == i :
                tot += 1
        if tot == len(s) :
            print("Yes")
        else :
            print("No")
    except :
        break