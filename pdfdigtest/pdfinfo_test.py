'''
Created on Mar 29, 2012

@author: micle
'''
from pdfdig.pdfinfo import TOC
import json
import re
import os

#pdf = '../example/coordinate.pdf'
pdf = '../example/coordinate.pdf'
pattern = 'brain '

toc = TOC(pdf)
print toc.toc
print ''.join(toc.results)

json_dir = '../docs/json'
json_file_dictionary = os.path.join(json_dir, 'dictionary.json')
json_file_articles = os.path.join(json_dir, 'articles.json')

a_file = open(json_file_articles)
d_file = open(json_file_dictionary)
json_string_articles = a_file.read()
json_string_dictionary = d_file.read()
articles = json.loads(json_string_articles)
dictionary = json.loads(json_string_dictionary)

total = len(articles)
print '{0}\t: Total\t'.format(total)

for k,v in sorted(dictionary.items(), key=lambda x:x[1], reverse=True):
    if (1.0*v)/total > 0.1:
        print '{0}\t: {1}'.format(v,k) 
