#-*- encoding: utf-8 -*-
# target: 作业调度FCFS算法

class queue:
    def __init__(self):
        self.queue = []
    
    # 插入数据，新建队列
    def buildQue(self):
        num = int(input("请输入你需要创建的作业数："))
        print("请依次输入：\n作业名   入井时间   运行时间：")
        for i in range(num):
            data = [_ for _ in input().split()]
            node = process(data[0], data[1], int(data[2]))
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
        print("\n模拟作业FCFS调度过程输出结果：")
        print("名字  到达时间  运行时间  作业调度时间      作业调度等待时间  进程调度时间  进程调度等待时间  完成时间     周转时间（分钟）  带权周转系数：")
        for now in self.queue:
            print("{:5}  {:5}\t{:5}\t     {:5}\t\t{:5}\t\t{:5}\t\t{:5}\t\t{:5}\t\t{:5}\t\t{:.4f}".format(now.name, now.arrive, now.zx, now.start, now.wait, now.start, 0, now.finish, now.zz, now.zzxs))
            zzsum += now.zz
            zzzqsum += now.zzxs
        print("系统平均周转周期时间为：\t\t\t\t\t\t\t\t\t\t\t\t%.2f" % (zzsum / len(self.queue)))
        print("系统带权平均周转周期为：\t\t\t\t\t\t\t\t\t\t\t\t\t\t%.4f" % (zzzqsum / len(self.queue)))

class process:
    def __init__(self, name, arrive, zx):
        self.name = name
        self.arrive = arrive
        self.zx = zx
        self.start = None
        self.finish = None
        self.zz = None
        self.zzxs = None
        self.wait = None

def fcfs(q):
    h = int(q.queue[0].arrive.split(":")[0])
    m = int(q.queue[0].arrive.split(":")[1])
    # 循环从头开始计算时间
    for now in q.queue:
        if (h*60 + m) > (int(now.arrive.split(":")[0])*60 + int(now.arrive.split(":")[1])):
            now.start = str(h) + ":" + str(m).zfill(2)
        else:
            now.start = now.arrive
        h = finshh = int(now.start.split(":")[0]) + (int(now.start.split(":")[1]) + now.zx)//60
        m = finshm = (int(now.start.split(":")[1]) + now.zx) % 60
        now.finish = str(finshh) + ":" + str(finshm).zfill(2)
        now.wait = int(now.start.split(":")[0])*60 + int(now.start.split(":")[1]) - int(now.arrive.split(":")[0])*60 - int(now.arrive.split(":")[1])
        now.zz = finshh*60 + finshm - int(now.arrive.split(":")[0])*60 - int(now.arrive.split(":")[1])
        now.zzxs = round(now.zz / now.zx, 4)
    return q


def main():
    q = queue()
    q.buildQue()
    q = fcfs(q)
    q.output()

if __name__ == "__main__":
    main()

"""
4
JOB1      8:00         120
JOB2      8:50         50
JOB3      9:00         10
JOB4      9:50         20
"""