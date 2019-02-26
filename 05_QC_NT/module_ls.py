__author__ = 'jinhh'

'''
FUNCTION :  

USAGE :

'''

import requests
#from BeautifulSoup4 import bs4
import lxml
import time
import operator
import re
import os
import sys
import threading

def fastq_to_fasta(input_fastq):
    pass

def input_data_convert_to_fasta(input_data,data_format):
    '''
    Judge input file foramt (fastq , fasta , bam ...) covert them to fasta format  
    '''
    if data_format == 'fastq':
        return fastq_to_fasta(input_data)
    elif data_format == 'fq':
        return fastq_to_fasta(input_data)
    elif data_format == 'fq.gz':
        return fastq_to_fasta(input_data)
    elif data_format == 'other':
        pass

def read_fasta_sequence(fasta_file):
    '''
    Given the name of FASTA file , read and process it .
    '''
    with open(fasta_file) as fasta_file_obj:
        fasta_file_obj_line = fasta_file_obj.readline()
        #  process ...

    return ''

def iter_test():
    collection = 'string'
    for item in collection:
        print (item)


if __name__ == '__main__':
    print (__name__,"run self")
else:
    print (__name__,'been imported')