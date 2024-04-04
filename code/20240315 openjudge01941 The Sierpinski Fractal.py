
def work(n) :
    if n == 1 :
        return [" /\ ", "/__\\"]
    s = work(n - 1)
    s1 = []
    for i in range(1 << (n - 1)) :
        s1.append(" " * (1 << (n - 1)) + s[i] + " " * (1 << (n - 1)))
    for i in range(1 << (n - 1)) :
        s1.append(s[i] + s[i])
    return s1

while True :
    n = int(input())
    if n == 0 :
        break
    s = work(n)
    for item in s :
        print(item)
    print("")
