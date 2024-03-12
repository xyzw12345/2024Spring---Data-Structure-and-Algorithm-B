cnt = 1
while(True) :
    s = input().split()
    b = int(s[0])
    c = int(s[1])
    d = int(s[2])
    a = int(s[3])
    if a == -1 and b == -1 and c == -1 and d == -1 :
        break
    for i in range(1, 21253) :
        if (a + i - b) % 23 == 0 and (a + i - c) % 28 == 0 and (a + i - d) % 33 == 0 :
            print(f"Case {cnt}: the next triple peak occurs in {i} days.")
            break 
    cnt += 1