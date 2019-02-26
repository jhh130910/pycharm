
name = 'string'

for i in name :
    print (i,end='\n')

def Function_Name(arg1='arg1', arg2='arg2') :
    print (arg1 + '->' + arg2 )

Function_Name('a','ab')
Function_Name()
def Funtion_two(*params):
    print ('length is ',len(params))
    print ('second parameters :' , params[1])

Funtion_two(1,'name',2,3,4,'pk')

age = 28
def Function_Global():
    global age
    age = 7
    print ("just _name ")

Function_Global()
print (age)

'''
function 
'''
def func1():
    print ('func1 run ...')
    def func2():
        print('func2 run ...')
    func2()

func1()

'''
编程范式（面向过程，面向对象，代码重用性可用性）
闭包
容器类型  或者  堆栈
nonlocal
lambda

'''

lambda_num = lambda x,y : x + y
#lambda_num()
print (lambda_num(1,2))

'''
filter  过滤false 或者null

map 
'''