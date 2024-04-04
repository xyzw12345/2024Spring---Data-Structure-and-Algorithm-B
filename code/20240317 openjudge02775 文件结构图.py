h = []

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

class dir :
    def __init__(self, files, dirs, val) :
        self.files = files
        self.dirs = dirs
        self.val = val
    def addfile(self, val) :
        self.files.append(val)
        self.files = sorted(self.files)
    def adddir(self, val) :
        self.dirs.append(val)
    def ToStr(self) :
        res = [self.val]
        for dir in self.dirs :
            res += ["|     " + this for this in dir.ToStr()]
        for file in self.files :
            res.append(file)
        return res

def work() :
    global h
    stackDir = stack([dir([], [], "ROOT")])
    for item in h :
        if item[0] == "f" :
            u = stackDir.getTopAndPop()
            u.addfile(item)
            stackDir.push(u)
        if item[0] == "d" :
            stackDir.push(dir([], [], item))
        if item[0] == "]" :
            u = stackDir.getTopAndPop()
            v = stackDir.getTopAndPop()
            v.adddir(u)
            stackDir.push(v)
    for i in stackDir.top().ToStr() :
        print(i)




Case = 1
while True :
    s = input()
    if s == "*" :
        print(f"DATA SET {Case}:")
        work()
        Case += 1
        print("")
        h = []
    if s == "#" :
        break
    h.append(s)