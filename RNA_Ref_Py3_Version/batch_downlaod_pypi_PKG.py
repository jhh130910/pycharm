'''
batch download PyPI Packages
'''

pypi_download_site = 'https://files.pythonhosted.org/packages'

def second(num):
    ''' cite func start '''
    start(num)

def start(func):
    def wrapper_add():
        func()
        stats = True
        func()
        if stats:
            print ( ' OK ... ')
        else:
            print ( ' start decorator error ')
    return wrapper_add

''' 装饰器对象add_func参数问题'''
@start
def add_func():
    num = 2
    print ( 'give {} ...'.format(num))

if  __name__ == '__main__':
    #staticmethod
    #start(2)
    #second(4)
    add_func()
