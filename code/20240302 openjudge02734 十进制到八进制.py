n = int(input())
s = []
while n != 0 :
    s.append(n % 8)
    n = n // 8
s.reverse()
for item in s :
   print(item, end = "")