#-*- encoding: utf-8 -*-
# target: 磁盘移臂调度算法

class Storage:
    def __init__(self):
        self.size = None
        self.list = []
        self.now = None
    
    def build(self):
        self.size = int(input("请输入访问序列的长度："))
        self.list = [int(_) for _ in input("请输入访问的柱面顺序：").split()]
        self.now = int(input("请输入正在访问的页面："))

    def fcfs(self):
        s, res, last = 0, [53], self.now
        for i in self.list:
            s += abs(i - last)
            last = i
            res.append(i)
        print("*"*10 + "FCFS磁盘移臂调度过程" + "*"*10)
        print("移动的顺序为：\n{}\n移动柱面为：{}\n".format(res, s))
    
    def sstf(self):
        s, m, mnum, res, last = 0, 9999, 0, [53], self.now
        flags = [0] * len(self.list)
        for j in range(len(self.list)):
            for i in self.list:
                if abs(i - last) < m and flags[self.list.index(i)] == 0:
                    m = abs(i - last)
                    mnum = i
            flags[self.list.index(mnum)] = 1
            s += m
            last = mnum
            res.append(mnum)
            m = 9999
        print("*"*10 + "SSTF磁盘移臂调度过程" + "*"*10)
        print("移动的顺序为：\n{}\n移动柱面为：{}\n".format(res, s))

    def elevator(self):
        s1, s2, index, res1, res2, last = 0, 0, 0, [53], [53], self.now
        self.list.sort()
        for i in self.list:
            if i < self.now:
                index = self.list.index(i)
        for i in self.list[:index + 1][::-1]:
            res1.append(i)
            s1 += abs(i - last)
            last = i
        for i in self.list[index + 1:]:
            res1.append(i)
            s1 += abs(i - last)
            last = i
        last = self.now
        for i in self.list[index + 1:]:
            res2.append(i)
            s2 += abs(i - last)
            last = i
        for i in self.list[:index + 1][::-1]:
            res2.append(i)
            s2 += abs(i - last)
            last = i
        print("*"*10 + "电梯磁盘移臂调度过程" + "*"*10)
        print("由里向外移动的顺序为：\n{}\n移动柱面为：{}".format(res1, s1))
        print("由外向里移动的顺序为：\n{}\n移动柱面为：{}".format(res2, s2))

def main():
    s = Storage()
    s.build()
    s.fcfs()
    s.sstf()
    s.elevator()

if __name__ == "__main__":
    main()

'''
8
98 183 37 122 14 124 65 67
53
'''
