
''' P47
描述符就是将某个特殊类型的类的实例指派给另一个类的属性

特殊类型的：
__get__（self,instance,owner)
访问属性，返回属性的值

__set__(self,instance,value)
将在属性分配操作中调用，不返回任务内容

__delete__(self,instance)
控制删除操作，不返回任何内容

'''

class MyDecriptor:
    def __get__(self, instance, owner):
        print ("getting ...",self,instance,owner)

    def __set__(self, instance, value):
        print ("setting ...",self,instance,value)

    def __delete__(self, instance):
        print ("deleting ..." , self,instance)

class Test:
    x = MyDecriptor()

test = Test()
test.x
print (test.x)
print (Test)
