#-*- encoding: utf-8 -*-
# target: 优先级调度算法

class process:
    def __init__(self, id, name, good, arrive, zx):
        self.id = id
        self.name = name
        self.good = good
        self.arrive = arrive
        self.zx = zx
        self.start = None
        self.finish = None
        self.zz = None
        self.zzxs = None

class queue:
    def __init__(self):
        self.queue = []

    # 插入数据，新建队列
    def buildQue(self):
        print("ID号 名字 优先级 到达时间 执行时间（分钟）：")
        while 1:
            data = [_ for _ in input().split()]
            if data[0] == "-1":
                break
            node = process(data[0], data[1], int(data[2]), data[3], int(data[4]))
            if len(self.queue) == 0:
                self.queue.append(node)
            else:
                # 找位置，排序插入
                for i in range(len(self.queue)):
                    if (int(node.arrive.split(":")[0])*60 + int(node.arrive.split(":")[1])) >= (int(self.queue[i].arrive.split(":")[0])*60 + int(self.queue[i].arrive.split(":")[1])):
                        break
                self.queue.insert(i,node)
        self.queue.reverse()
    
    # 队列输出
    def output(self):
        zzsum = zzzqsum = 0
        print("模拟进程优先级调度过程输出结果：")
        print("ID号   名字  优先级  到达时间  执行时间（分钟）  开始时间  完成时间  周转时间（分钟）  带权周转系数：")
        for now in self.queue:
            print("{:5}  {:5}  {:2}      {:5}\t{:5}\t\t  {:5}     {:5}\t{:5}\t\t{:.2f}".format(now.id, now.name, now.good, now.arrive, now.zx, now.start, now.finish, now.zz, now.zzxs))
            zzsum += now.zz
            zzzqsum += now.zzxs
        print("系统平均周转周期时间为：\t\t\t\t\t\t%.2f" % (zzsum / len(self.queue)))
        print("系统带权平均周转周期为：\t\t\t\t\t\t\t\t%.2f" % (zzzqsum / len(self.queue)))

# 优先级调度算法
def ps(q):
    res = queue()
    # res 为新建队列，插入新的节点
    q.queue[0].start = q.queue[0].arrive
    finshh = int(q.queue[0].start.split(":")[0]) + (int(q.queue[0].start.split(":")[1]) + q.queue[0].zx)//60
    finshm = (int(q.queue[0].start.split(":")[1]) + q.queue[0].zx) % 60
    q.queue[0].finish = str(finshh) + ":" + str(finshm).zfill(2)
    q.queue[0].zz = finshh*60 + finshm - int(q.queue[0].arrive.split(":")[0])*60 - int(q.queue[0].arrive.split(":")[1])
    q.queue[0].zzxs = round(q.queue[0].zz / q.queue[0].zx, 2)
    res.queue.append(q.queue[0])
    del q.queue[0]
    while q.queue:
        tmp = []
        # 找出来在 res 最后一个节点 finish time 前到达的进程
        for now in q.queue:
            if (int(now.arrive.split(":")[0])*60 + int(now.arrive.split(":")[1])) <= (int(res.queue[-1].finish.split(":")[0])*60 + int(res.queue[-1].finish.split(":")[1])):
                tmp.append(now)
        maxgood = tmp[0]
        # 找出来这些进程中优先级最高的那个
        for now in tmp:
            if now.good > maxgood.good:
                maxgood = now
        maxgood.start = res.queue[-1].finish
        finshh = int(res.queue[-1].finish.split(":")[0]) + (int(res.queue[-1].finish.split(":")[1]) + maxgood.zx)//60
        finshm = (int(res.queue[-1].finish.split(":")[1]) + maxgood.zx) % 60
        maxgood.finish = str(finshh) + ":" + str(finshm).zfill(2)
        maxgood.zz =  finshh*60 + finshm - int(maxgood.arrive.split(":")[0])*60 - int(maxgood.arrive.split(":")[1])
        maxgood.zzxs = round(maxgood.zz / maxgood.zx, 2)
        res.queue.append(maxgood)
        q.queue.remove(maxgood)
    return res

def main():
    q = queue()
    q.buildQue()
    q = ps(q)
    q.output()

if __name__ == "__main__":
    main()

# 1001  p1    1      9:40      20
# 1004  p4    4     10:10      10
# 1005  p5    3     10:05      30
# 1002  p2    3      9:55      15
# 1003  p3    2      9:45      25
# -1