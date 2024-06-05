while True :
    n = int(input())
    if n == 0 :
        break
    q = [{}]
    q[0][1] = ["1"]
    j = 0
    while 0 not in q[j] :
        q.append({})
        for i in q[j] :
            q[j + 1][(10 * i) % n] = q[j][i] + ["0"]
            q[j + 1][(10 * i + 1) % n] = q[j][i] + ["1"]
        j += 1
    print("".join(c for c in q[j][0]))