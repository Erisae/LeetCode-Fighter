### Tag Problems
sorting decreasing to frequency
- [x] 🔴 [465. Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/description/)
    - **D**: [from, to, amount], 最少transaction次数
    - **S**: 在array index上的backtracking试图用当前处理后面的债务
        1. 建表owe[person]每个人欠钱，filter非0的形成array
        2. backtracking(输入当前处理index和当前transaction数)尝试用cur_index处理后面任意i_index的债务(乘积<0)。这之后cur_index处理完毕bkt输入cur_index+1。注意backtracking也要开始skip所有开始的0
- [] 🟡 [666. Path Sum IV](https://leetcode.com/problems/path-sum-iv/description/)
    - **D**: dpv->depth, postion, value; 返回所有root到leaf的path总和
    - **S**: $[d, p]$ -> $[d+1, p*2-1]$和$[d+1, p*2]$; dfs传到node前的总和
- [] 🟡 [2217. Find Palindrome With Fixed Length](https://leetcode.com/problems/find-palindrome-with-fixed-length/description/)
    - **D**: 返回queries[i]th个长度为intLength的对称数
    - **S**: 构造对称数，只用看前半部分顺序ceil(intLengh/2)，后半部分变大不会影响整体。按照顺序从10..0开始flip生成后面
- [] 🔴 [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/description/)
    - **D**: 实现file system数据结构和方法：ls, mkdir, addContentToFile, readContentFromFile
    - **S**: 数据结构Dir(self.contains，dict包含的名字：结构)File(结self.content，str)
- [x] 🔴 [2263. Make Array Non-decreasing or Non-increasing](https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/description/)
    - **D**: 每次操作只能把nums[i]变成+1/-1,问最少次数让nums成为单调增/减
    - **S**: maxHeap
        1. increasing和decreasing是一个意思，只需要把array反过来
        2. make increasing, 10,5 两个数无论怎么都要cost 5, 就写成10，5表示都可以pay zero cost(5之后)到10，10
        3. 如果之后num > maximum current -> incresing直接append heap
        4. 如果之后num < maximum current -> 需要pay cost(difference), 然后把max变小diff
- [] [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/description/)
    - **D**: 找到(i,j,k)个数(i < j < k)使得nums[i]+nums[j]+nums[k]<target
    - **S**: fix i, fix j, 快速找到k
        1. sort, fix i
        2. 对于j,k: 如果一个(j,k)成立->k选择j+1~k之间的都成立。类似fix j找成立的最大k。从k最大开始，k不成立->k--(为了更快通过可以test k//2是否成立，不成立直接腰斩)，直到k成立。
- [x] 🔴 [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/description/)
    - **D**: non-negative int, +-*/,()
    - **S**: 重点是不把+-当二元计算
        1. evaluate函数用来计算局部2元结果，注意+-不计算二元结果，只表示当前curValue是正负(*), */立即处理，+-变符号处理，处理完了之后入栈，()和全部结果都是直接把栈上相加
        2. digit => build curVal
        3. "("把lastSeenOp入栈 (只有在这种情况下入栈op, 用来定位括号)
        4. op或")"则evaluate(lastSeenOp, curVal, stack[-1])并且入栈
        5. 特别的")"，继续把直到lastSeenOp前的int都加起来入栈，recover lastSeenOp
- [x] 🔴 [403. Frog Jump](https://leetcode.com/problems/frog-jump/description/)
    - **D**: stones的array，青蛙一开始在0上并且第一跳只能为1，上次跳k这次只能跳k-1,k,k+1问是否可以到最后一个stone上
    - **S**: 有点像bfs，逐步生成next。因为每次只有三种可能的跳跃长度，并且到stonej>i之前所有i都遍历完了，可以从stones前面遍历到后面，记录可以到达的后面stone，dict{stonei, list of ks}，表示能到达stonei的上一个k。对后面的stone从字典中选取上一次的k并且生成之后可以到达的。
- [] 🟢 [1507. Reformat Date](https://leetcode.com/problems/reformat-date/description/)
    - **D**: "6th Jun 1933" -> "1933-06-06"
    - **S**: 字典map
- [] 🟡 [1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/)
    - **D**: binrary tree+distance, good的定义是两个leaf node他们的最短距离<=distance
    - **S**: DFS
        1. 对于每个node,分别找到左右child的leaf-node len, 组合起来看有多少个< distance。因为组合的是左右，所以这个node一定是最深的公共parent。
        2. 不会重复，可以不存具体node，用dict
- [] 🟡 [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/description/)
    - **D**: 返回相同独特形状的island个数
    - **S**: DFS的时候存形状, 可以用frozenset把set转换成key
- [] 🟡 [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)
    - **D**: prerequisites = [a, b] take b before take a. 返回order of course上的
    - **S**: topological sort
        1. BFS, 建立dict depend[a] = [c, d, e, f]表示后面都有prereq为a，对每个课建立prereq数，表示还有几门prereq没有上。enqueue prereq数为0的，每次处理一个queue里的，并且把相应depend list中所有prereq - 1.
        2. DFS, 根据prereq建立edge。如果有环说明不成立(rec_stack二次访问)，visited更新在dfs之后，顺序是dfs的相反顺序。访问node前后要加入/删除node在rec_stack中。因为node已经访问过了其实可以delete edge[node]防止再次访问。返回visited的reverse
- [x] 🔴 [2290. Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/)
    - **D**: 2D的grid，0表示可以走1表示obstacle。最少remove的obstable数量然后从(0, 0)走到(m-1. n-1)
    - **S**: BFS, 
        1. visited[i][j] 存放最少remove的obstacle以到达(i,j)。queue也存放这个cost，下一个cost+grid[i][j]如果比visited里面小就再次enqueue
        2. 为了使得第一次遍历到(m-1,n-1)的时候就是shortest path(最少obstacle)可以在上述enqueue的时候把策略改成如果比visited小而且grid==0,表示可以直通，appendleft而不是append。
- [] 🟡 [395. Longest Substring with At Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/)
    - **D**: 返回最长子串，里面每个char的出现次数>=k
    - **S**: recursion
        1. 从长往段看，如果在[a, b]中有一个字符k不满足 -> 说明最后结果一定不包含k，根据k把原来的字符串分割成了几个子串
        2. 在split的上面查看，并且记录最长的
- [x] 🔴 [2791. Count Paths That Can Form a Palindrome in a Tree](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/description/)
    - **D**： 用parent存的树，每个edge赋值了一个char，问所有node pair(u, v) u < v,并且从u到v的path上的所有char可以rearrange成一个palindrome字符串
    - **S**：DFS + bit manipulation
        1. palindrome -> 最多只有一个出现为奇数次 -> 26 bit的串只有一位为1
        2. (u, v) path -> 如果不考虑最低相同父节点，考虑root，会经过两次root->同父，不影响palindrome判断
        3. DFS，到node的时候记录root->node的path mask，dfs获得所有root->node的path
        4. 这些mask可以求一个counter
        5. 不对所有mask一一xor，而是对每个node，result+`mask[node]`(相同的),+`sum[mask[mask[node] ^ 1 << i] for i in range(26)]` 认为^反方向有效，找到和当前`mask[node]`可能形成palindrome的mask。最后/2
- [] 🟡 [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/description/)
    - **D**: balanced parenthesis, ()=1, AB=A+B, (A)=2*A
    - **S**: stack
        1. ((() + ())) -> 可以拆分为((())) + ((()))所以结果，根据最深的深度(1, 2, 4增长)可以直接加到result
        2. `(` -> 入栈深度，`)`->出栈，如果`)`并且上一个不是`)`就在result上加上出栈的数据
- [] 🔴 [924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/description/)
    - **D**: 邻接表存每两个node之间是否有直接联系，有一系列initials，问remove哪一个让减少最多malware
    - **S**: union-find，对每一对相邻的union。最后找initials里面每个的root，remove->该root只有他且group size最大的
- [] 🟡 [886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/description/)
    - **D**: split into 2, dislikei = [ai, bi]这两个人不要在一个group，返回是否可能split
    - **S**: union-find, 当dislike a<->b, a<->c 说明b应该在同一组，按照这个规律union，如果最后dislike的两个在不同root就合理
- [] 🟡 [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
    - **D**: 返回island个数
    - **S**: DFS, visit过的改成0
- [] 🔴 [2050. Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/description/)
    - **D**: course 有[prevCourse, nextCourse]表示依赖关系。另外上每门课都有时间，必须在时间上完之后才能下一门，返回上完所有课最短时间
    - **S**: BFS, toposort, maxDistance
        1. queue中是现在parallel在上的课(prereq都满足), 包括是什么课以及到它的时间。distance表示到每门课的时间(最大的)
        2. 每次popleft queue表示这门课已经上完了(到它时间+用时)，然后把depend on它的课dependency都-1，更新distance。如果dependency为0了就enqueue。
- [] 🟡 [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/)
    - **D**: 删除相邻的k个重复字符，删除之后连接，知道没有
    - **S**: stack, 都入栈，相邻k个就全部出栈。因为有拼接，非常直观。
- [] 🔴 [1293. Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/)
    - **D**: 类似2280，但是这次有限制最多remove k和obstacle，然后要找的是到corner的shortest path
    - **S**: BFS, queue里需要有node, distance, credit(一开始是k)，然后distance存到当前的credit，如果之后到这个点的credit更大/distance更小，改变distance并且二次enqueue。第一次就能return。注意因为步幅恒定是1，所以第一次到dest一定是最早的。
- [] 🟡 [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)
    - **D**: 有一些列的flights = [from, to, price] 返回最多k stop的最低价格
    - **S**: BFS，设置一个credit(一开始是k)，queue内是node, price, credit，如果到一个点price更低/credit更高继续enqueue。visited存credit和cost。注意不能到dest的时候直接return(因为每一步的长度不等)
- [] 🟡 [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/)
    - **D**: 有weights表示按照顺序的重量，找到传送带的最低容量使得可以在k天内传送完所有货物
    - **S**: search-> bin search, 最小为sum/day, 最大为sum。每次选定cap用greedy测试
- [] 🔴 [815. Bus Routes](https://leetcode.com/problems/bus-routes/description/)
    - **D**: 有一系列的bus routes，问从source到dest的最少换乘次数
    - **S**：抽象然后BFS。只在意换乘次数->把每条route抽象成一个node，有交叉点就是有edge。然后进行bfs找最短路径
