def getGcd(m, n) :
    if m == 0 or n == 0 :
        return m + n
    return getGcd(n, m % n)
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
    
    def simp(self) :
        return Fraction(self.num // getGcd(self.num, self.den), self.den // getGcd(self.num, self.den))

a = list(map(int, input().split()))
x = Fraction(a[0], a[1])
y = Fraction(a[2], a[3])
print((x + y).simp())