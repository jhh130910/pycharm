
'''
提供迭代方法的容器或者方法
迭代器
从容器依次处理
'''

def iter(n):
    if n == 1 :
        return 1
    else :
        return iter(n-1)*n

iter_count = iter(9)
print (iter_count)