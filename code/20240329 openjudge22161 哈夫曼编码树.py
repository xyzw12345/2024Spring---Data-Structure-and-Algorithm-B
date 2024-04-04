import heapq

class node :
    def __init__(self, chars, val, left = None, right = None, isleaf = True, char = None) :
        self.chars = chars
        self.val = val
        self.left = left
        self.right = right
        self.isleaf = isleaf
        self.char = char
    def __lt__(self, other) :
        return self.val < other.val or (self.val == other.val and min(self.chars) < min(other.chars)) 
    def merge(self, other) :
        return node(self.chars.union(other.chars), self.val + other.val, self, other, isleaf = False)
    def getcode(self, c) :
        if self.isleaf == True and c == self.char:
            return ""
        if c in self.left.chars :
            return "0" + self.left.getcode(c)
        if c in self.right.chars :
            return "1" + self.right.getcode(c)
    def decode(self, root, u) :
        if self.isleaf :
            return self.char + root.decode(root, u)
        if u == "" :
            return ""
        if u[0] == "0" :
            return self.left.decode(root, u[1 : len(u)])
        else :
            return self.right.decode(root, u[1 : len(u)])
    def encode(self, s) :
        res = ""
        for i in s :
            res = res + self.getcode(i)
        return res

def Huffman(s1) :
    heapq.heapify(s1)
    while len(s1) >= 2 :
        x = heapq.heappop(s1)
        y = heapq.heappop(s1)
        heapq.heappush(s1, x.merge(y))
    return heapq.heappop(s1)


n = int(input())
s1 = []
for i in range(n) :
    u = input().split()
    s1.append(node(set([u[0]]), float(u[1]), char = u[0]))
H = Huffman(s1)
while True :
    try :
        s = input()
        if ord(s[0]) == ord('0') or ord(s[0]) == ord('1') :
            print(H.decode(H, s))
        else :
            print(H.encode(s))
    except :
        break