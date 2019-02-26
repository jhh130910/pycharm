'''

功能描述：fileinput模块提供处理一个或多个文本文件的功能，可以通过使用for循环来读取一个或多个文本文件的所有行。
模块特征：工作方式和readlines很类似，不同点在于它不是将全部的行读到列表中而是创建了一个xreadlines对象。

input()       #返回能够用于for循环遍历的对象
filename()    #返回当前文件的名称
lineno()      #返回当前已经读取的行的数量（或者序号）
filelineno()  #返回当前读取的行的行号
isfirstline() #检查当前行是否是文件的第一行

'''

import re
import time
import os
import sys
import random

import fileinput

switch = random.randint(1,20)

def get_current_dir(switch):

    ''' get current_dir name '''
    print ( "now num is :{}".format(switch))
    if  switch > 10:
        print ( os.getcwd())
        print ( os.path.split( os.getcwd() ))
    else:
        sys.exit(0)

# read file
class Fileinput_Class():

    ''' xxx '''
    def __init__(self,input_file_name,line_num_max=100):
        self.input_file_name = input_file_name
        self.line_num_max = line_num_max

    def fileinput_read(self):

        ''' xxx'''
        for each_line in fileinput.input( self.input_file_name, backup='.bk', inplace=1):
            print ( each_line.strip().replace('AA','##'))
        fileinput.close()

    def fileinput_message_glob(self, exit_condition = 4 ):

        ''' xxx'''
        for line in fileinput.input( self.input_file_name ):

            if exit_condition > fileinput.lineno():
                print ( fileinput.filename() )
                print ( fileinput.lineno() )
                print ( fileinput.filelineno() )
            else :
                break

    def just_read_file_isfistline(self):

        ''' xxx'''
        for line_isfirt in fileinput.input( self.input_file_name ):
            if fileinput.isfirstline():
                print ( line_isfirt )


# executable main
if __name__ == '__main__':

    # step 1
    get_current_dir(switch)

    # step 2
    Fileinput_Class_Obj = Fileinput_Class('readme.txt')
    Fileinput_Class_Obj.fileinput_read()
    Fileinput_Class_Obj.fileinput_message_glob()

    time.sleep(1.5)
    if os.path.exists('readme.txt.bk'):
        os.remove('readme.txt.bk')
