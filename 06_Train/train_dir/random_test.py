import random as xx

print( xx.random() )
print( xx.randint(2,40) )

import random_test

# 如果文件名称和模块名称一致，程序理解为导入自定义模块（个人理解）
with open("foo.txt") as file:
    data = file.read()


class Sample:
    def __enter__(self):
        print ("In __enter__()")
        return "test"

    def __exit__(self, type, value, trace):
        print ("In __exit__()")


def get_sample():
    return Sample()


with get_sample() as sample:
    print ("sample:", sample)


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print ("type:", type)
        print ("value:", value)
        print ("trace:", trace)

    def do_something(self):
        bar = 1 / 1
        return bar + 10

with Sample() as sample:
    sample.do_something()

# Python的with语句是提供一个有效的机制，让代码更简练，同时在异常产生时，清理工作更简单。