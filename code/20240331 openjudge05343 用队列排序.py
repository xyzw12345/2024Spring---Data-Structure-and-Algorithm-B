N = int(input())
s = input().split()
q = []
for i in range(15) :
    q.append([])
for item in s :
    q[int(item[1])].append(item)
for i in range(1, 10) :
    print(f"Queue{i}:", end = "")
    print(' '.join(item for item in q[i]))
for i in range(1, 10) :
    for item in q[i] :
        q[ord(item[0]) - ord('A') + 10].append(item)
for i in range(0, 4) :
    print(f"Queue{chr(i + ord('A'))}:", end = "")
    print(' '.join(item for item in q[i + 10]))
for i in range(10, 14) :
    for item in q[i] :
        q[14].append(item)
print(' '.join(item for item in q[14]))
