#!/usr/bin/env python
'''
@summary: TOC's command line script.
          Build a pdf document's TOC, filtered by a TOC dictionary. 

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdftoc.py 2012-03-29 Micle Bu
'''
import string
import sys
from pdfdig.pdfinfo import TOC

def main(argv):
    import getopt
    def usage():
        print ('Usage: %s [Option] File ...\n'
               'Options:\n'
               '    -o, --output OUTFILE \n'
               '        Specify the output file. \n'
               '    -i, --minlen Num \n'
               '        Print the number of matches for each input file, instead of normal ouput. \n'
               '    -m, --maxlen Num \n'
               '        Ingnore case distinctions.\n'
               '    -f, --file-prefix \n'
               '        Prefix each line of output with input file. \n'
               '    -n, --line-number \n'
               '        Prefix each line of output with 1-based line number within its txt file. \n'
               '    -t, --threshold FLOAT \n'
               '        The probability of a TOC item can be computed using p=frequency/total. \n'
               '        The TOC items with probability p < FLOAT will be ignored in output. \n'
               '        FLOAT should between 0 and 1. \n'
               '    -p, --path PATH \n'
               '        Specify the TOC dictionary directory. \n'
               '    -d, --dictionary \n'
               '        Use TOC dictionary as filter in constructing TOC. \n'
               '    -h, --help \n'
               '        Print usage information. \n' % argv[0])
        return 100
    try:
        (opts, args) = getopt.getopt(argv[1:], 'o:i:m:fnt:p:dh', 
                                     ['output=','minlen=','maxlen=','file-prefix',
                                      'line-number','threshold=','path=','dictionary=','help'])
    except getopt.GetoptError:
        return usage()
    if not args: return usage()
    
    # options
    outfile = None
    minlen = 4
    maxlen = 25
    pfile = False
    pnumber = False
    threshold = 0.05
    path = '../docs/json'
    dictionary = False
    #
    for (k, v) in opts:
        if k in ('-o', '--output'): outfile = v
        elif k in ('-i', '--minlen'): minlen = string.atoi(v)
        elif k in ('-m', '--maxlen'): maxlen = string.atoi(v)
        elif k in ('-f', '--file-prefix'): pfile = True
        elif k in ('-n', '--line-number'): pnumber = True
        elif k in ('-t', '--threshold'): threshold = string.atof(v)
        elif k in ('-p', '--path'): path = v
        elif k in ('-d', '--dictionary'): dictionary = True
        elif k in ('-h', '--help'): return usage()
    #    
    if outfile:
        f = file(outfile, 'w')
    else:
        f = sys.stdout
    
    # extract toc        
    for pdffile in args:
        # pdftoc
        toc = TOC(pdffile, minlen=minlen, maxlen=maxlen,
                  threshold=threshold,path=path)
        
        if dictionary:
            toc_toc = toc.buildtoc_dict()
        else:
            toc_toc = toc.buildtoc()

        # output        
        f.write('\n{0}\n{1}'.format(pdffile, ''.join(toc.formats(toc_toc, pfile, pnumber))))
    f.close()
    
    return

if __name__ == '__main__': sys.exit(main(sys.argv))