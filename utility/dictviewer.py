#!/usr/bin/env python
'''
@summary: TOCDictionary's command line script.
          Print provided TOC dictionary in readable way. 

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: dicviewer.py 2012-04-01 Micle Bu
'''
import json
import sys
import os
import string

def main(argv):
    import getopt
    def usage():
        print ('Usage: %s [Option]\n'
               'Options:\n'
               '    -t, --threshold FLOAT \n'
               '        The probability of a TOC item can be computed using p=frequency/total. \n'
               '        The TOC items with probability p < FLOAT will be ignored in output. \n'
               '        FLOAT should between 0 and 1. \n'
               '    -p, --path PATH \n'
               '        Specify the TOC dictionary directory. \n'
               '    -h, --help \n'
               '        Print usage information. \n' % argv[0])
        return 100
    try:
        (opts, args) = getopt.getopt(argv[1:], 't:p:h', 
                                 ['threshold=','path=','help'])
    except getopt.GetoptError:
        return usage()
    #if not args: return usage()
    
    # options
    threshold = 0.05
    path = '../docs/json'
    #
    for (k, v) in opts:
        if k in ('-t', '--threshold'): threshold = string.atof(v)
        elif k in ('-p', '--path'): path = v
        elif k in ('-h', '--help'): return usage()
        
    # dictionary
    json_file_dictionary = os.path.join(path, 'dictionary.json')
    json_file_articles = os.path.join(path, 'articles.json')
    
    a_file = open(json_file_articles)
    d_file = open(json_file_dictionary)
    json_string_articles = a_file.read()
    json_string_dictionary = d_file.read()
    articles = json.loads(json_string_articles)
    dictionary = json.loads(json_string_dictionary)
    
    total = len(articles)
    print '{0}\t: Total\t'.format(total)
    
    for k,v in sorted(dictionary.items(), key=lambda x:x[1], reverse=True):
        if (1.0*v)/total > threshold:
            print '{0}\t: {1}'.format(v,k) 
    a_file.close()
    d_file.close()
    # end
    return

if __name__ == '__main__': sys.exit(main(sys.argv))