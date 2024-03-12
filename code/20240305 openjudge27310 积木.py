import itertools
perm4 = itertools.permutations([0, 1, 2, 3])
Opt = []
for j1 in range(7) :
    for j2 in range(7) :
        for j3 in range(7) :
            for j4 in range(7) :
                Opt.append([j1, j2, j3, j4])
N = int(input())
Inpt = []
for i in range(4) :
    Inpt.append([])
    s = input()
    for j in range(6) :
        Inpt[i].append(s[j])
    Inpt[i].append("")
Allwords = set()
for perm in perm4 :
    for opt in Opt :
        Allwords.add("".join(Inpt[perm[j]][opt[j]] for j in range(4)))
for i in range(N) :
    s = input()
    if s in Allwords :
        print("YES")
    else :
        print("NO")