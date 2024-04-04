- [470. Implement Rand10() Using Rand7()](./470.%20Implement%20Rand10()%20Using%20Rand7().py): 注意！！均匀分布，如果两个rand7()->49个数字，一定要ar1 + b(r2 - c)前后生成49个才可以
- [528. Random Pick with Weight](./528.%20Random%20Pick%20with%20Weight.py): weight -> 区间然后根据random生成挑选。因为最后在search可以改成bin search
- [biased toss](./biased_toss.py): 生成的所有结果不一定都要用起来 -> 其中uniform的部分用起来！
- [384. Shuffle an Array](./384.%20Shuffle%20an%20Array.py): for i, randomly swap j>i with i. 


### ML
- Training Preparation:
    - [stratified sampling](./stratified_sampling.py)

- Model:
    - [KNN]
    - [k-means]
    - [binary logistic regression](./binary_logistic_regression.py) (weight+bias -> sigmoid -> gradient descend -> loss)
    - [decision tree]
    - [BatchNorm]
    - [LayerNorm]
    - [Attention]
    - [AE]
    - [Dropout]

- Activation:
    - [Softmax](./softmax.py) $softmax(x_i) = \frac{e^{x_i}}{\sum_je^{x_j}}$, $i,j$ is class not sample
    - [Sigmoid](./sigmoid.py) $sigmoid(x) = \frac{1}{1+e^{-x}}$

- Loss function:
    - [Logistic Loss](./logistic_loss.py) $- (y\cdot log y' + (1-y)\cdot log(1-y'))$

- Training:
    - [Gradient Descend]

- Evaluation:
    - [auc_roc](./auc_roc.py): sort by prediction -> start from high -> suppose threshold is this pred -> add area (梯形) compared to prev
    - [auc_pr]

### Syntax
- Random
    - `random()`: float, [0,1]
    - `uniform(a, b)`: float, [a,b]
    - `randint(a, b)`: int, [a,b]
    - `randrange(start, stop[, step])`: select from list, start, start+step, .... stop
    - `choice(seq)`: pick one from seq
    - `choices(seq, weight=None, *, cum_weights=None, k=1)`: pick from seq k elements with weight
    - `shuffle(x[, random])`: shuffle x
    - `sample(x, k)`: pick from x k elements and form a new list
- Numpy
    - Zero, One
        - np.ones(shape, dtype=None)
        - np.ones_like(a, dtype=None)
    - Random
        - np.random.rand(*shape)
- PyTorch

    
