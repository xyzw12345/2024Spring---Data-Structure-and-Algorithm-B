listVowel = ['a','A','e','E','i','I','o','O','u','U','y','Y']
def isVowel(c) :
    for v in listVowel :
        if c == v :
            return 1
    return 0
def toLowerCase(c) :
    if ord('A') <= ord(c) and ord(c) <= ord('Z') :
        return chr((ord(c) + ord('a') - ord('A')))
    return c

s = input()
res = []
for c in s :
    if isVowel(c) == 0 :
        res.append('.')
        res.append(toLowerCase(c))
res1 = "".join(res)
print(res1)
