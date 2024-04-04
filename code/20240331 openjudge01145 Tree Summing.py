#NOTICE THAT NEGATIVE NUMBERS MAY APPEAR!

u = 0
flag = True
class Node :
    def __init__(self, val, left, right) :
        self.val = val
        self.left = left
        self.right = right
    def have_sum(self, u) :
        if self.left == None and self.right == None :
            return (self.val == u)
        x = False if self.left == None else self.left.have_sum(u - self.val)
        y = False if self.right == None else self.right.have_sum(u - self.val)
        return (x or y)
node = None
qval = []
qnode = []
def continue_parsing(s) :
    global qval, qnode, node, flag
    neg = 1
    flag = False
    for i in range(len(s)) :
        if s[i] == ' ' :
            continue
        if s[i] == '(' :
            qval.append(s[i])
        elif s[i] == '-' :
            neg = -neg
        elif s[i] == ')' :
            c = qval[-1]
            qval.pop()
            if c == '(' :
                qnode.append(None)
            else :
                qnode[-2] = Node(c, qnode[-2], qnode[-1])
                qnode.pop()
                qval.pop()
        else :
            if i >= 0 and s[i - 1].isdigit() :
                continue
            j = i + 1
            while j < len(s) and s[j].isdigit() :
                j += 1
            qval.append(neg * int(s[i : j]))
            neg = 1
    if len(qval) == 0 and len(qnode) == 1:
        node = qnode[0]
        flag = True
        return
    else :
        return

def clear() :
    global qnode, qval, node
    qnode = []
    qval = []
    node = None

while True :
    try :
        s = input()
    except :
        break
    if flag == False :
        continue_parsing(s)
    else :
        s = s.split()
        u = int(s[0])
        clear()
        continue_parsing("".join(item for item in s[1 : len(s)]))
    if flag :
        print("yes" if node and node.have_sum(u) else "no")

