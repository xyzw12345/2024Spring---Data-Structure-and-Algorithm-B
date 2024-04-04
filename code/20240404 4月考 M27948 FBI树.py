sum = []
class node :
    def __init__ (self, left, right, type) :
        self.left = left
        self.right = right
        self.type = type 
    def __str__ (self) :
        s1 = "" if self.left == None else str(self.left)
        s2 = "" if self.right == None else str(self.right)
        return s1 + s2 + self.type
def build(l, r) :
        global sum
        m = (l + r) // 2
        c = 'F'
        if sum[r] - sum[l - 1] == r - l + 1:
            c = 'I'
        if sum[r] - sum[l - 1] == 0 :
            c = 'B'
        if l == r :
            return node(None, None, c)
        return node(build(l, m), build(m + 1, r), c)
n = int(input())
s = input()
sum.append(0)
for i in range(1 << n) :
    sum.append(sum[-1] + ord(s[i]) - ord('0'))
print(build(1, 1 << n))
