
class C:
    def __init__(self,size):
       # self.x = 'man'
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self):
        self.size = value

    def delSize(self):
        del self.size

    def __getattr__(self, item):
        pass

    x = property(getSize,setSize,delSize)

c = C(4)
#print (c.x)

'''
__getattr__(self,name)
定义当用户试图获取一个不存在的属性时的行为

__getattribute__(self,name)
定义当该类的属性被访问时的行为

__setattr__(self,name,value)
定义当一个属性被设置时的行为

__delattr__(self,name)
定义当一个属性被删除时的行为

'''
#  死循环陷阱及解决方案

class Rect:
    def __init__(self,width=0,height=0):
        self.width = width
        self.heigth = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.heigth = value
        else :
            #super().__setattr__(key , value)
            self.__dict__[key] = value
    def getArea(self):
        return self.width * self.heigth

obj_Rect = Rect(2,5)
obj_Rect.getArea()
print ( obj_Rect.getArea())

