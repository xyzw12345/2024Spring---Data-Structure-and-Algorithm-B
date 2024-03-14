class node :
    def __init__(self, sons, val) :
        self.sons = sons
        self.val = val
    def ToPostString(self) :
        if self.sons == [] :
            return self.val
        return "".join(son.ToPostString() for son in self.sons) + self.val
    def __str__(self) :
        if self.sons == [] :
            return self.val
        return self.val + "".join(str(son) for son in self.sons)

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
    def __str__(self) :
        return str(list(str(item) for item in self.item ))

def build(s) :
    l = 0
    stackval = stack([])
    stacknode = stack([])
    for l in range(len(s)) :
        if s[l] == "(" :
            stacknode.push("(")
        elif s[l] == ")"  or l == len(s):
            tmp = []
            while(stacknode.top() != "(") :
                tmp.append(stacknode.getTopAndPop())
            stacknode.pop()
            tmp.reverse()
            stacknode.push(node(tmp, stackval.getTopAndPop()))
        elif s[l] == "," :
            continue
        elif l < len(s) - 1 and s[l + 1] == "(" :
            stackval.push(s[l])
        else :
            stacknode.push(node([], s[l]))
        #print(l, stackval, stacknode, sep = " ")
    return stacknode.top()

s = input()
v = build(s)
print(v)
print(v.ToPostString())