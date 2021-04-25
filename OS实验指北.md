# OS 实验指北

* [第二章 进程管理](#ch2)
  * [实验一：进程调度算法](#ch2-lab1)
    1. [FCFS](#ch2-lab1-fcfs)
    2. [优先级调度](#ch2-lab1-ps)
    3. [时间片轮转调度](#ch2-lab1-rr)

## <span id="ch2">第二章 进程管理</span>

### <span id="ch2-lab1">实验一：进程调度算法</span>

#### <span id="ch2-lab1-fcfs">1. FCFS</span>

​		本实验是模拟进程调度中的先来先服务算法，每次CPU都是按照进入就绪队列的先后次序依次选中一个进程装入CPU运行，等结束时再选取下一个。

​		进程类成员变量

```python
self.id = id			# 编号
self.name = name		# 进程名
self.arrive = arrive	# 到达就绪队列时间
self.zx = zx			# 执行时间
self.start = None		# 开始时间
self.finish = None		# 完成时间
self.zz = None			# 周转时间 = 完成时间 - 到达时间
self.zzxs = None		# 带权周转系数 = 周转时间 / 执行时间
```

​		函数包括：

* `queue.buildQue()`：构建队列
* `queue.output()`：打印函数
* `fcfs()`：先来先服务算法

​		实验结果：

![image-20210425160048728](C:\Users\ieven\AppData\Roaming\Typora\typora-user-images\image-20210425160048728.png)

​		程序流程图：

```flow
st=>start: 开始
e=>end: 结束
inputID=>operation: 输入进程ID
judgeID=>condition: ID == -1
op1=>operation: 新建一个进程对象，并输
入其信息对其进行初始化
op2=>operation: 将进程对象按照到达时间按序插入就绪队列
fcfsop1=>operation: now = 就绪队列头
fcfsop2=>operation: 计算进程相关信息
fcfsop3=>operation: now = now->next
fcfsjudge1=>condition: now == NULL
output=>operation: 输出信息
st->inputID->judgeID
judgeID(yes)(left)->fcfsop1->fcfsjudge1
judgeID(no)->op1(bottom)->op2(right)->inputID
fcfsjudge1(yes)->output->e
fcfsjudge1(no)->fcfsop2(right)->fcfsop3(top)->fcfsjudge1
```

---

#### <span id="ch2-lab1-ps">2. 优先级调度</span>

​		本实验是模拟进程调度中的优先级调度算法，CPU先看当前有哪些进程进入了就绪队列，再从其中选去优先级最高的一个进程装入CPU运行，等结束之后重复上述过程。

​		进程类成员变量

```python
self.id = id			# 编号
self.name = name		# 进程名
self.good = good		# 优先级
self.arrive = arrive	# 到达就绪队列时间
self.zx = zx			# 执行时间
self.start = None		# 开始时间
self.finish = None		# 完成时间
self.zz = None			# 周转时间 = 完成时间 - 到达时间
self.zzxs = None		# 带权周转系数 = 周转时间 / 执行时间
```

​		函数包括：

* `queue.buildQue()`：构建队列

* `queue.output()`：打印函数

* `ps()`：优先级调度算法

  实验结果：

![image-20210425164506637](C:\Users\ieven\AppData\Roaming\Typora\typora-user-images\image-20210425164506637.png)

​		程序流程图：

```flow
st=>start: 开始
e=>end: 结束
inputID=>operation: 输入进程ID
judgeID=>condition: ID == -1
op1=>operation: 新建一个进程对象，并输
入其信息对其进行初始化
op2=>operation: 将进程对象按照到达时间按序插入就绪队列
psop00=>operation: 就绪队列头出队列
进入结果队列
psop0=>operation: 计算就绪队列第一
个进程的相关信息
psop1=>operation: now = 就绪队列头
psop2=>operation: 找出在结果队列队尾元素执行完毕时间之前
到达就绪队列的进程，并取出其中优先级最高的进程进行计算
psop3=>operation: now = now->next
psop4=>operation: 将该进程出就绪队列
入结果队列
psjudge1=>condition: now == NULL
output=>operation: 输出信息
st->inputID->judgeID
judgeID(yes)->psop0->psop00->psop1->psjudge1
judgeID(no)->op1(bottom)->op2(right)->inputID
psjudge1(yes)->output->e
psjudge1(no)->psop2(right)->psop4(bottom)->psop3(right)->psjudge1
```

---

#### <span id="ch2-lab1-rr">3. 时间片轮转调度</span>

​		本实验是模拟进程调度中的时间片轮转算法，首先对所有进程按到达时间排好序，然后逐个对就绪队列中的进程轮流进入CPU执行，每次开始的时间就是上个进程让出CPU的时间，在该进程本轮结束前(含结束时间)，所有入队的进程均按时间先后入队，结束时间到再将该进程排到队列的末尾，从而进入后续循环。

​		进程类成员变量

```python
self.id = id			# 编号
self.name = name		# 进程名
self.arrive = arrive	# 到达就绪队列时间
self.zx = zx			# 执行时间
self.start = None		# 开始时间
self.finish = None		# 完成时间
self.zz = None			# 周转时间 = 完成时间 - 到达时间
self.zzxs = None		# 带权周转系数 = 周转时间 / 执行时间
self.nowstart = None	# 当前开始时间
self.donetime = 0		# 已完成时间
self.retime = zx		# 剩余完成时间
```

​		函数包括：

* `queue.buildQue()`：构建队列

* `queue.output()`：打印函数

* `rr()`：时间片轮转调度算法

  实验结果：

![image-20210425171056765](C:\Users\ieven\AppData\Roaming\Typora\typora-user-images\image-20210425171056765.png)

![image-20210425171012733](C:\Users\ieven\AppData\Roaming\Typora\typora-user-images\image-20210425171012733.png)

​		程序流程图：

```flow
st=>start: 开始
e=>end: 结束
op0=>operation: 输入进程数 num
op00=>operation: 输入单个时间片的时间
op000=>operation: i = 0
op01=>operation: i += 1
inputID=>operation: 输入进程信息
judgeID=>condition: i < num
op1=>operation: 新建一个进程对象，并输
入其信息对其进行初始化
op2=>operation: 将进程对象按照到达时间按序插入输入队列
rrop0=>operation: 输入队列头出队列、入就绪队列
rrop1=>operation: now = 就绪队列头
rrop2=>operation: 进行一次时间片轮转，计算相关信息
rrop21=>operation: 对输入队列进行遍历，寻找到达的队列，
将其入就绪队列
rrop22=>operation: 输出该轮运行信息
rrop3=>operation: now = now->next
rrop4=>operation: 将执行完毕的进程
从就绪队列删除
rrjudge1=>condition: now == NULL
output=>operation: 输出信息
st->op0->op00->op000->inputID->op01->op1(bottom)->op2(right)->judgeID
judgeID(yes)->rrop0->rrop1->rrjudge1
judgeID(no)->inputID
rrjudge1(yes)->output->e
rrjudge1(no)->rrop2(bottom)->rrop21(bottom)->rrop22(right)->rrop4(bottom)->rrop3(right)->rrjudge1
```

