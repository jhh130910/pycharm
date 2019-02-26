
# coding : utf-8

# attr + method = obj

class Obj_Name():
    '''
    封装  ： 属性、方法
    继承  ： 
    多态  ： 同一个函数，动作差异性
    '''

    color = 'green'
    age = 4
    name = 'gui'

    def run(self):
        print ('run ...')

    def eat(self):
        print ('eat ...')

temp_obj = Obj_Name()
temp_obj.run()
temp_obj.eat()

#  继承
class Ji_Cheng(list):
    pass
obj_jicheng = Ji_Cheng()
obj_jicheng.append(5)
obj_jicheng.append(1)
obj_jicheng.append(2)
obj_jicheng.sort()
print (obj_jicheng)

#  2
class Parent():
    def hi(self):
        print ("调用父类...")

class Child(Parent):
    pass

p = Parent()
p.hi()

c = Child()
c.hi()

#  多态

class Duo_Tai():
    def Attr(self,age,name):
        self.age = age
        self.name = name

    def Add(self):
        print ('%s age is : %d' % (self.name , self.age))

obj_duotai1 = Duo_Tai()
obj_duotai1.Attr(12,'niuniu')

obj_duotai2 = Duo_Tai()
obj_duotai2.Attr(20,'taotao')

obj_duotai1.Add()
obj_duotai2.Add()

