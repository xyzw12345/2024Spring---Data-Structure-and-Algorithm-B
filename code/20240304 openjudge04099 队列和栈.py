m = int(input())
for Case in range(m) :
    n = int(input())
    s1 = []
    s2 = []
    flag = True
    for i in range(n) :
        u = input().split()
        if u[0] == "push" :
            x = int(u[1])
            s1.append(x)
            s2.append(x)
        else :
            if len(s1) == 0 or len(s2) == 0 :
                flag = False
                continue
            else :
                del(s1[0])
                del(s2[len(s2) - 1])
    if flag :
        for i in s1 :
            print(i, end = " ")
        print("")
        for i in s2 :
            print(i, end = " ")
        print("")
    else :
        print("error")
        print("error")