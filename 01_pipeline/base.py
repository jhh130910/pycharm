'''
    test script 
'''

# --*-- coding : utf-8 --*--

import re

def regexp():
    '''
    # alt + enter check regex pattern
    '''
    pattern_one = re.compile('[0-9]+')
    string = 'AGCTN0009999'
    result_pattern = pattern_one.findall(string)
    print ( result_pattern )

if __name__ == '__main__':
    print ( 'Start ...')
    regexp()
