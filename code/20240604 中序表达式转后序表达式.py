precedence = {"+" : 10, "-" : 10, "*" : 20, "/" : 20, "(" : 0}
ToNum = lambda x : str(x)
Calc = {"+" : (lambda x, y : x + y),
        "-" : (lambda x, y : x - y),
        "*" : (lambda x, y : x * y),
        "/" : (lambda x, y : x / y)}
NumberOfOpr = {i : 2 for i in "+-*/"}
Val = "1234567890."
Opr = "+-*/"
class SyntaxTree :
    def __init__ (self, val, left = None, right = None):
        self.val = val # in the form of a string
        self.left = left
        self.right = right
    def ToExpr(self, mode = "infix"):
        lexpr = "" if not self.left else self.left.ToExpr(mode)
        rexpr = "" if not self.right else self.right.ToExpr(mode)
        if mode == "prefix" :
            return self.val + ("" if not self.left else (" " + lexpr)) + ("" if not self.right else (" " + rexpr))
        elif mode == "postfix" :
            return ("" if not self.left else (lexpr + " ")) + ("" if not self.right else (rexpr + " ")) + self.val
        else :
            if self.right and (self.right.val in precedence) and precedence[self.right.val] <= precedence[self.val]:
                rexpr = ("(" + rexpr + ")")
            if self.left and (self.left.val in precedence) and precedence[self.left.val] < precedence[self.val]:
                lexpr = ("(" + lexpr + ")")
            return ("" if not self.left else (lexpr + " ")) + self.val + ("" if not self.right else (" " + rexpr))
    def Eval(self):
        if self.val not in precedence:
            return ToNum(self.val)
        else:
            if not self.left:
                return Calc[self.val](self.right.Eval())
            else:
                return Calc[self.val](self.left.Eval(), self.right.Eval())
    def __str__(self):
        return self.ToExpr("prefix")

def InfixToSyntax(s):
    output_stack = []
    opr_stack = []
    tmp = ""
    for char in s:
        #print(tmp, opr_stack)
        #print(" ".join(str(i) for i in output_stack))
        if char in Val:
            tmp += char
        else:
            if tmp:
                output_stack.append(SyntaxTree(tmp))
                tmp = ""
            if char in Opr:
                while opr_stack and precedence[opr_stack[-1]] >= precedence[char]:
                    opr = opr_stack.pop()
                    if NumberOfOpr[opr] == 1 :
                        x = output_stack.pop()
                        output_stack.append(SyntaxTree(opr, None, x))
                    else:
                        y = output_stack.pop()
                        x = output_stack.pop()
                        output_stack.append(SyntaxTree(opr, x, y))
                opr_stack.append(char)
            elif char == "(":
                opr_stack.append(char)
            elif char == ")":
                while opr_stack and opr_stack[-1] != "(":
                    opr = opr_stack.pop()
                    if NumberOfOpr[opr] == 1 :
                        x = output_stack.pop()
                        output_stack.append(SyntaxTree(opr, None, x))
                    else:
                        y = output_stack.pop()
                        x = output_stack.pop()
                        output_stack.append(SyntaxTree(opr, x, y))
                opr_stack.pop()
    if tmp:
        output_stack.append(SyntaxTree(tmp))
    #print(tmp, opr_stack)
    #print(" ".join(str(i) for i in output_stack))
    while opr_stack:
        opr = opr_stack.pop()
        if NumberOfOpr[opr] == 1 :
            x = output_stack.pop()
            output_stack.append(SyntaxTree(opr, None, x))
        else:
            y = output_stack.pop()
            x = output_stack.pop()
            output_stack.append(SyntaxTree(opr, x, y))
    return output_stack.pop()

T = int(input())
for Case in range(T) :
    s = input()
    print(InfixToSyntax(s).ToExpr("postfix"))

    
                