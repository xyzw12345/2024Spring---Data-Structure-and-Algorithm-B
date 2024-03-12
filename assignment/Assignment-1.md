# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by ==数学科学学院 王镜廷 2300010724==



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows11 专业版

Python编程环境：VSCode 1.86.2, with extension Python and python version 3.12.2




## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/


做题时间：约3分钟


思路：
用数组存储数列每项的值并递推即可


##### 代码

```python
s = [0, 1, 1]
for i in range(30) :
    s.append(s[i]+s[i+1]+s[i+2])
n = int(input())
print(s[n])

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A

做题时间：约5分钟

思路：
用一个变量$n$来记录在当前位置及以前最多能匹配字符串$"hello"$的前几位


##### 代码

```python
s1 = "hello"
s = input()
n = -1
for c in s :
    if n < 4 :
        if c == s1[n+1] :
            n = n + 1
if n == 4 :
    print("YES")
else :
    print("NO")

```



代码运行截图 ==（至少包含有"Accepted"）==

![alt text](image-2.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A

做题时间：约10分钟

思路：将String转化为List， 每一位依次处理后再转换回String输出



##### 代码

```python
# listVowel = ['a','A','e','E','i','I','o','O','u','U','y','Y']
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


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-1.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/

做题时间：约5分钟

思路：
对于每一对和为$n$的数依次判断是否均为质数，输出第一对满足条件的


##### 代码

```python
def isPrime(n) :
    i = 2
    while i * i <= n :
        if n % i == 0 :
            return 0
        i = i + 1
    return 1

n = int(input())
i = 1
while i <= n / 2 :
    if isPrime(i) == 1 and isPrime(n - i) == 1 :
        print(f"{i} {n - i}")
        break
    i = i + 1

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-3.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/

做题时间：约15分钟

思路：
首先以加号把不同的项分开，之后依次处理并判断其是否会增大最高幂次


##### 代码

```python
s = input().split("+")
s2 = []
x = 0
y = 0
k = 0
for ss in s :
    s2 = list(map(int, [item for item in ss.split("n^") if item != ""]))
    #print(s2)
    if len(s2) == 1 :
        x = 1
        y = s2[0]
    else :
        x = s2[0]
        y = s2[1]
    if y > k and x > 0 :
        k = y
print(f"n^{k}")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-4.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/

做题时间：约10分钟

思路：

依次记录每个人所得票数，统计完成后枚举每个人得到答案

##### 代码

```python
s = list(map(int, input().split()))
cnt = [0] * 100001
for c in s :
    cnt[c] = cnt[c] + 1
MAX = 0
listMax = []
for i in range(100001) :
    if cnt[i] > MAX :
        listMax = []
        MAX = cnt[i]
    if cnt[i] == MAX :
        listMax.append(i)
for i in range(len(listMax)) :
    if i > 0 :
        print(" ", end = "")
    print(listMax[i], end = "")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-5.png)



## 2. 学习总结和收获

在这次作业中，我熟悉了python的基础语法，对于输入输出和基本的对于字符串和列表的操作有了更多了解。