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

class deque :
    left = stack([])
    right = stack([])
    def __init__(self, left, right) :
        left.reverse()
        self.left = stack(left)
        self.right = stack(right)
    def balanced(self) :
        if self.left.size() != 0 and self.right.size() != 0 :
            return True
        if self.left.size() <= 1 and self.right.size() <= 1 :
            return True
        return False
    def rebalance(self) :
        if self.balanced() :
            return
        if self.left.size() == 0 :
            n = self.right.size()
            m = n // 2
            s = self.right.item
            s1 = s[0 : m]
            s1.reverse()
            self.left = stack(s1)
            self.right = stack(s[m : n])
        if self.right.size() == 0 :
            n = self.left.size()
            m = n // 2
            s = self.left.item
            s.reverse()
            s1 = s[0 : m]
            s1.reverse()
            self.left = stack(s1) 
            self.right = stack(s[m : n])
            return 
    def size(self) :
        return self.left.size() + self.right.size()
    def front(self) : #in a balanced deque
        if self.size() == 0 :
            return None
        if self.left.size() == 0 :
            return self.right.item[0]
        return self.left.top()
    def end(self) : #in a balanced deque
        if self.size() == 0 :
            return None
        if self.right.size() == 0 :
            return self.left.item[0]
        return self.right.top()
    def pushfront(self, x) :
        self.left.push(x)
        self.rebalance()
    def pushback(self, x) :
        self.right.push(x)
        self.rebalance()
    def popfront(self) : #in a balanced deque
        if self.left.size() == 0 :
            self.right.pop()
        else :
            self.left.pop()
        self.rebalance()
    def popback(self) :
        if self.right.size() == 0 :
            self.left.pop()
        else :
            self.right.pop()
        self.rebalance()
        
T = int(input())
for case in range(T) :
    n = int(input())
    h = deque([], [])
    flag = True
    for i in range(n) :
        op, x = map(int, input().split())
        if op == 1 :
            h.pushback(x)
        else :
            if x == 0 :
                h.popfront()
            else :
                h.popback()
            #if h.size() == 0 :
            #    flag = False
    if h.size() == 0 :
        print("NULL")
    else :
        s1 = h.left.item
        s1.reverse()
        s2 = h.right.item
        print(" ".join(str(item) for item in s1) + " " + " ".join(str(item) for item in s2))

