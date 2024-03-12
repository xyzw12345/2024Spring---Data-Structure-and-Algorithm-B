tot = 0
s = []
def solve() :
    global tot
    global s
    c = s[tot]
    tot += 1
    if c == '+' :
        return solve() + solve()
    if c == '-' :
        return solve() - solve()
    if c == '*' :
        return solve() * solve()
    if c == "/" :
        return solve() / solve()
    else :
        return float(c)
    

s = input().split()
print(f"{solve():.6f}")
