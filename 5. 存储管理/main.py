#-*- encoding: utf-8 -*-

from modules import *

def main():
    while True:
        print("*"*20 + "欢迎来到存储管理实验" + "*"*20)
        print("\t*\t     1.固定分区算法\t\t*")
        print("\t*\t     2.可变分区算法\t\t*")
        print("\t*\t     3.页面置换算法\t\t*")
        print("\t*\t     4.分页/分段算法\t\t*")
        print("\t*\t     5.磁盘移臂调度算法\t\t*")
        print("\t*\t     0.退出    \t\t\t*")
        opt = int(input("\t\t     请输入选项[ ]\b\b"))
        if not opt:
            break
        elif opt == 1:
            print("\n模拟固定分区算法\n")
            fpsm.main()
        elif opt == 2:
            print("\n模拟可变分区算法\n")
            vp.main()
        elif opt == 3:
            print("\n模拟页面置换算法\n")
            pr.main()
        elif opt == 4:
            print("\n模拟分页/分段算法\n")
            psss.main()
        elif opt == 5:
            print("\n模拟磁盘移臂调度算法\n")
            ass.main()

if __name__ == "__main__":
    main()