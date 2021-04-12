#-*- encoding: utf-8 -*-
# target: 银行家算法

class OS:
    def __init__(self):
        self.sourceTypeNum = None
        self.processNum = None
        self.available = []
        self.max = []
        self.allocation = []
        self.need = []
        self.flag = []

    def build(self):
        self.sourceTypeNum = int(input("请输入资源种类："))
        self.processNum = int(input("请输入进程数："))
        self.available = [int(_) for _ in input("请输入{}类资源初始化的资源数：".format(self.sourceTypeNum)).split()]
        self.max = []
        self.flag = [0 for _ in range(self.processNum)]
        print("\n请输入{}个进程的：\n进程名         最大需求量：\n               A   B   C".format(self.processNum))
        for i in range(self.processNum):
            self.max.append([int(_) for _ in [_ for _ in input().split()][1:]])
        self.need = [_ for _ in self.max]
        for i in range(self.processNum):
            self.allocation.append([0 for _ in range(self.sourceTypeNum)])
        print("\n请输入{}个进程的：\n进程名         第一次申请量：\n               A   B   C".format(self.processNum))
        for i in range(self.processNum):
            request = [int(_) for _ in [_ for _ in input().split()][1:]]
            temp = [(request[j] + self.allocation[i][j]) for j in range(self.sourceTypeNum)]
            if temp <= self.max[i]:
                if request <= self.available:
                    self.available = [(self.available[j] - request[j]) for j in range(self.sourceTypeNum)]
                    self.allocation[i] = [(self.allocation[i][j] + request[j]) for j in range(self.sourceTypeNum)]
                    self.need[i] = [(self.need[i][j] - request[j]) for j in range(self.sourceTypeNum)]
            if not self.security():
                self.available = [(self.available[j] + request[j]) for j in range(self.sourceTypeNum)]
                self.allocation[i] = [(self.allocation[i][j] - request[j]) for j in range(self.sourceTypeNum)]
                self.need[i] = [(self.need[i][j] + request[j]) for j in range(self.sourceTypeNum)]

    def output(self):
        print("\n进程名\t\t最大需求量\t\t尚需求量\t\t已分配量\t\t执行结束否")
        for i in range(self.processNum):
            status = "working"
            if self.need[i] == [0,0,0]:
                status = "finished"
                if self.flag[i] == 0 :
                    self.flag[i] = 1
                    self.available = [(self.available[j] + self.max[i][j]) for j in range(self.sourceTypeNum)]
            print("进程p[{}]\t{}\t\t{}\t\t{}\t\t{}".format(i + 1, self.max[i], self.need[i], self.allocation[i], status))
        print("资源剩余数：{}\n".format(self.available))

    # 安全性算法
    def security(self):
        self.work = self.available
        finish = [False] * self.processNum
        aqxl = ""
        # 安全序列
        while finish != [True] * self.processNum:
            flag = False
            for i in range(self.processNum):
                if not finish[i] and self.need[i] <= self.work:
                    if self.need[i] != [0] * self.sourceTypeNum:
                        aqxl += "p[{}]-->".format(i+1)
                    flag = True
                    self.work = [(self.work[j] + self.allocation[i][j]) for j in range(self.sourceTypeNum)]
                    finish[i] = True
                    break
            if not flag:
                return False
        print("申请成功！安全序列为：{}".format(aqxl[:-3]))
        return True

    def more(self):
        self.output()
        done = [[0 for i in range(self.sourceTypeNum)] for i in range(self.processNum)]
        while self.need != done:
            judge = input("是否需要再申请资源？（Y/N）")
            if judge == "Y" or judge == "y":
                processId = int(input("请输入进程编号（1-{}）：".format(self.processNum))) - 1
                request = [int(_) for _ in input("请输入进程p[{}]对{}类资源的申请：".format(processId, self.processNum)).split()]
            else:
                exit()
            if request > self.max[processId]:
                print("输入有误，重新输入")
            else:
                self.available = [(self.available[j] - request[j]) for j in range(self.sourceTypeNum)]
                self.allocation[processId] = [(self.allocation[processId][j] + request[j]) for j in range(self.sourceTypeNum)]
                self.need[processId] = [(self.need[processId][j] - request[j]) for j in range(self.sourceTypeNum)]
                if self.security():
                    self.output()
                    continue
                else:
                    print("无安全序列，申请不成功！")
                    self.available = [(self.available[j] + request[j]) for j in range(self.sourceTypeNum)]
                    self.allocation[processId] = [(self.allocation[processId][j] - request[j]) for j in range(self.sourceTypeNum)]
                    self.need[processId] = [(self.need[processId][j] + request[j]) for j in range(self.sourceTypeNum)]

def main():
    os = OS()
    os.build()
    os.more()

if __name__ == "__main__":
    main()

"""
3
5
10 5 7
进程p[1]       7   5   3
进程p[2]       3   2   2
进程p[3]       9   0   2
进程p[4]       2   2   2
进程p[5]       4   3   3
进程p[1]       0   1   1
进程p[2]       2   0   0
进程p[3]       3   0   2
进程p[4]       2   1   1
进程p[5]       0   0   2
y
1
4 3 1
y
1
1 2 0
y
4
0 1 1
y
2
1 2 2
y
3
6 0 0
y
1
6 2 2
y
5
4 3 1
"""