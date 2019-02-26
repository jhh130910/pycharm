# coding : utf-8

'''
1. 功能版本version1 ，判断数据是否是猜中的。
2. 产生随机数，去猜测，这样猜对结果具有随机性，概率多大。
3. 版本变种，比如对非数字，字符串等的猜测，并添加多个结果合并，对一定比例的正确情况下的反馈。

'''

import os
import sys
import re
import random

# 0-1.0
little_num = random.random()
# (a,b)  a-b
random_num = int(random.uniform(2,10))
#print (random_num)
#print (little_num)

while True :

    tmp = input("input a num: \n")

    num = int(tmp)

    if num == random_num :
        print ("right\n")
        break
    else :
        if num > random_num :
            print ("num is big\n")
        else :
            print ("num is small\n")

#Class Name_Random():
#    pass

def __init__():
    pass

def _function_attribute_1():
    pass

def __function_attribute_2():
    pass

def function_attribute_3():
    pass

str_normal = "Guess result Good!"
str_special = r'C:///*^%%@&*#&#'

print (str_normal)
print (str_special)