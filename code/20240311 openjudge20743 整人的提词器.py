class stack :
    def __init__(self, item) :
        self.item = item
    def pop(self) :
        if self.item != [] :
            self.item.pop()
    def push(self, x) :
        self.item.append(x)
    def isempty(self) :
        return self.item == []
    def size(self) :
        return len(self.item)
    def top(self) :
        if self.item == [] :
            return None
        return self.item[len(self.item) - 1]
    def getTopAndPop(self) :
        if self.item == [] :
            return None
        x = self.item[len(self.item) - 1]
        self.item.pop()
        return x
    def __str__(self) :
        return str(self.item)

s = input()
h = stack([])
for item in s :
    #print(item)
    if item == ")" :
        tmp = []
        while h.top() != "(" :
            tmp.append(h.getTopAndPop())
        h.pop()
        for i in tmp :
            h.push(i)
    else :
        h.push(item)
    #print("".join(i for i in h.item))
print("".join(i for i in h.item))