'''
Python中没有像C++中public和private这些关键字来区别公有属性和私有属性

'''
class Test(object):
    #普通方法
    def test(self):
        print("普通方法test")
    #普通方法
    def _test1(self):
        print("普通方法_test1方法")
    #私有方法
    def __test2(self):
        print("私有方法__test2方法")
        t.__test2()  #
        self.__test2()

t = Test()
t.test()
t._test1()
# 调用私有方法报错
#t.__test2()
