#coding=utf-8
'''
Created on Mar 31, 2012

@author: micle
'''
from pdfminer.pdfparser import PDFParser, PDFDocument
import normalizer
import json
import sys
import re
reload(sys)  
sys.setdefaultencoding('utf-8')

pdf='../example/demo/1297-9716-42-107.pdf'

fp = open(pdf, 'rb')
parser = PDFParser(fp)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')

# level 1 of toc
toc = list()

try:
    outlines = doc.get_outlines()
    
    count = 0
    first = ''
    print count
    for (level,title,dest,a,se) in doc.get_outlines():
        if count == 0:
            first=title
        count += 1
    
    print count,first
    
    for (level,title,dest,a,se) in doc.get_outlines():
        #print '{0}\t{1}'.format(level, title)
        if level==1:
            print '{0}\t{1}'.format(level, title)
            toc.append(title)
            
    print ''.join(toc)
    print json.dumps(toc)
except:
    print 'error'
