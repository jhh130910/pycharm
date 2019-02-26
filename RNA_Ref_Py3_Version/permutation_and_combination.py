# --*-- encoding:utf-8 --*--
'''
    permutation and combination  method test 
    
    combinations：不考虑顺序的排列组合
    permutations：考虑顺序的排列组合
'''

import itertools
import random
member_name = ['王明雅','谢静','张晓刚','徐昊','范磊','金会会','申琳揆']

result = itertools.combinations_with_replacement(member_name,2)

print ( list(result)  )
print ( type(result))
print ( type(list(result)) )

tmp = []
for name in itertools.combinations_with_replacement(member_name,2):
    #print ( name )
    tmp.append( name )
for xx in tmp:
    print ( xx )
print ( random.randint(1,10) )
