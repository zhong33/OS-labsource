class Storage:
    def __init__(self):
        self.num = None
        self.blocks = []
        self.worknum = None
        self.worksize = []
        

    def build(self):
        self.num = int(input("请输入系统的分区块数："))
        print("请依次输入：\n分区号\t大小\t起始")
        for i in range(self.num):
            self.blocks.append([int(_) for _ in input().split()] + [0])
        self.output()
        self.worknum = int(input("请输入作业的个数："))
        print("请输入这{}个作业的信息：".format(self.worknum))
        for i in range(self.worknum):
            self.worksize.append(int(input("请输入作业{}的大小：".format(i+1))))
            for j in self.blocks:
                if j[1] >= self.worksize[i] and j[3] == 0:
                    j[3] = "JOB" + str(i+1)
                    break
        print("打印各作业信息：\n作业名\t\t作业大小")
        for i in range(self.worknum):
            print("JOB{}\t\t{}KB".format(i+1, self.worksize[i]))

    def output(self):
        print("\n" + "*"*20 + "打印区块信息" + "*"*20)
        print("分区号\t大小(KB)\t起始(KB)\t状态")
        for now in self.blocks:
            print("{}\t{}\t\t{}\t\t{}".format(now[0],now[1],now[2],now[3]))

    def more(self):
        while True:
            self.output()
            judge = input("是否还需要回收？（y/n）")
            if judge == "Y" or judge == "y":
                self.output()
                flag = 1
                jobname = input("请输入回收的作业名：")
                for now in self.blocks:
                    if now[3] == jobname:
                        now[3] = flag = 0
                        print("回收成功！")
                        break
                if flag:
                    print("发生错误，回收失败！")
                self.output()
            else:
                exit()

if __name__ == "__main__":
    s = Storage()
    s.build()
    s.more()

"""
5
1       12      20
2       32      32
3       64      64
4       128     128
5       100     256
3
30
60
90
"""