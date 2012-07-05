'''
Created on Mar 29, 2012

@author: micle
'''
from pdfdig.pdfmatch import Match
import re

line = 'This is a 2 test for brain, just a 3 brain. The end.'

pattern = re.compile(r'brain')

h = ''
start = 0
end = len(line)
for match in pattern.finditer(line):
    s = match.start()
    e = match.end()
    
    replace = '\x1b[0;36m' + line[s:e] + '\x1b[0m'
    
    h += line[start:s]
    h += replace
    start = e
    #print s
h += line[start:end]


print h


