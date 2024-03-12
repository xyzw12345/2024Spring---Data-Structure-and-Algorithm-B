class queue :
    def __init__(self, item) :
        self.item = item
    def front(self) :
        return self.item[0]
    def pop(self) :
        del(self.item[0])
    def push(self, val) :
        self.item.append(val)
    def isempty(self) :
        return self == []
    def length(self) :
        return len(self.item)

while(True) :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break
    else :
        s = []
        for i in range(1, n + 1) :
            s.append(i)
        h = queue(s)
        tot = 0
        while h.length() > 1 :
            x = h.front()
            h.pop()
            tot += 1
            if tot == m :
                tot = 0
            else :
                h.push(x)
        print(h.front())
        
        
