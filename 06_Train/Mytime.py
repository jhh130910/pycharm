# coding : utf-8

'''
__author__ = 'jinhuihui' 
function :  time count and summary 
class : MyTime 
xxx : Not start timing ...
xxx.start() : Start timing ...
xxx.stop() : Timing over!
xxx1 + xxx2 : Total run time is : N second!
'''

#import time
#from time import localtime

'''
时间获取与转换
time.localtime 返回 struct_time时间格式
from time import localtime 
'''

# __str__  , __repr__
import time as t

# 时间元组
class MyTimer():
    def __init__(self):
        self.unit = ['year','month','day','hour','minute','second']
        self.prompt = "not start timing ... "
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__
    def __add__(self, other):
        prompt = "total run :"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index] )
            if result[index]:
                prompt += (  str(result[index]) + self.unit[index] )
        return prompt

    # Start timing
    def start(self):
        self.start = t.localtime()
        print ("start timing ...")

    # stop timing
    def stop(self):
        self.stop = t.localtime()
        self._calc()
        print ("stop timing ...")

    # internal -funciton
    def _calc(self):
        self.lasted = []
        self.prompt = " total run : "
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            self.prompt += str(self.lasted[index])
        print (self.prompt)

t1 = MyTimer()
t1.start()
t1.stop()