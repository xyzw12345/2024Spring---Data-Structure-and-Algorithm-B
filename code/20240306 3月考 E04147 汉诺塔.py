def hanoi(val, s1, s2, s3) :
    if val == 1 :
        print(f"{val}:{s1}->{s3}")
        return
    hanoi(val - 1, s1, s3, s2)
    print(f"{val}:{s1}->{s3}")
    hanoi(val - 1, s2, s1, s3)

s = input().split()
hanoi(int(s[0]), s[1], s[2], s[3])
