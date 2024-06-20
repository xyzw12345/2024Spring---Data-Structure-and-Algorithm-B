# 2024Spring---Data-Structure-and-Algorithm-B

这个代码仓库里存储的是2024年春季数据结构与算法B课程中所写的代码和作业。代码都在code文件夹中，标记了写的时间和出处，作业对应的markdown文档和pdf在assignment文件夹中，markdown文档里面对应的原始图片在image文件夹里面（因为一开始文件是在本地写的，所以就没有用图床），reference文件夹里面是两篇和这门课相关的文章，一篇探讨了shell sort的时间复杂度，另一篇探讨了在不进行按秩合并只进行路径压缩时并查集的时间复杂度，cheatsheet文件夹里就是cheatsheet。

学习方法与课程总结：  
    这门课上的一些知识在中学的时候已经学过，所以说主要的任务就变成了在课程中不断查漏补缺（比如说以前可能没有关注过warnsdorff算法这种的），同时也努力完成练习和作业，提高代码熟练度。一个学期的课程上下来感觉对于python还是显著的熟练了很多，也算是达到了报课的时候学习python这门语言的目的。  
    在学的过程中我感觉python相较于之前写的C而言相对会更方便一些，很多事情都可以通过调用别人已经写好的包来完成，对于科学计算有scipy/numpy，符号计算有sympy，都在平时生活中有不小的作用。这门课也让我感受到有时借助于ChatGPT也是一种很好的学习方法，ChatGPT一方面依赖于其训练数据而可以产生大量标准的代码，很有参考价值，另一方面对于各种包和系统函数的使用也可以随用随问，非常方便。

关于cheatsheet：  
    这次机考之前制作的cheatsheet混杂着这个学期写的python代码和之前写的C++代码，也有一些算法因为还没写过或者没找到想要的模板代码就暂时没有提供代码，但是在对应的地方也有对于算法思路的简述。  
    主要分成了几个部分，第一部分是关于python内置的set, dict, defaultdict, heap, deque和itertools, Counter等的使用方法，第二部分是一些在题目中常常可以与别的思路相结合以提高运行效率的数据结构或者算法，主要包括了树状数组、线段树、二分查找、单调栈、单调队列、AVL树、堆（重新手写了一遍）和ST表。第三部分是图上的算法，包括并查集、最短路（Dijkstra/Bellman-ford/Floyd/Johnson）、最小生成树（Kruskal/Prim）、强连通分量（Kosaraju，代码来自课程资料）、Warnsdorff算法等。第四部分是树上的算法，包括调度场算法（有一个我自己写的版本，但是怎么改都过不了布尔表达式那个题，所以还把题解里面武同学的布尔表达式的AC代码放在这里了）、LCA（是之前在C++里面写的重链剖分之后求LCA的版本）、前中序遍历建树等。第五部分是字符串算法，包括KMP（代码来自课程中提供的参考代码）、Trie树等，第六部分是数学相关的部分，只写了个欧拉筛。  
    本来在往里面填入代码之前列的算法和数据结构比现在其实还多一些，但是开始填入代码的时候才发现有很多东西自己没写过，也不完全会，于是就作罢了。


