class BinHeap : # the top of the heap is the smallest 
    def __init__(self) :
        self.item = [0]
        self.size = 0
    def percUp(self, i) :
        if i == 1 :
            return 
        if self.item[i] < self.item[i // 2] :
            self.item[i] ^= self.item[i // 2]
            self.item[i // 2] ^= self.item[i]
            self.item[i] ^= self.item[i // 2]
            self.percUp(i // 2)
    def insert(self, x) :
        self.item.append(x)
        self.size += 1
        self.percUp(self.size)
    def percDown(self, i) :
        if i * 2 > self.size :
            return 
        u = i * 2
        if 2 * i + 1 <= self.size :
            if self.item[2 * i + 1] < self.item[2 * i] :
                u = 2 * i + 1
        if self.item[u] < self.item[i] :
            self.item[i] ^= self.item[u]
            self.item[u] ^= self.item[i]
            self.item[i] ^= self.item[u]
            self.percDown(u)
    def delTop(self) :
        if self.size == 0 :
            return None
        res = self.item[1]
        self.item[1] = self.item[self.size]
        self.item.pop()
        self.size -= 1
        self.percDown(1)
        return res
    def heapify(self, items) :
        self.item.extend(items)
        self.size = len(self.item) - 1
        i = self.size // 2
        while i >= 1 :
            self.percDown(i)
            i -= 1

q = BinHeap()
n = int(input())
for i in range(n) :
    s = list(map(int, input().split()))
    if s[0] == 1 :
        q.insert(s[1])
    else :
        print(q.delTop())