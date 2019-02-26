import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print ('my position is :',self.x , self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):

    #  子类重写了父类的方法
    def __init__(self):

        # Fish.__init__(shark)  调用未绑定的父类方法，self此处是子类的实例对象
        Fish.__init__(self)  # super().__init__() 继承多个祖先（不需要给基类名称）
        self.hungry = True

    def eat(self):
        if self.hungry:
            print ("eat ...")
            self.hungry = False

        else :
            print ("enough ...")
# 类实例化
fish = Fish()

fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
shark.eat()
shark.move()

#  多重继承
class DerivedClassName(Base1,Base2,Base3...):
    #...

#