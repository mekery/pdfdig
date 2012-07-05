#coding=utf-8
'''
@summary: TOC class file, build Table of Contents(TOC) of PDF document.

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdfinfo.py 2012-03-28 Micle Bu
'''
from pdfdig.pdftext import Text
from pdfdig.tocdictionary import TOCDictionary
import normalizer

__all__ = ['Info']

class TOC():
    def __init__(self, pdf, 
                 minlen=4, maxlen=20, 
                 threshold=0.05, path='../docs/json'):
        self.file = pdf
        self.minlen = minlen
        self.maxlen = maxlen
        self.threshold = threshold
        self.path = path
    
    def buildtoc(self):
        # Text
        pdf = Text(self.file)
        lines = pdf.getlines()
        
        return self.gettoc(lines)
    
    def buildtoc_dict(self):
        # Text
        pdf = Text(self.file)
        lines = pdf.getlines()
        
        return self.gettoc_filter_by_dictionary(lines)
    
    def gettoc(self, lines):
        """
        Get the TOC of pdf document based on lines in pdf's txt content file, 
            use tuple to store toc item which consists of its name and line number in txt content file 
            use list to store toc within a file
        The structure of toc looks like:
            [(1, Abstract)],[(2, Introduction),(3, Methods)],[(5, Conclusion)]
        """
        import re     
               
        toc = []
        toc_filter = re.compile(r'[\\/:"*?<>|()]+', re.I)
        #toc_filter = re.compile(r'\d', re.I)
        
        for line in lines:
            # line: (pageno, lineno, cotent)
            lineno = line[1]
            linecontent = line[2]
            #print linecontent
            if len(linecontent) > self.minlen and len(linecontent) < self.maxlen:
                if not toc_filter.search(linecontent):
                    item = (lineno, normalizer.normalize_whitespace(linecontent))
                    toc.append(item)
        return toc      
    
    def gettoc_filter_by_dictionary(self, lines):
        """
        Get the TOC of pdf document based on lines in pdf's txt content file,
            use a TOC dictionary to filter TOC items
        The structure of toc looks like:
            [(1, Abstract)],[(2, Introduction),(3, Methods)],[(5, Conclusion)]
        """     
        toc_raw = self.gettoc(lines) 
        toc_dict = TOCDictionary(self.path,self.threshold)
        dictionary = toc_dict.build()
        toc = []
        for t in toc_raw:
            if normalizer.normalize_toc_item(t[1]) in dictionary.keys():
                toc.append(t)
        return toc              
    
    def formats(self, toc, pfile, pnumber):
        """
        Format the output of toc, one item per line, add prefix as needed
        """
        formatted_results = []
        for item in toc:
            prefix = ''
            if pfile:
                prefix = '{0}'.format(self.file)
            if pnumber:
                prefix = '{0}: {1}\t'.format(prefix, item[0])
            formatted_results.append('{0}: {1}\n'.format(prefix, item[1]))
        return formatted_results
            

        
        
        