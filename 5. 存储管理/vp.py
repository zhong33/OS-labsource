#-*- encoding: utf-8 -*-
# target: 可变分区算法

class Strorge:
    def __init__(self):
        self.size = int(input("请输入内存大小为："))
        self.start = int(input("请输入起始地址大小为："))
        self.use = []
        self.free = []

    def build(self):
        self.free.append([self.size, self.start, "空闲"])
        while True:
            print("*"*20 + "可变分区管理" + "*"*20)
            print("\t*\t     1.内存分配\t\t*")
            print("\t*\t     2.内存去配\t\t*")
            print("\t*\t     0.退出    \t\t*")
            opt = int(input("\t\t     请输入选项[ ]\b\b"))
            if not opt:
                break
            elif opt == 1:
                print("*"*20 + "分配算法" + "*"*20)
                print("\t*\t     1.最先分配法\t*")
                print("\t*\t     2.最优分配法\t*")
                print("\t*\t     3.最坏分配法\t*")
                opt1 = int(input("\t\t     请输入选项[ ]\b\b"))
                self.output()
                if opt1 == 1:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    flag = 1
                    # 直接遍历free，最先分配
                    for now in self.free:
                        if int(data[1]) < now[0]:
                            work = [int(data[1]), now[1], data[0]]
                            self.use.append(work)
                            self.use.sort(key=lambda x:x[1])
                            now[0] -= int(data[1])
                            now[1] += int(data[1])
                            print("分配成功！")
                            flag = 0
                            self.free.sort(key=lambda x:x[1])
                            self.output()
                            break
                    if flag:
                        print("发生错误，分配失败！")
                elif opt1 == 2:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    flag = 1
                    # 先对free进行大小的升序排序，再进行分配，最优分配
                    self.free.sort(key=lambda x:x[0])
                    for now in self.free:
                        if int(data[1]) < now[0]:
                            work = [int(data[1]), now[1], data[0]]
                            self.use.append(work)
                            self.use.sort(key=lambda x:x[1])
                            now[0] -= int(data[1])
                            now[1] += int(data[1])
                            print("分配成功！")
                            flag = 0
                            self.free.sort(key=lambda x:x[1])
                            self.output()
                            break
                    if flag:
                        print("发生错误，分配失败！")
                elif opt1 == 3:
                    data = [_ for _ in input("请输入作业名及其所需分配的主存大小（单位：KB）：").split()]
                    flag = 1
                    # 先对free进行大小的降序排序，再进行分配，最坏分配
                    self.free.sort(key=lambda x:x[0], reverse=True)
                    for now in self.free:
                        if int(data[1]) < now[0]:
                            work = [int(data[1]), now[1], data[0]]
                            self.use.append(work)
                            self.use.sort(key=lambda x:x[1])
                            now[0] -= int(data[1])
                            now[1] += int(data[1])
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
                for now in self.use:
                    # 寻找作业名
                    if now[2] == workName:
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
                        print("回收成功！")
                        flag = 0
                        self.output()
                        break
                if flag:
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

if __name__ == "__main__":
    s = Strorge()
    s.build()

"""
256
40
1
1
JOB_A 15
1
1
JOB_B 50
1
1
JOB_C 10
1
1
JOB_D 25
1
1
JOB_E 14
2
JOB_B
2
JOB_D
1
2
JOB_X 15
1
3
JOB_G 5
1
1
JOB_F 32
2
JOB_C
2
JOB_A
2
JOB_F
2
JOB_E
2
JOB_X
2
JOB_G
0
"""
