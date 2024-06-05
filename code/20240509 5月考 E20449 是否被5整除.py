A = input()
res = []
tmp = 0
for a in A :
    tmp = (2 * tmp + ord(a) - ord('0')) % 5
    res.append(1 if tmp == 0 else 0)
print("".join(str(a) for a in res))