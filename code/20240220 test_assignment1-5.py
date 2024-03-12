s = input().split("+")
s2 = []
x = 0
y = 0
k = 0
for ss in s :
    s2 = list(map(int, [item for item in ss.split("n^") if item != ""]))
    #print(s2)
    if len(s2) == 1 :
        x = 1
        y = s2[0]
    else :
        x = s2[0]
        y = s2[1]
    if y > k and x > 0 :
        k = y
print(f"n^{k}")