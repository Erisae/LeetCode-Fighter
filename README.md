# LeetCode-Fighter

### Sliding Window
1. 为什么要window -> window内的东西有意义 -> 连续的东西。
2. 维持window: left & right都从0开始，right滑扩大，left滑缩小。
3. window内：数据结构记录window信息并且在滑动更新，eg: dict
4. #longest/mimimum

##### 应用场景
- Substring, Subarray
    - <span style="color:orange">[Medium]</span> 3. Longest Substring Without Repeating Characters
    - <span style="color:orange">[Medium]</span> 209. Minimum Size Subarray Sum
    - <span style="color:red">[Hard]</span> 76. Minimum Window Substring
- Adjacent xx in string
- Repeating(连续) characters in string
    - <span style="color:orange">[Medium]</span> [424. Longest Repeating Character Replacement](./424.%20Longest%20Repeating%20Character%20Replacement.py)

---------

### Two Pointer
1. left,right从头尾开始的比较多，宽度收缩/sort上
2. 也是探索连续的部分

##### 应用场景
- 3 Sum, sort之后固定一个，后面两个分别表示最大最小，大了->移动右边，小了->移动左边
    - <span style="color:orange">[Medium]</span> [259. 3Sum Smaller](./259.%203Sum%20Smaller.py)
- 1D Palindrome
    - <span style="color:orange">[Medium]</span> 2422. Merge Operations to Turn Array Into a Palindrome
- 一片区域的长宽对面积的tradeoff
    - <span style="color:orange">[Medium]</span> [11. Container With Most Water](./11.%20Container%20With%20Most%20Water.py)

---------


### Union Find
1. 对每条edge进行union
2. 没有直接可看的edge就按照逻辑创造edge

##### 应用场景
- 无向连通图(邻接矩阵)，有多少个部分(roots)，每个部分有多少node(size)，每个点属于哪个部分(find)
    - <span style="color:red">[Hard]</span> [924.Minimize Malware Spread](./924.%20Minimize%20Malware%20Spread.py)
    - <span style="color:red">[Hard]</span> [929.Minimize Malware Spread II](./928.%20Minimize%20Malware%20Spread%20II.py)
    - <span style="color:orange">[Medium]</span> 323. Number of Connected Components in an Undirected Graph
- Bipatition，按照xx原因分成两组
    - 按照逻辑，应该在同一边的union，之后全局搜索不该同一边的如果在那就有问题
    - <span style="color:orange">[Medium]</span> 886. Possible Bipartition
- 无向图是否有环检测
    - 对edges数组，如果在union(e0,e1)之前就发现e0,e1在同一个子集里面说明有环
    - <span style="color:orange">[Medium]</span> 261. Graph Valid Tree
- xxx条件数字个数
    - <span style="color:orange">[Medium]</span> 128. Longest Consecutive Sequence

---------

### Back Tracking
##### 应用场景
- 组合Combination
    - <span style="color:orange">[Medium]</span> 39. Combination Sum
    - <span style="color:orange">[Medium]</span> 40. Combination Sum II
- 子集
    - <span style="color:orange">[Medium]</span> 78. Subsets
- Permutation
    - <span style="color:orange">[Medium]</span> 46. Permutations
    - <span style="color:orange">[Medium]</span> 47. Permutations II
- 给定patern，返回所有可组合的结果
    - <span style="color:orange">[Medium]</span> 93. Restore IP Addresses
- 向后search，模拟测试，找最小/pattern, 重点是可撤回
    - <span style="color:red">[Hard]</span> 465. Optimal Account Balancing [(lc)](https://leetcode.com/problems/optimal-account-balancing/description/)
    - <span style="color:orange">[Medium]</span> 79. Word Search [(lc)](https://leetcode.com/problems/word-search/description/) (search可以回退->visited)

---------

### Greedy
#### 应用场景
- 构造固定结构(结构构造方法很死)
    -  <span style="color:orange">[Medium]</span> [1541. Minimum Insertions to Balance a Parentheses String](./1541.%20Minimum%20Insertions%20to%20Balance%20a%20Parentheses%20String.py)
    - <span style="color:orange">[Medium]</span> 2422. Merge Operations to Turn Array Into a Palindrome
- 在不同时间/区间分配东西，求最少天数/capacity/长度
    - <span style="color:orange">[Medium]</span> [1011. Capacity To Ship Packages Within D Days](./1011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.py)
    - <span style="color:orange">[Medium]</span> [1405. Longest Happy String](./1405.%20Longest%20Happy%20String.py) (+heap)
    - <span style="color:orange">[Medium]</span> 253. Meeting Rooms II (+heap)
    - <span style="color:orange">[Medium]</span> 621. Task Scheduler (+heap)
- 按照让接下来有更多机会选择
    - <span style="color:orange">[Medium]</span> 45. Jump Game II (跳到reach最大的 -> 下一个有更大可选空间)
    - <span style="color:orange">[Medium]</span> 435. Non-overlapping Intervals (按照end time最早的选择 -> 下一个有更大可选空间)

---------


### 1D DP
##### 应用场景
- 循环中遍历前面已经生成dp生成新的路径
    - <span style="color:orange">[Medium]</span> 139. Word Break [(lc)](https://leetcode.com/problems/word-break/description/) (串<->list of words匹配)
    - <span style="color:orange">[Medium]</span> 45. Jump Game II
- dp0/dp1表示当包括i和直到i的max/min，交错更新
    - <span style="color:orange">[Medium]</span> 53. Maximum Subarray [(lc)](https://leetcode.com/problems/maximum-subarray/description/) (没有排序用不了2ptr和sw)
    - <span style="color:orange">[Medium]</span> 152. Maximum Product Subarray
- dp表示包括i的max/min/个数，根据相邻的逻辑生成递归，过程中记录全局min/max
    - <span style="color:red">[Hard]</span> 32. Longest Valid Parentheses [(lc)](https://leetcode.com/problems/longest-valid-parentheses/description/) (包括i则必须为)但是i-1有两种可能，分别构造)
    - <span style="color:orange">[Medium]</span> 91. Decode Ways [(lc)](https://leetcode.com/problems/decode-ways/description/)
- Best Time to buy and sell stock
    - <span style="color:orange">[Medium]</span> 122. Best Time to Buy and Sell Stock II
    - <span style="color:red">[Hard]</span> 123. Best Time to Buy and Sell Stock III

---------


### 2D DP
##### 应用场景
- Number/Len of palindrome => 从len=1开始构造，dp[i][j]表示考虑的子串
    - <span style="color:orange">[Medium]</span> 5. Longest Palindromic Substring
    - <span style="color:orange">[Medium]</span> 647. Palindromic Substrings
- 两个字符串的匹配修改(update/delete/insert)，dp[i][j]表示串1和串2匹配的截止位置
    - <span style="color:orange">[Medium]</span> 72. Edit Distance
    - <span style="color:red">[Hard]</span> 115. Distinct Subsequences [(lc)](https://leetcode.com/problems/distinct-subsequences/description/)
- 本身就在2Dgrid上操作，根据周边构造当前
    - <span style="color:orange">[Medium]</span> 542. 01 Matrix (prefer BFS)
    - <span style="color:orange">[Medium]</span> 799. Champagne Tower [(lc)](https://leetcode.com/problems/champagne-tower/description/)
- 115. Distinct Subsequences
- 799. Champagne Tower
- 542. 01 Matrix

---------

### Heap

---------


### Stack




