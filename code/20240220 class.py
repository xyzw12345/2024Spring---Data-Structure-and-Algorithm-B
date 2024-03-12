class Fraction :
    num = 1
    den = 0
    def __init__(self, top, bottom) :
        self.num = top
        self.den = bottom
    
    def __eq__(self, other) :
        return self.num * other.den == self.den * other.num
    
    def __str__(self) :
         return str(self.num)+"/"+str(self.den)
    
    def __add__(self, other) :
        return Fraction(self.num * other.den + self.den * other.num, self.den * other.den)
    
print(Fraction(1, 4) + Fraction(2, 5))

class Node :
    lson = None
    rson = None
    def __init__ (self, lson, rson) :
        self.lson = lson
        self.rson = rson
    
    def __str__(self) :
        s1 = ""
        if self.lson != None :
            s1 = str(self.lson)
        s2 = ""
        if self.rson != None :
            s2 = str(self.rson)
        return "(" + s1 +"|"+ s2 + ")"

print(Node(Node(None, Node(None, None)),None),Node(Node(None, Node(None, None)), Node(None, Node(None, None))))

class NodeWithVal (Node):
    val = 0
    def __init__ (self, val, lson, rson) :
        Node.__init__(self, lson, rson)
        self.val = val    
