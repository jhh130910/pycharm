
# Pool  Fish  Turtle

class Fish():
    def __init__(self,x):
        self.num = x


class Turtle():
    def __init__(self,y):
        self.num = y

class Pool():
    def __init__(self,x,y):
        self.fish = Fish(y)
        self.turtle = Turtle(x)

    def echo_num(self):
        print ('fish num is %d , turtle num is %d' % (self.fish.num , self.turtle.num ))

# 实例化（传参）
Shili_Pool = Pool(2,7)
# 调用函数
Shili_Pool.echo_num()


'''
没有继承关系的类，进行组合（横向）
有继承关系的类，进行继承（纵向）
Mix-in 编程模式

类 （类属性：静态属性）  class xxx 后面的定义
类对象 （类定义）        xxxx() 
实例对象 （实例属性可以覆盖类属性）
实例属性（如果属性名称和方法相同，会覆盖）

属性用名称
方法用动词

绑定 ： Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定概念
类可以直接调用方法（有没有实例不影响）
类实例化后，需要调用方法（该方法必须要有实例，或者说是个有效实例，就是有至少self参数等）

xxx.__dict__

BIF : build in function 

1. 判定一个类和其他类的关系
issubclass(class子类, classinfo或者object代表所有基类)

object : 所有类的基类

isinstance( 实例化对象，类）

hasattr( object , name) # 是否是对象的属性，name需要引号引起来，直接写认为是变量

getattr( object , name[, default])

setattr (object , name ,value )

delattr ( object , name )

property(fget=None , fset=None, fdel=None ，doc=None )
通过属性设置属性（定义好的属性）
应用场景：修改函数，不影响使用参数或者接口 （魔法方法的组合）

《魔法方法》： 构造 与 析构
魔法方法总是被双下划线包围，例如： __init__
魔法方法是面向对象的Python的一切，OOP编程强大
"魔力" 是总是在适当的时候被调用

问题1 ： 类定义，__init__方法什么需要定义？
__init__ 返回值为None

'''

class Rec:
    def __init__(self,parameter1,parameter2):
        self.x_attr = parameter1
        self.y_attr = parameter2

    def getZhouChang(self):
        return ( 'ZhouChang is : %d Mi'  %   ((self.x_attr + self.y_attr ) * 2) )

    def getMianJi(self):
        return ('MianJi is : %d Mi' % (self.y_attr * self.x_attr))
        # no print

obj_rect = Rec(1,5)
obj_rect.getMianJi()
obj_rect.getZhouChang()

print (obj_rect.getMianJi())
print (obj_rect.getZhouChang())

'''
__new__  方法（一般不需要重写，一般返回当前类）
__new__(cls[, ...])
继承不可变类型，修改str 字符串操作方法
__init__  and __new__ ：对象的构造器
'''

class CapStr(str):
    #def __new__(cls, *args, **kwargs)
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)

str_obj = CapStr('修改__new__方法成功！\nLove Xue')
print (str_obj)

'''
__del__(self)
python 析构器
当变量没有被调用，有对应垃圾回收机制
'''

class C:
    def __init__(self):
        print ("__init__")
    def __del__(self):
        print ("__del__")

c1 = C()
c2 = c1
del c1
del c2

'''
Python 2.2 之前： 类和类型
Python  int float ...   工厂函数
魔法方法：前后有两个下划线，如下
__add__(self,other)  +
__sub__(self,other)  -
__mul__(self,other)  * 
__truediv__(self,other) / 定义真除法行为 
__floordiv__(self,other)  // 定义整数除法的行为
__mod__(self,other) %  取模算法，余数
__divmod__(self,other) 
__pow__(self,other[,module])  ** 幂运算
__lshift__(self,other)  <<
__rshift__(self,other) >>
__and__(self,other) &
__xor__(self,other) ^
__or__(self,other) |
CPU：位（二进制） 
人：字节（8位）
'''
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)

a = New_int(2)
b = New_int(4)

print (a+b)
#  self  实例化对象绑定的方法
# most recursion 最大递归深度

class int(int):
    def __add__(self, other):
        return int.__sub__(self,other)

int_obj_a = int('6')
print (int_obj_a)
int_obj_b = int(3)
print (int_obj_b)
print (int_obj_a + int_obj_b)