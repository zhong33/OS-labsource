#-*- encoding: utf-8 -*-
# target: 模拟和验证辅存空间位示图算法的实现过程
import random

class Node:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.a = []         # 块号
        self.zihao = []     # 字号
        self.weihao = []    # 位号
        self.zhu = []       # 柱面号
        self.citou = []     # 磁头号
        self.shanqu = []    # 扇区号
    
    def out(self):
        print("*"*15 + "打印{}作业在辅存中的信息".format(self.name) + "*"*15)
        s = "%4s"%("记录") + "%8s"%("块号") + "%8s"%("柱面号") + "%8s"%("磁头号") + "%8s"%("扇区号")
        print(s)
        for i in range(self.size):
            s = ""
            s += "%5d"%(i+1) + "%10d"%self.a[i] + "%10d"%self.zhu[i] + "%10d"%self.citou[i] + "%10d"%self.shanqu[i]
            print(s)
    
class Disk:
    def __init__(self, size, wordlen, blocklen, tracksum, sectorsum):
        self.size = size
        self.a = [random.randint(0,1) for i in range(self.size // self.blocklen)]
        self.wordlength = wordlen
        self.blocklen = blocklen
        self.tracksum = tracksum
        self.sectorsum = sectorsum
        self.jobname = []       # 作业名列表
        self.job = []           # 作业列表
    
    def out(self):
        s = "   "
        for i in range(self.wordlength):
            s += ("%3d"%i)
        print(s)
        for i in range(self.size // (self.wordlength * self.blocklen) + 1):
            s = ""
            s += ("%3d"%i)
            for j in self.a[i*64:(i+1)*64]:
                s += ("%3d"%j)
            print(s)
        print("辅存剩余空块数：{}".format(self.a.count(0)))
    
    def distribute(self):
        print("*"*20 + "打印内存空间情况" + "*"*20)
        self.out()
        input1 = [_ for _ in input("请输入申请空间的作业名字和需要分配辅存空间的大小：").split()]
        if int(input1[1]) <= self.a.count(0) and self.jobname.count(input1[0]) == 0:
            node = Node(input1[0], int(input1[1]))
            tmp = node.size
            for i in range(len(self.a)):
                if self.a[i] == 0 and tmp > 0:
                    self.a[i] = 1
                    node.zhu.append(0)
                    node.citou.append(i // self.sectorsum)
                    node.shanqu.append(i % self.sectorsum)
                    node.a.append(i)
                    tmp -= 1
            self.jobname.append(node.name)
            self.job.append(node)
            print("内存分配成功！")
            print("*"*20 + "打印内存空间情况" + "*"*20)
            self.out()
            node.out()
        else:
            print("出现错误，分配失败！")
        
    def recycle(self):
        s = ""
        for i in self.jobname:
            s += (i + "->")
        s = s[:-2]
        print("当前分配的作业：{}".format(s))
        name = input("请输入你当前要回收的作业名：")
        if self.jobname.count(name) == 1:
            for i in self.job[self.jobname.index(name)].a:
                self.a[i] = 0
            self.job[self.jobname.index(name)].size = 0
            self.job[self.jobname.index(name)].out()
            del self.job[self.jobname.index(name)]
            self.jobname.remove(name)
            print("该作业无存储信息！回收成功！")
            self.out()
        else:
            print("出现错误，回收失败！")

def main():
    input1 = [int(_) for _ in input("请输入辅存空间的大小（单位：K）和字长（32 or 64）和块长（单位：K）：").split()]
    input2 = [int(_) for _ in input("请输入该辅存硬盘的磁道数（磁头数）、每磁道的扇区数：").split()]
    disk = Disk(input1[0], input1[1], input1[2], input2[0], input2[1])
    print("*"*20 + "辅存初始位示图如下" + "*"*20)
    disk.out()
    while True:
        print("*"*15 + "辅存管理" + "*"*15)
        print("\t*\t1.空间分配\t*")
        print("\t*\t2.空间去配\t*")
        print("\t*\t0.退出    \t*")
        opt = int(input("\t\t请输入选项[ ]\b\b"))
        if not opt:
            break
        elif opt == 1:
            disk.distribute()
        elif opt == 2:
            disk.recycle()

if __name__ == "__main__":
    main()

'''
1000 64 1
8 96
1
job1 50
1
job2 80
2
job1
2
job2
'''