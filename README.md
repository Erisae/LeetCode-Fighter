# LeetCode-Fighter
🟢
### Sliding Window
1. 为什么要window -> window内的东西有意义 -> 连续的东西。
2. 维持window: left & right都从0开始，right滑扩大，left滑缩小。
3. window内：数据结构记录window信息并且在滑动更新，eg: dict
4. #longest/mimimum

##### 应用场景
- Substring, Subarray
    - 🟡 3. Longest Substring Without Repeating Characters
    - 🟡 209. Minimum Size Subarray Sum
    - 🔴 76. Minimum Window Substring
    - 🟡 [1358. Number of Substrings Containing All Three Characters](./1358.%20Number%20of%20Substrings%20Containing%20All%20Three%20Characters.py)
- Adjacent xx in string
- Repeating(连续) characters in string
    - 🟡 [424. Longest Repeating Character Replacement](./424.%20Longest%20Repeating%20Character%20Replacement.py)

---------

### Two Pointer
1. left,right从头尾开始的比较多，宽度收缩/sort上
2. 也是探索连续的部分

##### 应用场景
- 3 Sum, sort之后固定一个，后面两个分别表示最大最小，大了->移动右边，小了->移动左边
    - 🟡 [259. 3Sum Smaller](./259.%203Sum%20Smaller.py) (+binary search移动的时候)
- 1D Palindrome
    - 🟡 2422. Merge Operations to Turn Array Into a Palindrome
- 一片区域的长宽对面积的tradeoff
    - 🟡 [11. Container With Most Water](./11.%20Container%20With%20Most%20Water.py)

---------


### Union Find
1. 对每条edge进行union
2. 没有直接可看的edge就按照逻辑创造edge

##### 应用场景
- 无向连通图(邻接矩阵)，有多少个部分(roots)，每个部分有多少node(size)，每个点属于哪个部分(find)
    - 🔴 [924.Minimize Malware Spread](./924.%20Minimize%20Malware%20Spread.py)
    - 🔴 [929.Minimize Malware Spread II](./928.%20Minimize%20Malware%20Spread%20II.py)
    - 🟡 323. Number of Connected Components in an Undirected Graph
- Bipatition，按照xx原因分成两组
    - 按照逻辑，应该在同一边的union，之后全局搜索不该同一边的如果在那就有问题
    - 🟡 886. Possible Bipartition
- 无向图是否有环检测
    - 对edges数组，如果在union(e0,e1)之前就发现e0,e1在同一个子集里面说明有环
    - 🟡 261. Graph Valid Tree
- xxx条件数字个数/转换成连通区间个数检测
    - 🟡 128. Longest Consecutive Sequence
    - 🟡 [947. Most Stones Removed with Same Row or Column](./947.%20Most%20Stones%20Removed%20with%20Same%20Row%20or%20Column.py)
- path in tree
    - 🔴 [2421. Number of Good Paths](./2421.%20Number%20of%20Good%20Paths.py), 对value聚合->从大到小union->neighbor按照条件union->统计连同个数

---------

### Back Tracking
##### 应用场景
- 组合Combination
    - 🟡 39. Combination Sum
    - 🟡 40. Combination Sum II
- 子集
    - 🟡 78. Subsets
- Permutation
    - 🟡 46. Permutations
    - 🟡 47. Permutations II
- 给定patern，返回所有可组合的结果
    - 🟡 93. Restore IP Addresses
