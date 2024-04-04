def cal(s1, s2) :
    u = list(map(int, s1.split(":")))
    v = list(map(int, s2.split(":")))
    return v[2] - u[2] + (v[1] - u[1]) * 60 + (v[0] - u[0]) * 3600

N = int(input())
d = dict()
for i in range(N) :
    u = input().split()
    if u[0] in d :
        d[u[0]] = d[u[0]] + cal(u[1], u[2])
    else :
        d[u[0]] = cal(u[1], u[2])
mx = 0
tmp = 0
for item in d :
    if d[item] > mx :
        tmp = item
        mx = d[item]
print(tmp)