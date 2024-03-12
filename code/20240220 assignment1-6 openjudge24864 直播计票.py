s = list(map(int, [item for item in input().split(" ") if item != ""]))
cnt = [0] * 100001
for c in s :
    cnt[c] = cnt[c] + 1
MAX = 0
listMax = []
for i in range(100001) :
    if cnt[i] > MAX :
        listMax = []
        MAX = cnt[i]
    if cnt[i] == MAX :
        listMax.append(i)
for i in range(len(listMax)) :
    if i > 0 :
        print(" ", end = "")
    print(listMax[i], end = "")