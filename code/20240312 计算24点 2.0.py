import itertools
class SyntaxTree :
    def __init__(self, left, right, val) :
        self.val = val
        self.left = left
        self.right = right

def eval1(fun, vals) :
    if fun == None :
        if len(vals) == 0 :
            return None
        return [1, vals[0]]
    s1 = eval1(fun.left, vals)
    if s1 == None :
        return None
    u1 = s1[0]
    v1 = s1[1]
    s2 = eval1(fun.right, vals[u1 : len(vals)])
    if s2 == None :
        return None
    u2 = s2[0]
    v2 = s2[1]
    if fun.val == "+" :
        v = v1 + v2
    elif fun.val == "-" :
        v = v1 - v2
    elif fun.val == "*" :
        v = v1 * v2
    else :
        if v2 == 0 :
            return None
        else :
            v = v1 / v2
    return [u1 + u2, v]

def eval(fun, vals) :
    s = eval1(fun, vals)
    if s == None :
        return None
    return s[1]

def ToPostFixExpr1(fun, vals) :
    if fun == None :
        if vals == [] :
            return None
        return [1, str(vals[0])]
    s1 = ToPostFixExpr1(fun.left, vals)
    if s1 == None :
        return None
    u1 = s1[0]
    v1 = s1[1]
    s2 = ToPostFixExpr1(fun.right, vals[u1 : len(vals)])
    if s2 == None :
        return None
    u2 = s2[0]
    v2 = s2[1]
    return [u1 + u2, v1 + " " + v2 + " " + fun.val]

def ToPostFixExpr(fun, vals) :
    s = ToPostFixExpr1(fun, vals)
    if s == None :
        return None
    return s[1]

signs = ["+", "-", "*", "/"]
fun = []
n = int(input())
fun.append([])
fun.append([None])
for i in range(2, n + 1) :
    fun.append([])
    for sign in signs :
        for j in range(1, i) :
            k = i - j
            for l in fun[j] :
                for r in fun[k] :
                    fun[i].append(SyntaxTree(l, r, sign))
# for Fun in fun[2] :
#     print(ToPostFixExpr(Fun, [1, 1]))
s = list(map(int, input().split()))
target = int(input())
perms = itertools.permutations(s)
eps = 10**(-8)
res = set()
for perm in perms :
    # print(perm)
    for Fun in fun[n] :
        k = eval(Fun, perm)
        if k == None :
            continue
        if -eps < k - target and k - target < eps :
            res.add(ToPostFixExpr(Fun, perm))
if res == set() :
    print("NO")
else :
    for s in res :
        print(s)
