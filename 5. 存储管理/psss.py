#-*- encoding: utf-8 -*-
# target: 模拟和验证分页/分段/段页存储管理方式的分配与回收
import random

class Section:
    pass

class SectionStorage:
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
            s = Section()
            s.main()
        elif opt == 3:
            ss = SectionStorage()
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
'''