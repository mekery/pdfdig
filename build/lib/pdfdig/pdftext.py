'''
@summary: Text class file, convert pdf to text.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@change: 1. create. 2012-03-28 Micle Bu
         2. support page number. 2012-04-18 Micle Bu
@version: pdftext.py 2012-04-18 Micle Bu
'''
import os
import sys
import platform
import normalizer

__all__ = ['Text']

class Text(list):
    """
    Convert PDF to text using 'pdftotext'.
    Normalize the text content, such as line-break, hyphen, whitespace, etc.
    Splite the text content into lines, and store them as a list.
    """
    def __init__(self, pdf, layout='raw'):
        
        if not self.check():
            print >>sys.stderr, 'pdftotext command not found'
            return
        
        self.pagecount = 0
        # raw pages
        self.pages = self.getpages(pdf, layout)
        # normalized pages
        self.content = self.normalize()
    
    def check(self):
        """
        Check if pdftotext available on running platform.
        """
        # Todo: Mac
        pathstring = os.environ.get('PATH')
        platform_prefix = platform.system()[0]
        if  platform_prefix in 'L,C,M':
            # L:Linux, C:Cygwin, M:Mac OS X
            paths = pathstring.split(':')
            for path in paths:
                pdftotext = os.path.join(path, 'pdftotext')
                if os.path.isfile(pdftotext):
                    # found
                    return True
        elif platform_prefix in 'W':
            # W:Windows
            paths = pathstring.split(';')
            for path in paths:
                pdftotext = os.path.join(path, 'pdftotext.exe')
                if os.path.isfile(pdftotext):
                    # found
                    return True
        return False
    
    def getpages(self, pdf, layout):
        """
        Get the raw page content of pdf document.
        """
        pages = []

        while True:
            command = 'pdftotext -{0} -f {1} -l {1} {2} -'.format(layout, self.pagecount+1, pdf)
            #page_content = os.popen(command).readlines()
            page_content = os.popen(command).read()
            
            # last+1 page
            #print self.pagecount
            if len(page_content) == 0:
                break
                     
            self.pagecount += 1       
            #pages.append(''.join(page_content))
            pages.append(page_content)
        
        return pages    
    
    def normalize(self):
        """ 
        Normalize the page content of pdf document.
        """
        pages = list()
        for page in self.pages:
            pages.append(normalizer.normalize_break(page))
        
        return pages

    def getlines(self):
        """
        Put all lines within a pdf document in a python object.
            use list to store lines
            use tuple to store a line
        The result structure looks like:
            [(pageno, lineno, content), (1,1,'This is a line'), ...]
        """
        pageno = 0
        lineno = 0
        lines = list()
        for page in self.content:
            pageno += 1
            # line in one page
            t = page.split('\n')
            for s in t:
                lineno += 1
                line = (pageno,lineno,s)
                lines.append(line)
        
        return lines
                