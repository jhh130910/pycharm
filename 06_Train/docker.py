
'''
鸭子思想 DuckTyping  自觉，经验
协议 ： Protocols ，一种指南
容器

list
turple
dict
容器类型的协议：
容器不可变： __len__()  __getitem__()

容器可变：
__len__() __getitem__()
__setitem__()  __delitem__()
'''

# 一个不可改变list，记录元素被访问的次数

class Count_term:
    def __init__(self,*args):
        self.values = [ i for i in args]
        self.count = {}.fromkeys(  range(len(self.values)),0 )

    def __len__(self, other):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

c1 = Count_term(1,2,3,4,5)
c1[1]
c1[2]
c1[2]
print (c1.count)