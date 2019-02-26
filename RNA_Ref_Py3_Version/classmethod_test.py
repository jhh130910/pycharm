
import unittest

''' classmethod test '''


class NameClass(object):
    normal = 'xxx'

    @classmethod
    def count(cls, messg):
        print("{} .. {}".format(messg, cls.x_type))

class A(NameClass):
    x_type = 'A'

class B(NameClass):
    x_type = 'B'

a = A()
a.count('1...')
A.count("2...")

