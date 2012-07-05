'''
@summary: Match class file, pattern matching

@author: Micle Bu <mekery@gmail.com>
@copyright: Copyright &copy; 2012 Micle Bu
@license: BSD New
@version: pdfmatch.py 2012-04-18 Micle Bu
'''
import normalizer
from pdfdig.pdftext import Text
from pdfdig.pdfinfo import TOC

__all__ = ['Match']

class Match(list):
    def __init__(self, pattern, pdffile, icase=False, location=False, 
                 context=0, dictionary=None):
        self.pattern = pattern
        self.file = pdffile
        self.icase = icase
        self.location= location
        self.context = context
        self.dictionary = dictionary
        self.pdf = Text(pdffile)
        self.lines = self.pdf.getlines() 
                
        # result
        self.count = 0
        self.matches = self.domatch()
    
    def domatch(self):
        """
        Do the matching and counting based on lines in pdf's txt content file, 
            use tuple to store matches 
            use list to store matches within a line a file
            each match consists of line number and pattern with context
        The structure of match result looks like:
            [[(pageno, lineno, location, context),...],...]
            [[(1,1,location1, ...match...)],[(1,20,location2, ...match...),(2,32,location3, ...match...)]]
        """
        import re
        pattern = normalizer.normalize_pattern(self.pattern)
        if self.icase:
            pattern = re.compile(pattern, re.I)
        else:
            pattern = re.compile(pattern)
        
        count = 0
        results = []
        for line in self.lines:
            # line: (pageno, lineno, cotent)
            pageno = line[0]
            lineno = line[1]
            linecontent = line[2]
            if pattern.search(linecontent):
                res = []
                for match in pattern.finditer(linecontent):
                    count += 1
                    # context
                    if self.context > 0:
                        s = self.startindex(match.start(), self.context)
                        e = match.end() + self.context 
                    else:
                        s = self.startposition(match.start(), linecontent)
                        e = self.endposition(match.end(), linecontent)
                    # location
                    if self.location:
                        # toc
                        if self.dictionary:
                            toc = TOC(self.file, path=self.dictionary)
                        else:
                            toc = TOC(self.file)
                        toc_dictionary = toc.gettoc_filter_by_dictionary(self.lines)
                        location = self.matchlocation(lineno, toc_dictionary)
                    else:
                        location = 'All'              
                    res.append((pageno,lineno,location,linecontent[s:e]))
                    #print count
                results.append(res)
        self.count = count
        return results
    
    def matchlocation(self, num, toc_dictionary):
        """
        Get the location of match within TOC items        
        """        
        num_min = 0
        num_max = 0
        item_temp = (0, 'Title/Abstract')
        for item in toc_dictionary:
            num_max = item[0]
            if num >= num_min and num < num_max:
                return item_temp[1]
            else:
                num_min = num_max  
                item_temp = item            
        return item_temp[1]
    
    def startindex(self, index, offset):
        """
        Get the start index of a match with context
        """
        start = index - offset
        if start < 0:
            start = 0
        return start

    def startposition(self, start, line):
        """
        Get the start position of the sentence which contains the match.
            sentence context
        """
        s = start
        while s > 0:
            if line[s] == '.':
                return s+1
            s -= 1
        
        return s
    
    def endposition(self, end, line):
        """
        Get the end position of the sentence which contains the match.
            sentence context
        """
        e = end
        while e < len(line):
            if line[e] == '.':
                return e+1
            e += 1
        
        return e
    
    def formats(self, pfile, ppage, pnumber, highlight=False, color='red'):
        """
        Format the output of matches, one match per line, add prefix as needed.
        """
        formatted_result = []
        for s in self.matches:
            for t in s:
                # format_result.append('{0}:{1}\t:{2}\n'.format(self.file,t[0],t[1]))  
                # match content only
                prefix = ''
                if pfile:
                    prefix = '@F:{0}'.format(self.file)
                if ppage:
                    prefix = '{0} @P: {1}\t'.format(prefix, t[0])
                if pnumber:
                    prefix = '{0} @N: {1}\t'.format(prefix, t[1])
                if self.location:
                    prefix = '{0} @L: {1}\t'.format(prefix, t[2])
                
                # context
                if highlight:
                    formatted_result.append('{0} @C: {1}\n'.format(prefix, self.highlight(t[3], color))) 
                else:       
                    formatted_result.append('{0} @C: {1}\n'.format(prefix, t[3]))         
        return formatted_result

    def highlight(self, line, color):
        """
        Highlight the matched words.
        """
        import re
        pattern = normalizer.normalize_pattern(self.pattern)
        if self.icase:
            pattern = re.compile(pattern, re.I)
        else:
            pattern = re.compile(pattern)
        
        hline = ''
        start = 0
        end = len(line)
        for match in pattern.finditer(line):
            s = match.start()
            e = match.end()
            
            # highlight for bash
            # forecolor:3, backcolor: 4
            # black:0,red:1,green:2,orange:3,blue:4,purple:5,bluegreen:6,white:7+
            replace = '\x1b[0;3{0}m'.format(self.highlightcolor(color)) + line[s:e] + '\x1b[0m'
            
            hline += line[start:s]
            hline += replace
            start = e
            
        hline += line[start:end]
        
        return hline
    
    def highlightcolor(self, name):
        color = {
                 'black'    : '0',
                 'red'      : '1',
                 'green'    : '2',
                 'orange'   : '3',
                 'blue'     : '4',
                 'purple'   : '5',
                 'bluegreen': '6',
                 'white'    : '7'        
                 }
        if name in color.keys():
            return color[name]
        else:
            return color['red']
        