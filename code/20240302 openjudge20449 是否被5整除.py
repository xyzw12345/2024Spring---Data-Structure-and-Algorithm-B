s = input()
r = 0
for c in s :
    r = 2 * r + ord(c) - ord('0')
    r = r % 5
    if r == 0 :
        print("1", end = "")
    else :
        print("0", end = "")

