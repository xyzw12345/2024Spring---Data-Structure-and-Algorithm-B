n, k = map(int, input().split())
val = list(map(int, input().split()))
h = []
head = 0
for i in range(k) :
    while head < len(h) and val[h[len(h) - 1]] <= val[i] :
        h.pop()
    h.append(i)
print(val[h[head]], end = "")
for i in range(k, n) :
    while head < len(h) and val[h[len(h) - 1]] <= val[i] :
        h.pop()
    h.append(i)
    while head < len(h) and h[head] <= i - k :
        head += 1
    print(f" {val[h[head]]}", end = "")
