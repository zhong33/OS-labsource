#-*- encoding: utf-8 -*-
# target: 服务进程调度算法

class queue:
    def __init__(self):
        self.queue = []
    
    def buildQue(self):
        print("ID号 名字 到达时间 执行时间（分钟）：")
        while 1:
            data = [_ for _ in input().split()]
            if data[0] == "-1":
                break
            node = process(data[0], data[1], data[2], int(data[3]))
            if len(self.queue) == 0:
                self.queue.append(node)
            else:
                for i in range(len(self.queue)):
                    if (int(node.arrive.split(":")[0])*60 + int(node.arrive.split(":")[1])) >= (int(self.queue[i].arrive.split(":")[0])*60 + int(self.queue[i].arrive.split(":")[1])):
                        break
                self.queue.insert(i,node)
        self.queue.reverse()
        
    def output(self):
        zzsum = zzzqsum = 0
        print("模拟进程FCFS调度过程输出结果：")
        print("ID号   名字  到达时间  执行时间（分钟）  开始时间  完成时间  周转时间（分钟）  带权周转系数：")
        for now in self.queue:
            print("{:5}  {:5}  {:5}\t{:5}\t\t  {:5}     {:5}\t{:5}\t\t{:.2f}".format(now.id, now.name, now.arrive, now.zx, now.start, now.finish, now.zz, now.zzxs))
            zzsum += now.zz
            zzzqsum += now.zzxs
        print("系统平均周转周期时间为：%.2f" % (zzsum / len(self.queue)))
        print("系统带权平均周转周期为：%.2f" % (zzzqsum / len(self.queue)))

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

def fcfs(q):
    h = int(q.queue[0].arrive.split(":")[0])
    m = int(q.queue[0].arrive.split(":")[1])
    for now in q.queue:
        if (h*60 + m) > (int(now.arrive.split(":")[0])*60 + int(now.arrive.split(":")[1])):
            now.start = str(h) + ":" + str(m).zfill(2)
        else:
            now.start = now.arrive
        h = finshh = int(now.start.split(":")[0]) + (int(now.start.split(":")[1]) + now.zx)//60
        m = finshm = (int(now.start.split(":")[1]) + now.zx) % 60
        now.finish = str(finshh) + ":" + str(finshm).zfill(2)
        now.zz = finshh*60 + finshm - int(now.arrive.split(":")[0])*60 - int(now.arrive.split(":")[1])
        now.zzxs = round(now.zz / now.zx, 2)
    return q


def main():
    q = queue()
    q.buildQue()
    q = fcfc(q)
    q.output()

if __name__ == "__main__":
    main()

# 1001  p1     8:40    20
# 1004  p4    10:10    10
# 1005  p5    10:05    30
# 1002  p2     9:55    15
# 1003  p3     9:45    25
# -1