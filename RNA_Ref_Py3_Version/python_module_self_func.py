
'''
_func() 
from module import *  will not import _xxx  unless  use : __all__ = [ 'function_name' , 'module_name' ] 

Python 私有属性和方法没有类似别的语言的public,private等关键词来修饰

'''
def cube(x):
    """
    >>> cube(10)
    1000
    """
    return x * x
def _test():
    pass

def add():
    pass

if __name__ == "__main__":
    _test()



