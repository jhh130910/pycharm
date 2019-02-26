'''
Function : vcf.gz file uncompress and compress, Fastq likely
Test Data :  
            clinvar_20170802.vcf.gz
            
            # TODO 
            Method 1 :  pigz software multiple processsing 
            Method 2 :  python gzip package 
            Method 3 : zlib - data compression 
            
Tips : diff about compress and pack

'''

import os
import sys
import gzip
import zlib
import shutil

# P1 : demo code of gzip
# provides a simple interface to compress and decompress files just like the GNU programs gzip and gunzip would

def gzip_file_read():

    '''Open a gzip-compressed file in binary or text mode, returning a file object.'''
    # mode : binary : 'r', 'rb' [defalut], 'a', 'ab', 'w', 'wb', 'x' or 'xb'
    # mode : text : 'rt', 'at', 'wt', or 'xt'
    # compresslevel : 0..9
    gzip.open(filename, mode='rb', compresslevel=9, encoding=None

    gzip.compress(data, compresslevel=9)

    gzip.decompress(data)


def test_of_gzip():

    import gzip
    with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
        file_content = f.read()

    content = b"Lots of content here"
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
        f.write(content)

    with open('/home/joe/file.txt', 'rb') as f_in:
        with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    s_in = b"Lots of content here"
    s_out = gzip.compress(s_in)


# P2 : demo code of zlib


