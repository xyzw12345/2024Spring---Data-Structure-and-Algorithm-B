while True :
    try :
        s = input()
        if s == "".join(reversed(s)) :
            print("YES")
        else :
            print("NO")
    except :
        break