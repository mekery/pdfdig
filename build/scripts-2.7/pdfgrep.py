#!/usr/bin/python
'''
@summary: Match's command line script.
          Search in pdf based on converted text from it, works like grep.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdfgrep.py 2012-04-18 Micle Bu
'''
import sys
import os
import platform
import string
from pdfdig.pdfmatch import Match

def main(argv):
    import getopt
    def usage():
        print ('Usage: %s [Option] Pattern File ...\n'
               'Options:\n'
               '    -o, --output OUTFILE \n'
               '        Specify the output file. \n'
               '    -c, --count \n'
               '        Print the number of matches for each input file, instead of normal ouput. \n'
               '    -i, --ignore-case \n'
               '        Ingnore case distinctions.\n'
               '    -f, --file-prefix \n'
               '        Prefix each line of output with input file. \n'
               '    -p, --page-number \n'
               '        Prefix each line of output with page number. \n'
               '    -n, --line-number \n'
               '        Prefix each line of output with 1-based line number within its txt file. \n'
               '    -t, --context NUM \n'
               '        Print at most NUM characters of context around each match.\n'
               '    -d, --dictionary PATH \n'
               '        Specify the TOC dictionary directory. \n'
               '    -l, --location \n'
               '        Print the match location within TOC.\n'
               '    -C, --color COLOR\n'
               '        Highlight color.\n '
               '        COLOR is red by default, also can be black,red,green,orange,blue,purple,bluegreen or white.\n'
               '    -h, --help \n'
               '        Print usage information. \n' % argv[0])
        return 100
    
    def distribution(matches):
        dist = dict()
        for match in matches:
            # [[(pageno, lineno, location, context),...],...]
            for s in match.matches:
                for t in s:
                    key = t[2]
                    if key in dist.keys():
                        dist[key] += 1
                    else:
                        dist[key] = 1
        return dist
    
    # main
    try:
        (opts, args) = getopt.getopt(argv[1:], 'o:cinfpt:d:lC:h', 
                                     ['output=','count', 'ignore-case','file-prefix','page-number', 
                                      'line-number','context=','dictionary=','location','color=','help'])
    except getopt.GetoptError:
        return usage()
    if len(args) < 2: return usage()
    
    # options
    outfile = None
    context = 0
    dictionary = None
    count = False
    icase = False
    pfile = False
    ppage = False
    pnumber = False
    location = False
    color = 'red'
    #
    for (k, v) in opts:
        if k in ('-o', '--output'): outfile = v
        elif k in ('-c', '--count'): count = True
        elif k in ('-i', '--ignore-case'): icase = True
        elif k in ('-f', '--file-prefix'): pfile = True
        elif k in ('-p', '--page-number'): ppage = True
        elif k in ('-n', '--line-number'): pnumber = True
        elif k in ('-t', '--context'): context = string.atoi(v)
        elif k in ('-l', '--location'): location = True
        elif k in ('-d', '--dictionary'): dictionary = v
        elif k in ('-C', '--color'): color = v
        elif k in ('-h', '--help'): return usage()
    #    
    if outfile:
        f = file(outfile, 'w')
    else:
        f = sys.stdout
    
    # match pattern
    pattern = args[0]
    infiles = args[1:]  
    matches = []    
    for infile in infiles:
        # directory
        if os.path.isdir(infile):                
            for dirpath, dirnames, filenames in os.walk(infile):
                for filename in filenames:
                    if filename.endswith('.pdf'):
                        pdffile = os.path.join(dirpath,filename)
                        print 'Matching in {0}'.format(pdffile)
                        match = Match(pattern, pdffile, icase=icase, location=location, 
                                      context=context, dictionary=dictionary)
                        matches.append(match)
        # file
        elif os.path.isfile(infile):
            if infile.endswith('.pdf'):
                pdffile = infile
                match = Match(pattern, pdffile, icase=icase, location=location, 
                              context=context, dictionary=dictionary)
                matches.append(match)
        else:
            continue
    
    # output
    if count:
        dist = distribution(matches)   
        for key in dist.keys():
            f.write('@L: {0}\t@C: {1}\n'.format(key,str(dist[key])))
    else:
        for match in matches:
            if outfile:
                # no highlight
                results = match.formats(pfile, ppage, pnumber)
            else:
                # no highlight on Windows
                # Todo: Mac                
                if  platform.system() == 'Windows':
                    results = match.formats(pfile, ppage, pnumber)
                else:
                    results = match.formats(pfile, ppage, pnumber, highlight=True, color=color)
            if (len(results) > 0):
                f.write('{0}\n'.format(''.join(results))) 
             
    f.close()
    if outfile:
        print '\nThe results have been saved in {0}.\n'.format(outfile)
    
    return

if __name__ == '__main__': sys.exit(main(sys.argv))