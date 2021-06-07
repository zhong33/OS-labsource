#-*- encoding: utf-8 -*-
# target: 模拟和验证分页/分段/段页存储管理方式的分配与回收
import random

class Segment:
    def __init__(self):
        print("*"*15 + "段式管理模拟" + "*"*15)
        self.size = int(input("请输入内存大小为："))
        self.start = int(input("请输入起始地址大小为："))
        self.use = []
        self.free = []

    def main(self):
        self.free.append([self.size, self.start, "空闲"])
        while True:
            print("*"*15 + "段式存储管理" + "*"*15)
            print("\t*\t1.内存分配\t*")
            print("\t*\t2.内存去配\t*")
            print("\t*\t0.退出    \t*")
            opt = int(input("\t\t请输入选项[ ]\b\b"))
            if not opt:
                break
            elif opt == 1:
                print("*"*20 + "分配算法" + "*"*20)
                print("\t*\t1.最先分配法\t*")
                print("\t*\t2.最优分配法\t*")
                print("\t*\t3.最坏分配法\t*")
                opt1 = int(input("\t\t请输入选项[ ]\b\b"))
                self.output()
                if opt1 == 1:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    part = int(input("请输入分成几段："))
                    tmp = 0
                    for i in range(part):
                        flag = 1
                        tmp = int(input("剩余{}K的内存，请输入第{}段的大小（单位：KB）：".format(int(data[1]) - tmp, i+1)))
                        # 直接遍历free，最先分配
                        for now in self.free:
                            if int(data[1]) < now[0]:
                                work = [tmp, now[1], data[0]+"(%s)"%str(i)]
                                self.use.append(work)
                                self.use.sort(key=lambda x:x[1])
                                now[0] -= tmp
                                now[1] += tmp
                                print("分配成功！")
                                flag = 0
                                self.free.sort(key=lambda x:x[1])
                                self.output()
                                break
                    if flag:
                        print("发生错误，分配失败！")
                elif opt1 == 2:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    part = int(input("请输入分成几段："))
                    tmp = 0
                    for i in range(part):
                        flag = 1
                        tmp = int(input("剩余{}K的内存，请输入第{}段的大小（单位：KB）：".format(int(data[1]) - tmp, i+1)))
                        # 先对free进行大小的升序排序，再进行分配，最优分配
                        self.free.sort(key=lambda x:x[0])
                        for now in self.free:
                            if int(data[1]) < now[0]:
                                work = [tmp, now[1], data[0]+"(%s)"%str(i)]
                                self.use.append(work)
                                self.use.sort(key=lambda x:x[1])
                                now[0] -= tmp
                                now[1] += tmp
                                print("分配成功！")
                                flag = 0
                                self.free.sort(key=lambda x:x[1])
                                self.output()
                                break
                    if flag:
                        print("发生错误，分配失败！")
                elif opt1 == 3:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    part = int(input("请输入分成几段："))
                    tmp = 0
                    for i in range(part):
                        flag = 1
                        tmp = int(input("剩余{}K的内存，请输入第{}段的大小（单位：KB）：".format(int(data[1]) - tmp, i+1)))
                        # 先对free进行大小的降序排序，再进行分配，最坏分配
                        self.free.sort(key=lambda x:x[0], reverse=True)
                        for now in self.free:
                            if int(data[1]) < now[0]:
                                work = [tmp, now[1], data[0]+"(%s)"%str(i)]
                                self.use.append(work)
                                self.use.sort(key=lambda x:x[1])
                                now[0] -= tmp
                                now[1] += tmp
                                print("分配成功！")
                                flag = 0
                                self.free.sort(key=lambda x:x[1])
                                self.output()
                                break
                    if flag:
                        print("发生错误，分配失败！")
            elif opt == 2:
                self.output()
                workName = input("请输入你要回收的作业名：")
                flag = 1
                for i in range(len(self.use)):
                    for now in self.use:
                        # 寻找作业名
                        if now[2].startswith(workName):
                            now[2] = "空闲"
                            # 判断是否有上界和下界
                            for nowFree in self.free:
                                # 上有空闲
                                if now[0] + now[1] == nowFree[1]:
                                    nowFree[1] = now[1]
                                    self.check()
                                    self.use.remove(now)
                                    break
                                # 下有空闲
                                elif nowFree[0] + nowFree[1] == now[1]:
                                    nowFree[0] += now[0]
                                    self.check()
                                    self.use.remove(now)
                                    break
                                # 上下都无空闲
                                else:
                                    self.free.append(now)
                                    self.use.remove(now)
                                    self.free.sort(key=lambda x:x[1])
                                    self.check()
                                    break
                            flag = 0
                if not flag:
                    print("回收成功！")
                    self.output()
                else:
                    print("发生错误，回收失败！")

    # 输出函数
    def output(self):
        print("\n" + "*"*20 + "主存分配情况" + "*"*20)
        print("已分配：\n分区号\t大小(KB)\t起始(KB)\t状态")
        i = 1
        for now in self.use:
            print("{}\t{}\t\t{}\t\t{}".format(i, now[0],now[1],now[2]))
            i += 1
        print("未分配：\n分区号\t大小(KB)\t起始(KB)\t状态")
        for now in self.free:
            print("{}\t{}\t\t{}\t\t{}".format(i, now[0],now[1],now[2]))
            i += 1

    # 对free进行check，判断是否存在相连分区
    def check(self):
        for i in range(len(self.free) - 1, 0, -1):
            if self.free[i-1][0] + self.free[i-1][1] == self.free[i][1]:
                self.free[i-1][0] += self.free[i][0]
                self.free.remove(self.free[i])

