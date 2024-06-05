s = input().split(", ")
u = s[-1]
s.pop()
s.extend(u.split(" & "))
t = []
for item in s :
    u = item.split()
    t.append(u[-1] + ", " + ", ".join(v[0] + "." for v in u[0 : len(u) - 1]))
print(", ".join(item for item in t))