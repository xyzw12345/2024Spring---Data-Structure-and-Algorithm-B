class node :
    def __init__ (self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val

def getIndex(c, s) :
    for i in range(len(s)) :
        if c == s[i] :
            return i
    return -1

def ToPostString(s) :
    s1 = ""
    if s.left != None :
        s1 = ToPostString(s.left) + " "
    s2 = ""
    if s.right != None :
        s2 = ToPostString(s.right) + " "
    return s1 + s2 + str(s.val)

def BuildTree_pre_in(sp, si) :
    if sp == [] :
        return None
    l = getIndex(sp[0], si)
#    print(sp, si, l, sep = " ")
    return node(BuildTree_pre_in(sp[1 : l + 1], si[0 : l]), BuildTree_pre_in(sp[l + 1 : len(sp)], si[l + 1 : len(si)]), sp[0])

n = int(input())
s1 = list(map(int, input().split()))
s2 = sorted(s1)
print(ToPostString(BuildTree_pre_in(s1, s2)))
