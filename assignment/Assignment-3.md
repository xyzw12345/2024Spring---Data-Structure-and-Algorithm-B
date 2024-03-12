# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by 数学科学学院 王镜廷 2300010724



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows11 专业版

Python编程环境：VSCode 1.86.2, with extension Python and python version 3.12.2



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/

用时：约10分钟

思路：

用dp[i]记录考虑前i个导弹，在击落第i个导弹的情况下至多击落几枚导弹。

##### 代码

```python
n = int(input())
s = list(map(int, input().split()))
dp = [0] * (n + 1)
res = 0
for i in range(n) :
    dp[i] = 1
    for j in range(i) :
        if s[j] >= s[i] :
            dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])
print(res)

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-12.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147

用时：约5分钟

思路：

使用递归方法来处理。

##### 代码

```python
def hanoi(val, s1, s2, s3) :
    if val == 1 :
        print(f"{val}:{s1}->{s3}")
        return
    hanoi(val - 1, s1, s3, s2)
    print(f"{val}:{s1}->{s3}")
    hanoi(val - 1, s2, s1, s3)

s = input().split()
hanoi(int(s[0]), s[1], s[2], s[3])


```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-13.png)



**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253

用时：约10分钟

思路：

用队列来模拟

##### 代码

```python
while(True) :
    n, p, m = map(int, input().split())
    if n == 0 and m == 0 and p == 0 :
        break
    h = []
    for i in range(p, n + 1) :
        h.append(i)
    for i in range(1, p) :
        h.append(i)
    tot = 0
    flag = False
    while h != [] :
        tot += 1
        x = h[0]
        del(h[0])
        if tot == m :
            if not flag :
                print(x, end="")
            else :
                print(f",{x}", end="")
            flag = True
            tot = 0
        else :
            h.append(x)
    print("")


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-14.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554

用时：约6分钟

思路：

将学生按照时间从短到长来安排

##### 代码

```python
class stu :
    def __init__(self, time, num) :
        self.time = time
        self.num = num
    def __lt__(self, other) :
        return self.time < other.time or (self.time == other.time and self.num < other.num)

n = int(input())
s = list(map(int, input().split()))
h = []
for i in range(n) :
    h.append(stu(s[i], i))
h = sorted(h)
print(" ".join(str(item.num + 1) for item in h))
sum = 0
for i in range(n) :
    sum += h[i].time * (n - 1 - i)
print(f"{sum / n :.2f}")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-16.png)



**19963:买学区房**

http://cs101.openjudge.cn/practice/19963

用时：约10分钟

思路：

依题意模拟即可

##### 代码

```python
def Median(s) :
    s1 = sorted(s)
    n = len(s)
    if n % 2 == 0 :
        return (s1[n//2 - 1] + s1[n//2]) / 2
    else :
        return s1[(n - 1)//2]

n = int(input())
pairs = [i[1:-1] for i in input().split()]
distances = [sum(map(int, i.split(','))) for i in pairs]
prices = list(map(int, input().split()))
ratio = [distances[i] / prices[i] for i in range(n)]
price_m = Median(prices)
ratio_m = Median(ratio)
res = 0
for i in range(n) :
    if prices[i] < price_m and ratio[i] > ratio_m :
        res += 1
print(res)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-17.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300

用时：约15分钟

思路：

依题意处理，将每个信息拆成名字、参数量中的数字部分和参数量的单位来处理，之后排序并输出即可。

##### 代码

```python
class info :
    def __init__ (self, name, sizenum, sizelevel) :
        self.name = name
        self.sizenum = sizenum
        self.sizelevel = sizelevel
    def __lt__(self, other) :
        return self.name < other.name or (self.name == other.name and self.sizelevel > other.sizelevel) or (self.name == other.name and self.sizelevel == other.sizelevel and float(self.sizenum) < float(other.sizenum))

n = int(input())
h = []
for i in range(n) :
    s = input().split("-")
    h.append(info(s[0], s[1][0 : len(s[1]) - 1], s[1][len(s[1]) - 1]))
h = sorted(h)
for i in range(len(h)) :
    if i == 0 or (i != 0 and h[i].name != h[i - 1].name) :
        print(f"{h[i].name}: {h[i].sizenum}{h[i].sizelevel}", end="")
    else :
        print(f", {h[i].sizenum}{h[i].sizelevel}",end="")
    if i < len(h) - 1 and h[i].name != h[i + 1].name :
        print("")



```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-18.png)



## 2. 学习总结和收获

又练习了一下python中类的写法，同时复习了计算概论中的dp等方面的基础知识。