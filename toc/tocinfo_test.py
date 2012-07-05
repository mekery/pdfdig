'''
Created on Mar 31, 2012

@author: micle
'''
from toc.pdfinfo import Info
import json
import sys

#pdf = '../example/toc/1471-2105-12-S13-S20.pdf'
pdf = './coordinate.pdf'

info = Info(pdf)

articles = dict()
items = dict()
relations = dict()

# Dictionary
d_count = len(articles)
if info.title not in articles.values():
    d_count += 1
    articles[d_count] = info.title
    
for k,v in articles.items():
    print '{0}\t{1}'.format(k, v)

d_json = json.dumps(articles)
print d_json

# Items
i_count = len(items)
for key in info.toc:
    if key in items.keys():
        items[key] += 1
        relations[key].append(d_count)
    else:
        items[key] = 1
        relations[key] = list()
        relations[key].append(d_count)

for k,v in items.items():
    print '{0}\t{1}'.format(k, v)
    
for k,v in relations.items():
    print '{0}\t{1}'.format(k, v)

i_json = json.dumps(items)
r_json = json.dumps(relations)

print i_json
print r_json

d_file = file('dictionary.json', 'w')
i_file = file('items.json', 'w')
r_file = file('relations.json', 'w')


d_file.write('{0}\n'.format(d_json))
i_file.write('{0}\n'.format(i_json))
r_file.write('{0}\n'.format(r_json))
