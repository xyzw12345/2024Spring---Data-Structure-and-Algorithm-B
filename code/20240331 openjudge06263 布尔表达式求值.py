while True :
    try :
        s = input()
        s = s.replace("!", "not ")
        s = s.replace("|", " or ")
        s = s.replace("&", " and ")
        s = s.replace("V", "(True)")
        s = s.replace("F", "(False)")
        #print(s)
        print("V" if eval(s) else "F")
    except :
        break