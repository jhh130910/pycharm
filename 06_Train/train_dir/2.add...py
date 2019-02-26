# math 模块 ; help("math")
# help(math) 与 help("math")  的区别，help(math) 需要模块导入环境

import math

# python 科学计算器 ，运算符
def add_subtract_multiply_divide(p1,p2,p3,p4,p5):
    return (p1*p2 + p3 - p4/p5)

add_subtract_multiply_divide_TEMP = add_subtract_multiply_divide(12,34,78,132,6)
#print (add_subtract_multiply_divide_TEMP)

def IsPrime(n):
    if n <= 1:
       return ('Not prime ...')
    for i in range( 2,(int(math.sqrt(n))+1)) :
        if n % i == 0:
            # BUG : pass result change 
            return('...')
    else :
        return ('Yes prime ...')
#print (IsPrime(4))
#print (IsPrime(5))
#print (IsPrime(9))

def NumIsPrime(max=100):
    for j in range(2,max):
        judge_out = IsPrime(j)
        print ('%d %s' % (j,judge_out))

NumIsPrime(14)
NumIsPrime(16)
