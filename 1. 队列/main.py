#-*- encoding: utf-8 -*-
# target: 队列的新建、插入，修改，删除，检索，排序

class Queue:
    def __init__(self):
        self.queue = []
    
    # 插入数据，建立队列
    def buildQue(self):
        data = [int(_) for _ in input("请输出您想插入的数据：").split()]
        for i in data:
            self.queue.append(i)
    
    # 输出数据
    def output(self):
        res = ""
        for i in self.queue:
            res += str(i) + " "
        print("当前队列为：" + res)

    # 插入数据
    def insert(self):
        x = int(input("请输入您想插入的数据："))
        self.queue.append(x)

    # 删除队首元素
    def dele(self):
        print("删除队首元素：" + str(self.queue[0]))
        del(self.queue[0])

    # 排序
    def sort(self):
        print("队列排序完成")
        self.queue.sort()

    # 修改队列元素
    def change(self):
        i = int(input("请输入您想修改元素的位置："))
        x = int(input("请输入修改后的数据："))
        self.queue[i - 1] = x

    
def main():
    q = Queue()
    q.buildQue()
    q.output()
    q.insert()
    q.output()
    q.change()
    q.output()
    q.dele()
    q.output()
    q.sort()
    q.output()

if __name__ == "__main__":
    main()