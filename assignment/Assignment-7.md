# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by 数学科学学院 王镜廷 2300010724



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows11 专业版

Python编程环境：VSCode 1.86.2, with extension Python and python version 3.12.2



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/

用时：约5分钟

思路：
依题意模拟即可


代码

```python
s = input().split()
s.reverse()
print(" ".join(item for item in s))

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-39.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/

用时：约10分钟

思路：
依题意模拟即可


代码

```python
m, n = map(int, input().split())
s = list(map(int, input().split()))
mem = []
res = 0 
for item in s :
    #print(mem)
    if not item in mem :
        res += 1
        mem.append(item)
        if len(mem) > m :
            mem.pop(0)
print(res)

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-40.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/

用时：约5分钟

思路：
注意所求之数如果存在的话即为从小到大第k个，只需判断其是否满足即可


代码

```python
n, k = map(int, input().split())
s = list(map(int, input().split()))
s.append(1)
s = sorted(s)
if k < n and s[k] == s[k + 1] :
    print("-1")
else :
    print(s[k]) 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-41.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/

用时：约12分钟

思路：
依题意模拟即可，判断每个节点类型可以通过计算区间和完成（和为区间长度则全部为1，和为0则全部为0），区间和可以通过前缀和求出。


代码

```python
sum = []
class node :
    def __init__ (self, left, right, type) :
        self.left = left
        self.right = right
        self.type = type 
    def __str__ (self) :
        s1 = "" if self.left == None else str(self.left)
        s2 = "" if self.right == None else str(self.right)
        return s1 + s2 + self.type
def build(l, r) :
        global sum
        m = (l + r) // 2
        c = 'F'
        if sum[r] - sum[l - 1] == r - l + 1:
            c = 'I'
        if sum[r] - sum[l - 1] == 0 :
            c = 'B'
        if l == r :
            return node(None, None, c)
        return node(build(l, m), build(m + 1, r), c)
n = int(input())
s = input()
sum.append(0)
for i in range(1 << n) :
    sum.append(sum[-1] + ord(s[i]) - ord('0'))
print(build(1, 1 << n))


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-42.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/

用时：约11分钟

思路：
维护一个现在从前往后的小组的队列，再对每个小组分别维护一个队列记录其在队中的人。


代码

```python
from collections import deque
people2grp = dict()
t = int(input())
for i in range(t) :
    s = list(map(int, input().split()))
    for u in s :
        people2grp[u] = i
q = []
for i in range(t) :
    q.append(deque([]))
qgrp = deque([])
isin = dict(zip(list(i for i in range(t)), [0] * t))
while True :
    s = input().split()
    if s[0] == "STOP" :
        break
    if s[0] == "DEQUEUE" :
        u = qgrp.popleft()
        isin[u] = 0
        print(q[u].popleft())
        if len(q[u]) > 0 :
            qgrp.appendleft(u)
            isin[u] = 1
    if s[0] == "ENQUEUE" :
        u = people2grp[int(s[1])]
        q[u].append(int(s[1]))
        if isin[u] == 0 :
            qgrp.append(u)
            isin[u] = 1



```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-44.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/

用时：约12分钟

思路：依题意模拟即可，注意过程中首先需要求出根节点的编号。



代码

```python
n = int(input())
d = dict()
dstr = dict()
def getstr(u) :
    global d
    global dstr
    if u in dstr :
        return dstr[u]
    dstr[u] = "\n".join((getstr(v) if v != u else str(u)) for v in d[u])
    return dstr[u]
for i in range(n) :
    s = list(map(int, input().split()))
    d[s[0]] = sorted(s)
dfather = dict(zip(list(item for item in d), list(item for item in d)))
for u in d :
    for v in d[u] :
        if v != u :
            dfather[v] = u
root = 0
for u in d :
    if dfather[u] == u :
        root = u
print(getstr(root))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-43.png)



## 2. 学习总结和收获

总结：这次考试因为上机课的时间有事情所以未能到现场参加，自己在下面完成的时候用了大约55分钟完成全部题目。这次考试让我留下深刻印象的是代码常常可以运用系统中提供的dict和deque进行简化。