#!/usr/bin/env python
'''
Created on Mar 31, 2012

@author: micle
'''
import sys
import os
import string
import json
from toc.pdfinfo import Info

def main(argv):
    import getopt
    def usage():
        print ('Usage: %s [Option] [File Directory] ...\n'
               'Options:\n'
               '    -o, --output OUTFILE \n'
               '        Specify the output file. \n'
               '    -r, --reverse \n'
               '        Sort the output in DESC order, ASC order in default. \n'
               '    -t, --threshold FLOAT \n'
               '        The probability of a TOC item can be computed using p=frequency/total. \n'
               '        The TOC items with probability p < FLOAT will be ignored in output. \n'
               '        FLOAT should between 0 and 1. \n'
               '    -h, --help \n'
               '        Print usage information. \n' % argv[0])
        return 100
    
    def build_dictionary(pdf):
        info = Info(pdf)
        if info.toc:
            # articles
            a_count = len(articles)
            # process articles with title only
            if len(info.title) > 1:
                if info.title not in articles.values():
                    a_count += 1
                    articles[a_count] = info.title
                
                # dictionary items and relations
                for key in info.toc:
                    if key in dictionary.keys():
                        dictionary[key] += 1
                        relations[key].append(a_count)
                    else:
                        dictionary[key] = 1
                        relations[key] = list()
                        relations[key].append(a_count)
        info = None
        return 200
    
    # global variables
    articles = dict()
    dictionary = dict()
    relations = dict()
    
    # begin
    try:
        (opts, args) = getopt.getopt(argv[1:], 'o:t:rh', ['output=','threshold=','reverse'])
    except getopt.GetoptError:
        return usage()
    if len(args) != 1: return usage()
    # option
    outfile = None
    reverse = False
    threshold = -1
    for (k, v) in opts:
        if k in ('-o', '--output'): outfile = v
        if k in ('-t', '--threshold'): threshold = string.atof(v)
        if k in ('-r', '--reverse'): reverse = True
        elif k in ('-h', '--help'): return usage()

    # output      
    if outfile:
        if not os.path.exists(outfile):
            print 'The output directory does not exist, please create it first.'
            return 
    
    # build dictionary 
    infile = args[0] 
    if os.path.isdir(infile): 
        for dirpath, dirnames, filenames in os.walk(infile):
            for filename in filenames:
                if filename.endswith('.pdf'):
                    filepath=os.path.join(dirpath,filename)
                    #print filepath
                    #print 'hello \n'
                    build_dictionary(filepath)     
    elif os.path.isfile(infile):
        if infile.endswith('.pdf'):
            build_dictionary(infile)
    
    # json           
    if outfile:
        if os.path.isdir(outfile):
            a_file = file(os.path.join(outfile,'articles.json'), 'w')
            d_file = file(os.path.join(outfile,'dictionary.json'), 'w')
            r_file = file(os.path.join(outfile,'relations.json'), 'w')
        else:
            print 'Please indicate a output directory, not a file.'
        a_file.write('{0}\n'.format(json.dumps(articles)))
        d_file.write('{0}\n'.format(json.dumps(dictionary)))
        r_file.write('{0}\n'.format(json.dumps(relations)))
        a_file.close(),d_file.close(),r_file.close()
    else:        
        total = len(articles)  
        if reverse:
            print '\n{0}\t: Total\n'.format(total)
        for k,v in sorted(dictionary.items(), key=lambda x:x[1], reverse=reverse):
            #print (1.0*v) / total, threshold
            if (1.0*v) / total > threshold:
                print '{0}\t: {1}'.format(v,k)  
        if not reverse:            
            print '\n{0}\t: Total\n'.format(total)  
    # end
    return

if __name__ == '__main__': sys.exit(main(sys.argv))