- 向后search，模拟测试，找最小/pattern, 重点是可撤回
    - 🔴 465. Optimal Account Balancing [(lc)](https://leetcode.com/problems/optimal-account-balancing/description/)
    - 🟡 79. Word Search [(lc)](https://leetcode.com/problems/word-search/description/) (search可以回退->visited)
- 找到所有可能
    - 🔴 282. Expression Add Operators

---------

### Greedy
#### 应用场景
- 构造固定结构(结构构造方法很死)
    -  🟡 [1541. Minimum Insertions to Balance a Parentheses String](./1541.%20Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String.py)
    - 🟡 2422. Merge Operations to Turn Array Into a Palindrome
- 在不同时间/区间分配东西，求最少天数/capacity/长度
    - 🟡 [1011. Capacity To Ship Packages Within D Days](./1011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.py)
    - 🟡 [1405. Longest Happy String](./1405.%20Longest%20Happy%20String.py) (+heap)
    - 🟡 253. Meeting Rooms II (+heap)
    - 🟡 621. Task Scheduler (+heap)
    - 🟡 [767. Reorganize String](./767.%20Reorganize%20String.py) (+heap) 区间:相邻，时间:freeze1
    - 🔴 [358. Rearrange String k Distance Apart](./358.%20Rearrange%20String%20k%20Distance%20Apart.py) (+heap) 有确定的数量，freeze时间k
- 按照让接下来有更多机会选择
    - 🟡 45. Jump Game II (跳到reach最大的 -> 下一个有更大可选空间)
    - 🟡 435. Non-overlapping Intervals (按照end time最早的选择 -> 下一个有更大可选空间)

---------


### 1D DP
##### 应用场景
- 循环中遍历前面已经生成dp生成新的路径 -> 现在为之后生成路径
    - 🟡 139. Word Break [(lc)](https://leetcode.com/problems/word-break/description/) (串<->list of words匹配)
    - 🟡 45. Jump Game II
    - 🔴 [403. Frog Jump](./403.%20Frog%20Jump.py) (+hash, +现在jump为之后生成路径kindofdfs)
- dp0/dp1表示当包括i和直到i的max/min，交错更新
    - 🟡 53. Maximum Subarray [(lc)](https://leetcode.com/problems/maximum-subarray/description/) (没有排序用不了2ptr和sw)
    - 🟡 152. Maximum Product Subarray
- dp表示包括i的max/min/个数，根据相邻的逻辑生成递归，过程中记录全局min/max
    - 🔴 32. Longest Valid Parentheses [(lc)](https://leetcode.com/problems/longest-valid-parentheses/description/) (包括i则必须为)但是i-1有两种可能，分别构造)
    - 🟡 91. Decode Ways [(lc)](https://leetcode.com/problems/decode-ways/description/)
- Best Time to buy and sell stock
    - 🟡 122. Best Time to Buy and Sell Stock II
    - 🔴 123. Best Time to Buy and Sell Stock III
- 函数修饰器@cache,DP已经遍历过的输入&输出
    - 🔴 [2050. Parallel Courses III](./2050.%20Parallel%20Courses%20III.py) 多次树遍历
    - 🟡 [418. Sentence Screen Fitting](./418.%20Sentence%20Screen%20Fitting.py) 多次开始单词为x的函数
- 记录dynamic window/prefix-suffix
    - 🟡 [926. Flip String to Monotone Increasing](./926.%20Flip%20String%20to%20Monotone%20Increasing.py)只有一个分界线，滑动分界线看最小个数

---------


### 2D DP
##### 应用场景
- Number/Len of palindrome => 从len=1开始构造，dp[i][j]表示考虑的子串
    - 🟡 5. Longest Palindromic Substring
    - 🟡 647. Palindromic Substrings
- 两个字符串的匹配修改(update/delete/insert)，dp[i][j]表示串1和串2匹配的截止位置
    - 🟡 72. Edit Distance
    - 🔴 115. Distinct Subsequences [(lc)](https://leetcode.com/problems/distinct-subsequences/description/)
- 本身就在2Dgrid上操作，根据周边构造当前
    - 🟡 542. 01 Matrix (prefer BFS)
    - 🟡 799. Champagne Tower [(lc)](https://leetcode.com/problems/champagne-tower/description/)
- 115. Distinct Subsequences
- 799. Champagne Tower
- 542. 01 Matrix

---------

### Heap
- Design System
    - 🔴 295. Find Median from Data Stream
- Keep track of min/max current
    - 🔴 [2263. Make Array Non-decreasing or Non-increasing](./2263.%20Make%20Array%20Non-decreasing%20or%20Non-increasing.py)

---------


### Stack
##### 应用场景
- mono stack
    - 🟡 [2863. Maximum Length of Semi-Decreasing Subarrays.py](./2863.%20Maximum%20Length%20of%20Semi-Decreasing%20Subarrays.py) (+2ptr) 思想如果x为最佳，没有x‘小于x 能nums[x']大于nums[x]，构造可行结果的单调关系，另一边从stack取用. stack和另一侧遍历又构成shrink/expand对抗的2ptr
    - 🟡  [503. Next Greater Element II](./503.%20Next%20Greater%20Element%20II.py) 右边第一个最大的可以到前面->从右到左遍历并且min-mono->pop直到比当前大的就是next -> 来两遍
- parenthesis
    - 🟡 [1249. Minimum Remove to Make Valid Parentheses](./1249.%20Minimum%20Remove%20to%20Make%20Valid%20Parentheses.py)
    - 🟡 [921. Minimum Add to Make Parentheses Valid](./921.%20Minimum%20Add%20to%20Make%20Parentheses%20Valid.py) ()都push的stack

---------

### Queue
- Save during BFS // Design System
    - 🟡 [919. Complete Binary Tree Inserter](./919.%20Complete%20Binary%20Tree%20Inserter.py)

---------

### BFS
##### 应用场景
- 最短路径
    1. 路径长度为1
    2. 有obstacle / stop限制
    3. 路径长度各不相同
    4. dijkstra -> heap and pop min dist, not sequentially traversal (nlogn)
    5. 多个开始点
    6. modified BFS
    - 🟡 [787. Cheapest Flights Within K Stops](./787.%20Cheapest%20Flights%20Within%20K%20Stops.py) (2 & 3 || 2 & 4) dijkstra的时候第一次遍历到dst就可以返回了
    - 🔴 [2290. Minimum Obstacle Removal to Reach Corner](./2290.%20Minimum%20Obstacle%20Removal%20to%20Reach%20Corner.py) (2 & 4 || 2 & 5) dist是到(i,j)最小的obstacle数量；modified BFS 优先处理obstacle更小的路径->grid[ni][nj]==0时候直接pushleft表示无成本增加地处理下一个(shortcut)
    - 🟡 [994. Rotting Oranges](./994.%20Rotting%20Oranges.py) (2 & 5)简单的传播->问传播时间
    - 🟡 [1631. Path With Minimum Effort.py](./1631.%20Path%20With%20Minimum%20Effort.py) 不是求路径->求abs差最大的最小

-----------


### DFS
##### 应用场景
- topological sort
- 建树
    - 🟡 [1382. Balance a Binary Search Tree](./1382.%20Balance%20a%20Binary%20Search%20Tree.py) 从inorder(increasing)构建平衡BST，直接中间split
- path/substree
    - 🟡 [652. Find Duplicate Subtrees](./652.%20Find%20Duplicate%20Subtrees.py) (+hash)
    - 🔴 [2791. Count Paths That Can Form a Palindrome in a Tree](./2791.%20Count%20Paths%20That%20Can%20Form%20a%20Palindrome%20in%20a%20Tree.py) (+hash +bitmap)\
- Islands
    - 🔴 [827. Making A Large Island](./827.%20Making%20A%20Large%20Island.py)(改原始值，1->岛的index，用index存岛大小)

-----------

### Recursion
- 有自然顺序规律,但是遍历又过于复杂
    - 🟡 [386. Lexicographical Numbers](./386.%20Lexicographical%20Numbers.py) formation sequence is a -> a*10 -> a+1 and you don't know how many layers you would stop
- Smaller parts have a relationship with the whole part, divide point
    - 🟡 [395. Longest Substring with At Least K Repeating Characters](./395.%20Longest%20Substring%20with%20At%20Least%20K%20Repeating%20Characters.py) if count(x) < k -> x would not be in finnal substring, divide on x


------------

### Binary Search
##### 应用场景
- when search can solve a problem & satisfy one-way move condition
    - 🟡 [1062. Longest Repeating Substring](./1062.%20Longest%20Repeating%20Substring.py)
    - 🟡 [1802. Maximum Value at a Given Index in a Bounded Array](./1802.%20Maximum%20Value%20at%20a%20Given%20Index%20in%20a%20Bounded%20Array.py)
- ask to "find" and logn(1D)/mlgn(2D)
    - 🟡 [1901. Find a Peak Element II](./1901.%20Find%20a%20Peak%20Element%20II.py) (2D: bin search on column -> on row)

-------------


### Trie
##### 应用场景
- Word search
    - 🟡 [1268. Search Suggestions System](./1268.%20Search%20Suggestions%20System.py)
    - 🔴 [745. Prefix and Suffix Search](./745.%20Prefix%20and%20Suffix%20Search.py) prefix+suffix tries+set, paired trie, suffix wrapped trie
- Similar DS
    - 🔴 [588. Design In-Memory File System](./588.%20Design%20In-Memory%20File%20System.py)
-------------

### Prefix/Suffix
##### 应用场景
- product/sum
    - 🟡 [1352. Product of the Last K Numbers](./1352.%20Product%20of%20the%20Last%20K%20Numbers.py)


--------------

### Triplet
##### 应用场景
- 3Sum
- [259. 3Sum Smaller](./259.%203Sum%20Smaller.py) (sort+fix1+2ptr+bin searcg)
- [334. Increasing Triplet Subsequence](./334.%20Increasing%20Triplet%20Subsequence.py) 顺序是关键(unsorted+1次遍历+keep两个)

--------------
### Array 
##### 应用场景
- sorted
    - 3Sum
    - [259. 3Sum Smaller](./259.%203Sum%20Smaller.py) (sort+fix1+2ptr+bin searcg)
- unsorted  (+hash/dp) (要求O(n)) 顺序是关键
    - [334. Increasing Triplet Subsequence](./334.%20Increasing%20Triplet%20Subsequence.py) (unsorted+1次遍历+记录到现在为止1st/2nd小)
    - 🟡 128. Longest Consecutive Sequence (start of sequential -> while end)



