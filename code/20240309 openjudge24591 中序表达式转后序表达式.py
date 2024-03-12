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
        if c == "+" :
            return self.left.eval() + self.right.eval()
        elif c == "-" :
            return self.left.eval() - self.right.eval()
        elif c == "*" :
            return self.left.eval() * self.right.eval()
        elif c == "/" :
            return self.left.eval() / self.right.eval()
        else :
            return float(c)

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

T = int(input())
for Case in range(T) :
    s = input()
    s = SplitIntoNum(s)
    print(InfixToSyntaxTree(s).toPostfixExpr())