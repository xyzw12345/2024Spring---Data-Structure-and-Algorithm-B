def isSign(c) :
    if c == "+" or c == "-" or c == "*" or c == "/" :
        return True
    else :
        return False
def isSignOrBracket(c) :
    if isSign(c) or c == "(" or c == ")" :
        return True
    else :
        return False
def SignLevel(c) :
    if isSign(c) : 
        if c == ")" :
            return 10
        if c == "+" or c == "-" :
            return 20
        if c == "*" or c == "/" :
            return 30
        if c == "(" :
            return 40
    return -1

class stack :
    def __init__(self, item) :
        self.item = item
    def top(self) :
        if self.item == [] :
            return None
        else :
            return self.item[len(self.item) - 1]
    def pop(self) :
        if self.item == [] :
            return
        else :
            self.item.pop()
    def getTopAndPop(self) :
        if self.item == [] :
            return None
        else :
            x = self.top()
            self.pop()
            return x
    def isempty(self) :
        if self.item == [] :
            return True
        else :
            return False
    def push(self, elem) :
        self.item.append(elem)
    def size(self) :
        return len(self.item)

class SyntaxTree :
    def __init__(self, left, right, this) :
        self.this = this
        self.left = left
        self.right = right
    def toPrefixExpr(self) :
        c = self.this
        if not isSign(c):
            return c
        else :
            return self.this + " " + self.left.toPrefixExpr() + " " + self.right.toPrefixExpr()
    def toPostfixExpr(self) :
        c = self.this
        if not isSign(c) :
            return c
        else :
            return self.left.toPostfixExpr() + " " + self.right.toPostfixExpr() + " " + self.this
    def eval(self) :
        c = self.this
        if not isSign(c) :
            return float(c)
        x = self.left.eval()
        y = self.right.eval()
        if x == None or y == None :
            return None
        if c == "+" :
            return x + y
        elif c == "-" :
            return x - y
        elif c == "*" :
            return x * y
        elif c == "/" :
            if y == 0 :
                return None
            return x / y

def SplitIntoNum(s) :
    res = []
    tmp = []
    flag = True
    for c in s :
        if c == " " :
            if not flag :
                res.append("".join(str(i) for i in tmp))
                tmp = []
                flag = True
        elif isSignOrBracket(c) :
            if not flag :
                res.append("".join(str(i) for i in tmp))
                tmp = []
                flag = True
            res.append(c)
        else :
            tmp.append(c)
            flag = False
    if not flag :
        res.append("".join(str(i) for i in tmp))
    return res

def PostfixToSyntaxTree(s) : # No brackets in Postfix Exprs
    q = stack([])
    for c in s :
        if isSign(c) :
            if q.size() <= 1 :
                print("failure while converting postfix expression to syntax tree")
                return None
            else :
                y = q.getTopAndPop()
                x = q.getTopAndPop()
                q.push(SyntaxTree(x, y, c))
        else :
            q.push(SyntaxTree(None, None, c))
    return q.top()

def PrefixToSyntaxTree(s) : # No brackets in Prefix Exprs
    q = stack([])
    s.reverse()
    for c in s :
        if isSign(c) :
            if q.size() <= 1 :
                print("failure while converting prefix expression to syntax tree")
                return None
            else :
                x = q.getTopAndPop()
                y = q.getTopAndPop()
                q.push(SyntaxTree(x, y, c))
        else :
            q.push(SyntaxTree(None, None, c))
    return q.top()

def InfixToSyntaxTree(s) : # with brackets in Infix Exprs
    qTree = stack([])
    qSign = stack([])
    for c in s :
        if not isSignOrBracket(c) :
            qTree.push(SyntaxTree(None, None, c))
        elif c == "(" :
            qSign.push(c)
        elif c != ")" :
            while (not qSign.isempty()) and SignLevel(qSign.top()) >= SignLevel(c) :
                c1 = qSign.getTopAndPop()
                if qTree.size() <= 1 :
                    print("failure while converting infix expression to syntax tree") 
                    return None
                y = qTree.getTopAndPop()
                x = qTree.getTopAndPop()
                qTree.push(SyntaxTree(x, y, c1))
                # print(qTree.top().toPostfixExpr())
            qSign.push(c)
        else :
            while (not qSign.isempty()) and qSign.top() != "(" :
                c1 = qSign.getTopAndPop()
                if qTree.size() <= 1 :
                    print("failure while converting infix expression to syntax tree") 
                    return None
                y = qTree.getTopAndPop()
                x = qTree.getTopAndPop()
                qTree.push(SyntaxTree(x, y, c1))
                # print(qTree.top().toPostfixExpr())
            if qSign.isempty() :
                print("failure while converting infix expression to syntax tree") 
                return None
            qSign.pop()
        # print(qSign.item)
    while not qSign.isempty():
        c1 = qSign.getTopAndPop()
        if qTree.size() <= 1 :
            print("failure while converting infix expression to syntax tree") 
            return None
        y = qTree.getTopAndPop()
        x = qTree.getTopAndPop()
        qTree.push(SyntaxTree(x, y, c1))
        # print(qTree.top().toPostfixExpr())
    return qTree.top()

def bitcnt(k) :
    if k == 0 :
        return 0
    if k % 2 == 0 :
        return bitcnt(k // 2)
    return bitcnt(k // 2) + 1
s = list(map(float, input().split()))
target = float(input())
n = len(s)
L = []
for i in range(1 << n) :
    L.append(set())
for i in range(n) :
    L[(1 << i)].add(str(s[i]))
for i in range(n) :
    for j in range(1 << n) :
        k = j
        while k > 0 :
            if bitcnt(k) != i and bitcnt(j - k) == i :
                k = (k - 1) & j
                continue
            else :
                for u1 in L[k] :
                    for v1 in L[j - k] :
                        u = PostfixToSyntaxTree(SplitIntoNum(u1))
                        v = PostfixToSyntaxTree(SplitIntoNum(v1))
                        x = u.eval()
                        y = v.eval()
                        L[j].add(SyntaxTree(u, v, "+").toPostfixExpr())
                        L[j].add(SyntaxTree(u, v, "*").toPostfixExpr())
                        L[j].add(SyntaxTree(u, v, "-").toPostfixExpr())
                        L[j].add(SyntaxTree(v, u, "-").toPostfixExpr())
                        if x != 0 :
                            L[j].add(SyntaxTree(v, u, "/").toPostfixExpr())
                        if y != 0 :
                            L[j].add(SyntaxTree(u, v, "/").toPostfixExpr())
                k = (k - 1) & j
        print(i, j)
flag = False
eps = 10**(-7)
Ans = set()
for u1 in L[(1 << n) - 1] :
    u = PostfixToSyntaxTree(SplitIntoNum(u1))
    if - eps < u.eval() - target and u.eval() - target < eps:
        Ans.add(u.toPostfixExpr())
        flag = True
for item in Ans :
    print(item)
if not flag :
    print("NO")
        