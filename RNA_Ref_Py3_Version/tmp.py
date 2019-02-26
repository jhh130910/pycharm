import tempfile
import argparse, sys, os
import math
import time
import re
from argparse import RawTextHelpFormatter
from subprocess import Popen, PIPE, STDOUT
import os
import docx
import doctest

class XXX_XXX():
    __slots__ =  ('x','y')

def run_id_match():

    pattern_of_runid =  re.compile(r'(?:\d{2})?\d{6}\_(?:ST-)?\w\d{5}\_\d{4}\_(?:A|B)\S{9}')
    bcl = '20180926_E00591_0259_AHT3GGCCXY'
    out = pattern_of_runid.findall(bcl)
    print ( out )

if __name__ == '__main__':
    run_id_match()
