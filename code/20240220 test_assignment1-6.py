a = [item for item in input().split(" ") if item != ""]
a = list(map(int, a))
dict1 = {}
for i in a:
    if i not in dict1:
        dict1[i] = a.count(i)
max_votes = max(dict1.values())

winners = sorted([item for item in dict1.items() if item[1] == max_votes]) 

print(' '.join(str(winner[0]) for winner in winners))