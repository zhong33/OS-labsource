#-*- encoding: utf-8 -*-
# target: 时间片轮转调度算法

import time

class process:
    def __init__(self, id, name, arrive, zx):
        self.id = id
        self.name = name
        self.arrive = arrive
        self.zx = zx
        self.start = None
        self.finish = None
        self.zz = None
        self.zzxs = None
        self.nowstart = None
        self.donetime = 0
        self.retime = zx

class queue:
    def __init__(self):
        self.queue = []
        self.num = None
        self.time = None

    # 插入数据，新建队列
    def buildQue(self):
        self.num = int(input("请输入进程数："))
        self.time = int(input("请输入时间片的时间："))
        print("请输入%d个进程的：" % self.num)
        print("ID号 名字 到达时间 执行时间（分钟）：")
        for i in range(self.num):
            data = [_ for _ in input().split()]
            node = process(data[0], data[1], data[2], int(data[3]))
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
        print("\n模拟进程时间片轮转调度算法过程输出结果：")
        print("ID号   名字  到达时间  执行时间（分钟）  首次开始时间  完成时间  周转时间（分钟）  带权周转系数：")
        for now in self.queue:
            print("{:5}  {:5}  {:5}\t{:5}\t\t  {:5}         {:5}\t  {:5}\t\t       {:.2f}".format(now.id, now.name, now.arrive, now.zx, now.start, now.finish, now.zz, now.zzxs))
            zzsum += now.zz
            zzzqsum += now.zzxs
        print("系统平均周转周期时间为：\t\t\t\t\t   %.2f" % (zzsum / len(self.queue)))
        print("系统带权平均周转周期为：\t\t\t\t\t\t\t       %.2f" % (zzzqsum / len(self.queue)))

def rr(q):
    i = 1
    # 结果队列
    res = queue()
    # 就绪队列
    readyq = queue()
    readyq.queue.append(q.queue[0])
    readyq.queue[0].start = readyq.queue[0].nowstart = readyq.queue[0].arrive
    del q.queue[0]
    while readyq.queue:
        t = q.time if readyq.queue[0].retime >= q.time else readyq.queue[0].retime
        readyq.queue[0].donetime += t
        readyq.queue[0].retime -= t
        h = int(readyq.queue[0].nowstart.split(":")[0]) + (int(readyq.queue[0].nowstart.split(":")[1]) + t) // 60
        m = (int(readyq.queue[0].nowstart.split(":")[1]) + t) % 60
        tmp = str(h) + ":" + str(m).zfill(2)
        if readyq.queue[0].start == None:
            readyq.queue[0].start = readyq.queue[0].nowstart
        # 寻找添加进程至就绪队列
        for now in q.queue[:]:
            if (int(now.arrive.split(":")[0])*60 + int(now.arrive.split(":")[1])) <= (int(tmp.split(":")[0])*60 + int(tmp.split(":")[1])):
                readyq.queue.append(now)
                q.queue.remove(now)
        print("\n第%d轮执行和就绪队列结果：" % i)
        print("ID号   名字  到达时间  总执行时间（分钟）  当前开始时间  已完成时间  剩余完成时间：")
        for now in readyq.queue:
            if now == readyq.queue[0]:
                tmp = now.nowstart
            else:
                tmp = "0:00"
            print("{:5}  {:5}  {:5}\t{:5}\t\t\t{:5}     {:5}\t\t{:5}".format(now.id, now.name, now.arrive, now.zx, tmp, now.donetime, now.retime))
        i += 1
        readyq.queue[0].nowstart = str(h) + ":" + str(m).zfill(2)
        time.sleep(1)
        # 将执行完毕的进程从就绪队列删除
        if readyq.queue[0].retime == 0:
            timenow = readyq.queue[0].nowstart
            readyq.queue[0].finish = timenow
            readyq.queue[0].zz = int(timenow.split(":")[0])*60 + int(timenow.split(":")[1]) - int(readyq.queue[0].arrive.split(":")[0])*60 - int(readyq.queue[0].arrive.split(":")[1])
            readyq.queue[0].zzxs = round(readyq.queue[0].zz / readyq.queue[0].zx, 2)
            res.queue.append(readyq.queue[0])
            del readyq.queue[0]
            if readyq.queue:
                readyq.queue[0].nowstart = timenow
        else:
            timenow = readyq.queue[0].nowstart
            readyq.queue.append(readyq.queue[0])
            del readyq.queue[0]
            readyq.queue[0].nowstart = timenow
    return res

def main():
    q = queue()
    q.buildQue()
    q = rr(q)
    q.output()

if __name__ == "__main__":
    main()

# 5
# 8
# 1001  p1     9:40    20
# 1004  p4    10:10    10
# 1005  p5    10:05    30
# 1002  p2     9:55    15
# 1003  p3     9:45    25