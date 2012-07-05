#!/usr/bin/python
'''
@summary: Text's command line script.
          Convert pdf to text based on pdftotext.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdftotext.py 2012-03-29 Micle Bu
'''
import sys
import string
from pdfdig.pdftext import Text

def main(argv):
    import getopt
    def usage():
        print ('Usage: %s [Option] File ...\n'
               'Options:\n'
               '    -o, --output OUTFILE \n'
               '        Specify the output file. \n'
               '    -y, --layout [layout|raw] \n'
               '        Maintain the layout of the text. \n'
               '        "layout" preserve the original physical layout of the text. \n'
               '        "raw" keep the text in content stream order. This is the default setting. \n'
               '    -f, --first-page INT \n'
               '        First page to convert. \n'
               '    -l, --last-page INT \n'
               '        Last page to convert. \n'
               '    -p, --page INT \n'
               '        Specify a page to convert. \n'
               '    -h, --help \n'
               '        Print usage information. \n' % argv[0])
        return 100
    try:
        (opts, args) = getopt.getopt(argv[1:], 'o:y:f:l:p:h', 
                                     ['output=','layout=','first-page=','last-page=','pageno=','help'])
    except getopt.GetoptError:
        return usage()
    if not args: return usage()
    # option
    outfile = None
    layout = 'raw'
    first = 1
    last = 100000
    pageno = None
    for (k, v) in opts:
        if k in ('-o', '--output'): outfile = v
        elif k in ('-y', '--layout'): layout = v
        elif k in ('-f', '--first-page'): first = string.atoi(v)
        elif k in ('-l', '--last-page'): last = string.atoi(v)
        elif k in ('-p', '--pageno'): pageno = string.atoi(v)
        elif k in ('-h', '--help'): return usage()
    # output   
    if outfile:
        f = file(outfile, 'w')
    else:
        f = sys.stdout
    # pdftotext        
    for pdffile in args:
        # pdftext
        pc = Text(pdffile, layout=layout)
        pages = pc.content
        if pageno:
            if pageno <= pc.pagecount:
                f.write('{0}\n'.format(pages[pageno-1]))
            else:
                print "Invalide page number!"
        else:
            f.write('{0}\n'.format(''.join(pages[first-1:last])))
    f.close()
    return

if __name__ == '__main__': sys.exit(main(sys.argv))