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
    def isempty(self) :
        if self.item == [] :
            return True
        else :
            return False
    def push(self, elem) :
        self.item.append(elem)

def check(s, s1) :
    if len(s) != len(s1) :
        return False
    i = 0
    n = len(s) 
    q = stack([])
    j = 0
    while i <= n and j < n:
        if q.top() == s1[j] :
            q.pop()
            j += 1
            continue
        elif i < n:
            q.push(s[i])
            i += 1
        else :
            break
        #print(f"{i} {j} {q.item}")
    if j == n :
        return True
    else :
        return False
    
s = input()
while(True) :
    try :
        s1 = input()
        if check(s, s1) :
            print("YES")
        else :
            print("NO")
    except :
        break