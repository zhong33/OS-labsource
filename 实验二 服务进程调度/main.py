#-*- encoding: utf-8 -*-

from modules import *

def main():
    while True:
        print("*"*20 + "欢迎来到服务进程调度实验" + "*"*20)
        print("\t*\t     1.先来先服务\t\t*")
        print("\t*\t     2.优先级调度\t\t*")
        print("\t*\t     3.时间片轮转调度\t\t*")
        print("\t*\t     0.退出    \t\t\t*")
        opt = int(input("\t\t     请输入选项[ ]\b\b"))
        if not opt:
            break
        elif opt == 1:
            print("\n模拟先来先服务算法\n")
            fcfs.main()
        elif opt == 2:
            print("\n模拟优先级调度算法\n")
            ps.main()
        elif opt == 3:
            print("\n模拟时间片轮转调度算法\n")
            rr.main()

if __name__ == "__main__":
    main()