class SegmentStorage:
    def __init__(self):
        pass

    def main(self):
        pass

class Node:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.a = []
    
    def out(self):
        print("*"*15 + "打印{}作业在辅存中的信息".format(self.name) + "*"*15)
        s = "%4s"%("记录") + "%8s"%("块号")
        print(s)
        for i in range(self.size):
            s = ""
            s += "%5d"%(i+1) + "%10d"%self.a[i]
            print(s)

class Page:
    def __init__(self):
        print("*"*15 + "分页式管理模拟" + "*"*15)
        data = [int(_) for _ in input("请输入系统内存空间的大小（单位：K）和字长（32 or 64）和块长（单位：K）：").split()]
        self.size = data[0]
        self.wordlen = data[1]
        self.blocklen = data[2]
        self.a = [random.randint(0,1) for i in range(self.size // self.blocklen)]
        self.jobname = []
        self.job = []

    def out(self):
        print("*"*20 + "打印内存空间情况" + "*"*20)
        s = "   "
        for i in range(self.wordlen):
            s += ("%3d"%i)
        print(s)
        for i in range(self.size // (self.wordlen * self.blocklen) + 1):
            s = ""
            s += ("%3d"%i)
            for j in self.a[i*64:(i+1)*64]:
                s += ("%3d"%j)
            print(s)
        print("剩余空块数：{}".format(self.a.count(0)))

    def distribute(self):
        self.out()
        input1 = [_ for _ in input("请输入申请空间的作业名字和需要分配辅存空间的大小：").split()]
        if int(input1[1]) <= self.a.count(0) and self.jobname.count(input1[0]) == 0:
            node = Node(input1[0], int(input1[1]))
            tmp = node.size
            for i in range(len(self.a)):
                if self.a[i] == 0 and tmp > 0:
                    self.a[i] = 1
                    node.a.append(i)
                    tmp -= 1
            self.jobname.append(node.name)
            self.job.append(node)
            print("内存分配成功！")
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

    def main(self):
        self.out()
        while True:
            print("*"*15 + "分页式管理模拟" + "*"*15)
            print("\t*\t1.空间分配\t*")
            print("\t*\t2.空间去配\t*")
            print("\t*\t0.退出    \t*")
            opt = int(input("\t\t请输入选项[ ]\b\b"))
            if not opt:
                break
            elif opt == 1:
                self.distribute()
            elif opt == 2:
                self.recycle()

def main():
    while True:
        print("*"*15 + "模拟存储管理" + "*"*15)
        print("\t*\t1.分页式算法\t*")
        print("\t*\t2.分段式算法\t*")
        print("\t*\t3.段页式算法\t*")
        print("\t*\t0.退出    \t*")
        opt = int(input("\t\t请输入选项[ ]\b\b"))
        if not opt:
            break
        elif opt == 1:
            p = Page()
            p.main()
        elif opt == 2:
            s = Segment()
            s.main()
        elif opt == 3:
            ss = SegmentStorage()
            ss.main()

if __name__ == "__main__":
    main()

'''
1
2000 64 2
1
job1 50
1
job2 80
2
job2
2
job1

2
256
40
1
1
jobA 50
2
20
30
1
2
jobB 80
2
10
70
2
jobA
2
jobB
0
0
'''