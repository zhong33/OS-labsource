#-*- encoding: utf-8 -*-
# target: 页面置换算法

class Storage:
    def __init__(self):
        self.block = None
    
    def build(self):
        self.block = int(input("请输入物理块的块数："))

    def input(self):
        self.job = input("请输入作业名：")
        self.len = int(input("请输入作业页面的长度："))
        self.list = [int(_) for _ in input("请输入作业页面的顺序：").split()]

    def out(self):
        s = "   "
        for i in range(self.len):
            s += ("%3d"%i)
        print(s)
        s = "   "
        for i in self.list:
            s += ("%3d"%i)
        print(s)

    def fifo(self):
        self.input()
        print("*"*15 + "打印作业FIFO调度进入主存页的过程" + "*"*15)
        print("作业名：{}\n作业调度过程".format(self.job))
        self.out()
        brk, res, tmp = 0, [], []
        for i in self.list:
            if tmp.count(i) == 0:
                tmp.insert(0, i)
                if len(tmp) >= self.block:
                    tmp = tmp[:self.block]
                res.append(tmp.copy())
            else:
                res.append(tmp.copy())
        for i in range(self.block):
            s = "%3d"%i
            for j in res:
                try:
                    s += "%3d"%j[i]
                except:
                    s += "   "
            print(s)
        tmp = []
        s = "   "
        for i in res:
            if set(i) != set(tmp):
                s += "%3s"%"+"
                tmp = i
                brk += 1
            else:
                s += "   "
        print(s)
        print("缺页中断率为：{}".format(round(100*brk / self.len, 2)))

    def lru(self):
        self.input()
        print("*"*15 + "打印作业FIFO调度进入主存页的过程" + "*"*15)
        print("作业名：{}\n作业调度过程".format(self.job))
        self.out()
        brk, res, tmp = 0, [], []
        for i in self.list:
            if tmp.count(i) == 0:
                tmp.insert(0, i)
                if len(tmp) >= self.block:
                    tmp = tmp[:self.block]
                res.append(tmp.copy())
            else:
                tmp.remove(i)
                tmp.insert(0, i)
                res.append(tmp.copy())
        for i in range(self.block):
            s = "%3d"%i
            for j in res:
                try:
                    s += "%3d"%j[i]
                except:
                    s += "   "
            print(s)
        tmp = []
        s = "   "
        for i in res:
            if set(i) != set(tmp):
                s += "%3s"%"+"
                tmp = i
                brk += 1
            else:
                s += "   "
        print(s)
        print("缺页中断率为：{}".format(round(100*brk / self.len, 2)))

def main():
    s = Storage()
    s.build()
    while True:
        print("*"*15 + "请求分页式存储管理" + "*"*15)
        print("\t*\t1.FIFO分配\t*")
        print("\t*\t2.LRU(LFU)分配\t*")
        print("\t*\t0.退出    \t*")
        opt = int(input("\t\t请输入选项[ ]\b\b"))
        if not opt:
            break
        elif opt == 1:
            s.fifo()
        elif opt == 2:
            s.lru()

if __name__ == "__main__":
    main()

'''
3
1
job1
20
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
2
job2
20
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1

4
1
job3
20
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
2
job4
20
7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
'''