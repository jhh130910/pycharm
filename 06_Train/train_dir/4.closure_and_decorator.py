
# closure
list_test = [1,2,3,4,9]
def func_closure(list_obj):
    a = 1
    print ('func_closure ...')

    def func_inter():
        list_obj[2] += 1
        b = 2
        print (list_obj )
    return func_inter

func = func_closure(list_test)

func()
func()

# decorator
#  不影响原有函数的功能，还可以添加新的功能

def func1(func):
    def func2(x,y):
        x += 1
        y += 2
        return func(x,y)
    return func2

@func1
def mysum(a,b):
    print ( a+b )
mysum(1,4)
# 装饰器，是对函数的调用，添加新功能； 首先func1接受一个func参数（函数），然后闭包函数func2接受参数并返回被装饰
#  函数； 最内存函数传入参数 ；
#  https://www.bilibili.com/video/av18586448/?from=search&seid=838161685846804935
