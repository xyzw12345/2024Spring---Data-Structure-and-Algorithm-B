while(True) :
    try:
        s = input()
        if s == "" :
            break
        res = [' '] * len(s)
        Lbracket = []
        print(s)
        for i in range(len(s)) :
            if s[i] == "(" :
                Lbracket.append(i)
            if s[i] == ")" :
                if Lbracket != [] :
                    del(Lbracket[len(Lbracket) - 1])
                else :
                    res[i] = '?'
        for i in Lbracket :
            res[i] = '$'
        for i in res :
            print(i, end = "")
        print("") 
    except :
        break